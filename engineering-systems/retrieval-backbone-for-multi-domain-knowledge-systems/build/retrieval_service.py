#!/usr/bin/env python3
"""
P04 — Packaged retrieval backbone: query → answer + citation-bearing contexts.

All connection parameters come from a config object (built from env or injected).
State (Qdrant client, query engine) is **per instance** — no cross-query globals.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Any, Mapping, Sequence

import qdrant_client
from llama_index.core import Settings, PromptTemplate, VectorStoreIndex
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.vector_stores.qdrant import QdrantVectorStore

# Prompt must include {context_str} and {query_str} for default LlamaIndex text QA synthesis.
CITATION_AWARE_QA_TEMPLATE = PromptTemplate(
    template=(
        "Context information is below.\n"
        "---------------------\n"
        "{context_str}\n"
        "---------------------\n"
        "You are a helpful assistant. Use only the context above to answer the question.\n"
        "When you use information from the context, cite it explicitly using the document name, "
        "file path, or source URL shown in the context (for example: [Source: filename] or "
        "[Source: https://…]).\n"
        "If the context does not contain the answer, say you do not have enough information.\n"
        "Question: {query_str}\n"
        "Answer: "
    )
)


def _env_str(key: str, default: str) -> str:
    v = os.environ.get(key)
    return v if v is not None and v != "" else default


@dataclass(frozen=True)
class RetrievalBackboneConfig:
    """Injectable / env-backed settings. No hardcoded host paths."""

    qdrant_url: str = field(default_factory=lambda: _env_str("QDRANT_URL", "http://localhost:6333"))
    qdrant_collection: str = field(
        default_factory=lambda: _env_str("QDRANT_COLLECTION", "multi_domain_docs")
    )
    ollama_embed_model: str = field(
        default_factory=lambda: _env_str("OLLAMA_EMBED_MODEL", "nomic-embed-text")
    )
    ollama_llm_model: str = field(
        default_factory=lambda: _env_str("OLLAMA_LLM_MODEL", "llama3.2")
    )
    similarity_top_k: int = field(
        default_factory=lambda: int(_env_str("RAG_SIMILARITY_TOP_K", "3"))
    )
    ollama_request_timeout: float = field(
        default_factory=lambda: float(_env_str("OLLAMA_REQUEST_TIMEOUT", "120.0"))
    )

    @classmethod
    def from_mapping(cls, data: Mapping[str, Any] | None) -> RetrievalBackboneConfig:
        if not data:
            return cls()
        kwargs: dict[str, Any] = {}
        if "qdrant_url" in data:
            kwargs["qdrant_url"] = str(data["qdrant_url"])
        if "qdrant_collection" in data:
            kwargs["qdrant_collection"] = str(data["qdrant_collection"])
        if "ollama_embed_model" in data:
            kwargs["ollama_embed_model"] = str(data["ollama_embed_model"])
        if "ollama_llm_model" in data:
            kwargs["ollama_llm_model"] = str(data["ollama_llm_model"])
        if "similarity_top_k" in data:
            kwargs["similarity_top_k"] = int(data["similarity_top_k"])
        if "ollama_request_timeout" in data:
            kwargs["ollama_request_timeout"] = float(data["ollama_request_timeout"])
        return cls(**kwargs)


@dataclass
class CitationRecord:
    node_id: str
    score: float | None
    label: str
    source_url: str | None
    text_excerpt: str


@dataclass
class QueryResult:
    """Public contract: answer string + Ragas-shaped contexts + structured citations."""

    answer: str
    contexts: list[str]
    citations: list[CitationRecord]


def _response_text(response: object) -> str:
    r = getattr(response, "response", None)
    if r is not None:
        return str(r).strip()
    return str(response).strip()


def source_nodes_to_context_strings(source_nodes: Sequence[Any]) -> list[str]:
    """Map LlamaIndex source nodes to Ragas `retrieved_contexts` (list of strings)."""
    out: list[str] = []
    for sn in source_nodes:
        node = getattr(sn, "node", None)
        if node is None:
            continue
        text = node.get_content().strip()
        if text:
            out.append(text)
    return out


def source_nodes_to_citations(source_nodes: Sequence[Any], excerpt_len: int = 400) -> list[CitationRecord]:
    records: list[CitationRecord] = []
    for sn in source_nodes:
        node = getattr(sn, "node", None)
        if node is None:
            continue
        node_id = str(getattr(node, "node_id", None) or getattr(node, "id_", "?"))
        score = getattr(sn, "score", None)
        score_f: float | None
        try:
            score_f = float(score) if score is not None else None
        except (TypeError, ValueError):
            score_f = None
        meta = node.metadata or {}
        label = (
            meta.get("file_name")
            or meta.get("file_path")
            or meta.get("source_url")
            or str(meta.get("document_id", "unknown"))
        )
        source_url = meta.get("source_url")
        if source_url is not None:
            source_url = str(source_url)
        snippet = node.get_content().strip().replace("\n", " ")
        if len(snippet) > excerpt_len:
            snippet = snippet[: excerpt_len - 3] + "..."
        records.append(
            CitationRecord(
                node_id=node_id,
                score=score_f,
                label=str(label),
                source_url=source_url,
                text_excerpt=snippet,
            )
        )
    return records


class RetrievalBackboneService:
    """
    Instance-scoped service: one Qdrant client + one query engine per instance.

    Thread-safety: treat as **not** thread-safe unless each thread uses its own instance.
    """

    def __init__(self, config: RetrievalBackboneConfig | None = None) -> None:
        self._config = config or RetrievalBackboneConfig()
        self._client: qdrant_client.QdrantClient | None = None
        self._query_engine: object | None = None

    @property
    def config(self) -> RetrievalBackboneConfig:
        return self._config

    def _ensure_engine(self) -> object:
        if self._query_engine is not None:
            return self._query_engine

        cfg = self._config
        Settings.embed_model = OllamaEmbedding(model_name=cfg.ollama_embed_model)
        Settings.llm = Ollama(
            model=cfg.ollama_llm_model,
            request_timeout=cfg.ollama_request_timeout,
        )

        self._client = qdrant_client.QdrantClient(url=cfg.qdrant_url)
        self._client.get_collections()

        vector_store = QdrantVectorStore(
            client=self._client,
            collection_name=cfg.qdrant_collection,
        )
        index = VectorStoreIndex.from_vector_store(
            vector_store=vector_store,
            embed_model=Settings.embed_model,
        )
        self._query_engine = index.as_query_engine(
            similarity_top_k=cfg.similarity_top_k,
            text_qa_template=CITATION_AWARE_QA_TEMPLATE,
        )
        return self._query_engine

    def query(self, question: str) -> QueryResult:
        """Run retrieval + synthesis; return answer and contexts suitable for Ragas."""
        qe = self._ensure_engine()
        result = qe.query(question)
        nodes = getattr(result, "source_nodes", None) or []
        answer = _response_text(result)
        contexts = source_nodes_to_context_strings(nodes)
        citations = source_nodes_to_citations(nodes)
        return QueryResult(answer=answer, contexts=contexts, citations=citations)

# Case study — canonical queries

Strings below match **`build/ragas_eval.py`** `batch_rows()` so manual **`query_pipeline.py`** checks align with **Ragas** batch eval.

## Ragas batch (three domains)

### `markdown_file`

```text
What vector database does the indexed documentation say is used locally in this series?
```

### `pdf_topic`

```text
According to the indexed corpus, what file type can Unstructured partition for the same Qdrant collection as Markdown?
```

### `web_synthetic`

```text
According to the indexed documentation about Python environment variables, what does PEP 405 describe?
```

## Ragas baseline (single row)

Same as **`markdown_file`** question in `baseline_rows()`:

```text
What vector database does the indexed documentation say is used locally in this series?
```

## Extra manual checks (P02 / consumer)

Use with **`query_pipeline.py --query "…"`** or **`consumer_demo.py --query "…"`**:

```text
What does the corpus say about PDF ingestion?
```

```text
What topics appear in the sample corpus?
```

(Second line mirrors common P02 smoke; first appears in [../../build/README.md](../../build/README.md) consumer example.)

---
license: mit
language:
  - en
pretty_name: Openapi LLM Wiki
size_categories:
  - n<1K
task_categories:
  - question-answering
  - text-generation
tags:
  - llms-txt
  - rag
  - knowledge-base
  - openapi
  - openapi-specification
  - api-documentation
  - business-data
  - context-engineering
configs:
  - config_name: default
    data_files:
      - split: train
        path: data/knowledge.jsonl
---

# Openapi LLM Wiki

An LLM-optimized knowledge base for the [Openapi®](https://openapi.com) API marketplace, the
largest certified API marketplace in Europe. Use it to ground chat assistants, RAG pipelines and
AI agents on Openapi's company profile, platform conventions, API catalog and endpoints.

- **Source repository**: https://github.com/openapi/openapi-llm-wiki (the source of truth, this
  dataset is synced from its releases)
- **Single-file version**: [`llms-full.txt`](llms-full.txt)
- **Index**: [`llms.txt`](llms.txt), following the [llms.txt](https://llmstxt.org) convention

## Contents

`data/knowledge.jsonl` has one record per file of the knowledge base:

| Field | Description |
|---|---|
| `id` | Stable identifier, e.g. `platform-guide`, `service/company`, `oas/company` |
| `kind` | `core` (company, catalog, platform guide, FAQ, references), `service` (endpoint reference) or `oas` (OpenAPI 3 spec) |
| `service` | Service slug for `service` and `oas` records, `null` for `core` |
| `title` | Document title |
| `path` | Path of the file in the source repository |
| `format` | `markdown` or `openapi-json` |
| `content` | Full file content |

The raw files are also included under `knowledge/`, with the same layout as the GitHub repository.

## Usage

```python
from datasets import load_dataset

ds = load_dataset("HF_DATASET_REPO", split="train")

# Everything an agent needs to call the Company API
context = [r["content"] for r in ds if r["id"] in ("platform-guide", "service/company")]
```

Or fetch the single file directly:

```bash
curl -L https://huggingface.co/datasets/HF_DATASET_REPO/resolve/main/llms-full.txt
```

## Recommended loading pattern

Always pair a `service` record with `platform-guide` (authentication, scopes, billing, sandbox and
async patterns are shared by every service). Use the matching `oas` record when the model has to
generate exact requests.

## Updates

The OpenAPI specs are refreshed weekly from `https://console.openapi.com/oas/en/<service>.openapi.json`
and every GitHub release is pushed here. The [API Library](https://console.openapi.com/apis) is the
authoritative source for which APIs are active or deprecated.

## License

MIT, © Openapi®. Cite with the metadata in the source repository's `CITATION.cff`.

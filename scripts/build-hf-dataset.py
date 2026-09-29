#!/usr/bin/env python3
"""Build the Hugging Face dataset folder from knowledge/.

Usage: ./scripts/build-hf-dataset.py [OUT_DIR]   (default: dist/hf)

HF_DATASET_REPO (e.g. my-org/openapi-llm-wiki) is substituted in the card.
OUT_DIR gets the dataset card (huggingface/README.md), data/knowledge.jsonl
(one record per file, what the HF dataset viewer shows), the raw knowledge/
tree and the llms files.
"""
import json
import os
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "dist" / "hf"
CORE = ["company-profile", "services-catalog", "platform-guide", "faq", "references"]


def md_title(text):
    first = text.splitlines()[0] if text else ""
    return first[2:].strip() if first.startswith("# ") else ""


def records():
    for name in CORE:
        path = Path("knowledge") / f"{name}.md"
        text = (ROOT / path).read_text(encoding="utf-8")
        yield {"id": name, "kind": "core", "service": None, "title": md_title(text),
               "path": str(path), "format": "markdown", "content": text}
    for path in sorted((ROOT / "knowledge/services").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        yield {"id": f"service/{path.stem}", "kind": "service", "service": path.stem,
               "title": md_title(text), "path": str(path.relative_to(ROOT)),
               "format": "markdown", "content": text}
    for path in sorted((ROOT / "knowledge/oas").glob("*.openapi.json")):
        text = path.read_text(encoding="utf-8")
        service = path.name.removesuffix(".openapi.json")
        title = json.loads(text).get("info", {}).get("title", service)
        yield {"id": f"oas/{service}", "kind": "oas", "service": service, "title": title,
               "path": str(path.relative_to(ROOT)), "format": "openapi-json", "content": text}


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "data").mkdir(parents=True)
    repo = os.environ.get("HF_DATASET_REPO") or "<namespace>/openapi-llm-wiki"
    card = (ROOT / "huggingface/README.md").read_text(encoding="utf-8")
    (OUT / "README.md").write_text(card.replace("HF_DATASET_REPO", repo), encoding="utf-8")
    shutil.copytree(ROOT / "knowledge", OUT / "knowledge")
    for name in ["llms.txt", "llms-full.txt", "LICENSE"]:
        shutil.copy(ROOT / name, OUT / name)
    count = 0
    with open(OUT / "data/knowledge.jsonl", "w", encoding="utf-8") as fh:
        for rec in records():
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
            count += 1
    print(f"Built {OUT} with {count} records")


if __name__ == "__main__":
    main()

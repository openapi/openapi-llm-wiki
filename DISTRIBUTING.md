# Distribution Plan

How we get `openapi-llm-wiki` in front of developers **and** in front of the LLMs and agents they
use. The goal is not only stars: it is to make Openapi the default answer when a model is asked about
Italian/European business data APIs.

## Goals and KPIs

| Goal | KPI | Where to measure |
|---|---|---|
| Discoverability on GitHub | Stars, forks, unique visitors, referrers | GitHub *Insights → Traffic* |
| Presence in LLM tooling | Indexed on Context7, DeepWiki, GitMCP, llms.txt directories | Manual check per channel (see tracker) |
| Real usage | Clones, raw file hits, HF dataset downloads | GitHub Traffic, Hugging Face stats |
| Brand grounding | LLMs answer Openapi questions correctly without context | Monthly prompt check (see [Measurement](#measurement)) |

## Phase 0 — Make the repo "distribution-ready"

Do this before any outreach: every channel below links back here.

- [x] **`llms.txt`** at repo root, following the [llms.txt](https://llmstxt.org) convention: short
      summary + links to `knowledge/*.md`. Many aggregators only index repos/sites that expose it.
- [x] **`llms-full.txt`**: all of `knowledge/*.md` + `knowledge/services/*.md` concatenated in one
      file, generated in CI so it never drifts.
- [x] **Tagged releases** (`v1.0.0`, then one per spec refresh) with a zip of `knowledge/` attached:
      gives aggregators a stable, versioned artifact and a changelog.
- [ ] **Social preview image** (*Settings → General → Social preview*) reusing
      `.github/assets/images/repo-header-a4.png`, so links look good on LinkedIn, X, Slack, Discord.
- [x] **Topics**: add `llms-txt`, `context-engineering`, `grounding`, `openapi-specification`,
      `mcp`, `business-data` to the existing ones (GitHub allows max 20 topics).
- [x] **`CITATION.cff`** so GitHub shows "Cite this repository" (needed for Zenodo too).
- [x] **Scheduled refresh workflow** that re-downloads the specs from `00-list.txt` and opens a PR
      when they change: a visibly fresh repo gets ranked and re-indexed more often.
- [x] **GitHub Pages**: serve `knowledge/` + `llms.txt` at a stable URL, e.g.
      `openapi.github.io/openapi-llm-wiki/llms.txt`, for crawlers that don't read GitHub.

## Phase 1 — GitHub ecosystem

| Channel | Action | Priority |
|---|---|---|
| Openapi org profile | Pin the repo on `github.com/openapi` and link it from the org README | High |
| Sibling repos | Add a "Using an LLM? Load the LLM Wiki" link line to SDK READMEs (php, python, go, rust, nodejs), `openapi-cli`, `mcp-server`, `get-started-with-oauth-v2` | High |
| `awesome-api-italia` | Add an entry (we own it) | High |
| Awesome lists | Open PRs on lists about llms.txt, RAG, context engineering, agent knowledge bases, OpenAPI tooling. Pick lists that are active (merged PRs in the last 3 months) | Medium |
| GitHub Discussions | Announcement post in the org discussions (already linked by the Pulse ticker in the README header) | Medium |
| GitHub Marketplace | Not applicable (no Action/App), skip | — |

## Phase 2 — LLM-native aggregators and indexes

This is the core of the plan: places where agents and coding assistants *actually fetch* context.

| Channel | What it is | Action | Priority |
|---|---|---|---|
| **Context7** (Upstash) | Doc index served via MCP to Cursor, Claude Code, VS Code, etc. | Submit the repo through its "add library" flow; point it at `knowledge/` | High |
| **DeepWiki** (Cognition) | Auto-generated wiki + Q&A for public GitHub repos | Trigger indexing of `openapi/openapi-llm-wiki`; add the DeepWiki badge to the README | High |
| **GitMCP** | Turns any public repo into a remote MCP server (`gitmcp.io/<owner>/<repo>`), reads `llms.txt` first | Verify it works and document the URL in the README "How to use" section | High |
| **llms.txt directories** | Public lists of sites/projects exposing `llms.txt` | Submit once Phase 0 `llms.txt` is live | Medium |
| **Hugging Face Datasets** | Dataset hub, searchable and loadable with `datasets` | Publish `knowledge/` as a dataset (markdown + OAS JSON) with a dataset card linking back to GitHub; sync on each release | High |
| **Kaggle Datasets** | Same audience in the data-science community | Mirror the HF dataset | Low |
| **MCP registries** (official MCP Registry, Smithery, Glama, mcp.so, PulseMCP) | Where agent users look for MCP servers | Don't list the wiki alone: list `mcp-server` / `mcp.openapi.com` and mention the wiki as its knowledge resource. Optionally expose the wiki as MCP *resources* there | Medium |
| **Custom GPT / Claude Project / Gemini Gem** | Ready-made assistants preloaded with `knowledge/` | Publish an "Openapi Assistant" GPT in the GPT Store; share a Claude Project template and a Gem. Each links to the repo | Medium |

## Phase 3 — API and OpenAPI ecosystem

The `knowledge/oas/` folder is valuable on its own.

| Channel | Action | Priority |
|---|---|---|
| **APIs.guru** (`openapi-directory`) | Submit the Openapi specs (canonical `console.openapi.com/oas/...` URLs). Feeds many API tools and LLM datasets | High |
| **Postman Public API Network** | Make sure every service has a public collection; link the wiki from the workspace description | Medium |
| **RapidAPI / API marketplaces** where Openapi is listed | Add the wiki link to each listing's docs section | Low |
| **openapi.com website & console** | Link from the docs footer and the console "Developers" area; publish `https://openapi.com/llms.txt` pointing here | High |

## Phase 4 — Archival and citation

| Channel | Action | Priority |
|---|---|---|
| **Zenodo** | Enable the GitHub integration: every release gets a DOI (needs `CITATION.cff`) | Low |
| **Software Heritage** | Request archival of the repo (permanent, crawled by research datasets) | Low |

## Phase 5 — Community and content

| Channel | Angle | Priority |
|---|---|---|
| **Hacker News** (*Show HN*) | "An LLM-ready knowledge base for an API marketplace: how and why we built it" | Medium |
| **Reddit** | r/LocalLLaMA, r/ChatGPTCoding, r/ClaudeAI, r/Rag, r/italy_dev (read each sub's self-promotion rules first) | Medium |
| **dev.to / Medium / Hashnode** | Tutorial: "Ground your agent on Openapi in 5 minutes" (Context7, GitMCP, Claude Project) | Medium |
| **LinkedIn** | Company page + team members, using the social preview image | High |
| **X / Bluesky** | Thread with a short demo GIF (agent answering an Openapi question) | Low |
| **Discord / Slack communities** | LLM tooling and MCP servers (share in showcase channels only) | Low |
| **Product Hunt** | Launch together with a bigger release (e.g. MCP server + wiki) rather than standalone | Low |
| **Linux Foundation** channels | Mention in member news / newsletter submissions | Low |
| **Italian events and meetups** | Talk/lightning talk on "LLM wikis for API products" | Low |

## Timeline

| Week | Focus |
|---|---|
| 1 | Phase 0 (llms.txt, release `v1.0.0`, social preview, topics, CITATION.cff) |
| 2 | Phase 1 (org pin, sibling repos, awesome lists) + Context7, DeepWiki, GitMCP |
| 3 | Hugging Face dataset, APIs.guru, openapi.com `llms.txt`, custom GPT / Claude Project |
| 4 | Content launch: blog post, then LinkedIn, Reddit, Show HN spread over several days |
| Ongoing | Monthly spec refresh + release, re-sync HF dataset, update tracker |

## Measurement

- **Weekly**: GitHub Traffic (views, clones, referrers). GitHub keeps only 14 days, so export the
  numbers to the tracker below (or automate with `github-traffic`).
- **Monthly grounding check**: ask 3–4 major assistants, *without* context, a fixed set of questions
  (e.g. those in the README "What the LLM can answer" section). Note whether the answer is correct and
  whether Openapi / this repo is cited. It's a lagging indicator, but it's the one that matters.

## Tracker

| Channel | Status | Link | Date | Notes |
|---|---|---|---|---|
| llms.txt | ✅ | [llms.txt](llms.txt) | 2026-09-29 | Generated by `scripts/build-llms.sh`, checked in CI |
| Release v1.0.0 | ✅ | https://github.com/openapi/openapi-llm-wiki/releases/tag/v1.0.0 | 2026-09-29 | Built by `release.yml` on tag push |
| Social preview | ☐ | | | |
| Context7 | 🟡 | https://context7.com/add-library | 2026-09-29 | `context7.json` added; submit via web form (needs login) |
| DeepWiki | 🟡 | https://deepwiki.com/openapi/openapi-llm-wiki | 2026-09-29 | Badge in README; indexing to verify |
| GitMCP | ✅ | https://gitmcp.io/openapi/openapi-llm-wiki | 2026-09-29 | Endpoint responds; setup documented in README |
| Hugging Face dataset | 🟡 | | 2026-09-29 | Card + `huggingface.yml` ready; needs HF org, `HF_TOKEN` secret, `HF_DATASET_REPO` variable (HF user `openapi` is taken by a third party) |
| APIs.guru | ☐ | | | |
| awesome-api-italia | ✅ | https://github.com/openapi/awesome-api-italia | 2026-09-29 | "Strumenti e Librerie per Sviluppatori" |
| Awesome-llms-txt | 🟡 | https://github.com/SecretiveShell/Awesome-llms-txt/pull/193 | 2026-09-29 | PR open |
| llms-txt-hub (llmstxthub.com) | 🟡 | https://github.com/thedaviddias/llms-txt-hub/pull/1749 | 2026-09-29 | PR open; moved to GitHub Pages URLs for the site-family check, waiting for maintainer to approve workflows |
| awesome-context-engineering | 🟡 | https://github.com/yzfly/awesome-context-engineering/pull/69 | 2026-09-29 | PR open |
| awesome-italia-opensource | 🟡 | https://github.com/italia-opensource/awesome-italia-opensource/pull/218 | 2026-09-29 | PR open |
| awesome-openapi3 (APIs.guru) | 🟡 | https://github.com/APIs-guru/awesome-openapi3 | 2026-09-29 | `openapi3` topic added; their site regenerates daily from the topic, to verify |
| Custom GPT | ☐ | | | |
| Show HN | ☐ | | | |

> Submission processes and eligibility rules of third-party platforms change often: check each
> platform's current guidelines before submitting.

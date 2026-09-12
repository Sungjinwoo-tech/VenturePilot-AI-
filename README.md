# VenturePilot AI â€” Pakistan Cyber Law RAG Assistant

A working Streamlit + FAISS + RAG application for asking questions about Pakistan cyber-law documents.

## What it does

1. Downloads the configured official/legal PDF sources when they are not already in `data/`.
2. Extracts PDF text with `pypdf`.
3. Splits the law into overlapping chunks.
4. Creates semantic embeddings with Sentence Transformers on first startup.
5. Stores a FAISS vector index in `cache/`.
6. Retrieves the most relevant passages for each question.
7. If `OPENAI_API_KEY` is configured, generates a grounded answer using the retrieved passages.
8. Shows the retrieved source document and page for transparency.

## Run locally

```bash
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

### Optional LLM configuration

Create `.streamlit/secrets.toml`:

```toml
OPENAI_API_KEY = "your-key-here"
OPENAI_MODEL = "gpt-4o-mini"
```

You can also set environment variables instead:

```text
OPENAI_API_KEY=...
OPENAI_MODEL=gpt-4o-mini
```

Without an API key, the application still performs retrieval and displays the relevant legal passages; the generated-answer layer is disabled.

## Streamlit Cloud

1. Push this folder to GitHub.
2. Create a Streamlit app pointing to `app.py`.
3. Add `OPENAI_API_KEY` and optionally `OPENAI_MODEL` under Streamlit Secrets.
4. Deploy.

The application downloads the configured PDF sources and creates embeddings on startup. The first startup can take longer because the embedding model must be downloaded and the FAISS index created.

## Current knowledge sources

- Prevention of Electronic Crimes Act, 2016 (Pakistan Code):
  https://www.pakistancode.gov.pk/pdffiles/administrator6a061efe0ed5bd153fa8b79b8eb4cba7.pdf
- Removal and Blocking of Unlawful Online Content (Procedure, Oversight and Safeguards) Rules, 2021 (MoITT):
  https://moitt.gov.pk/SiteImage/Misc/files/Removal%20Blocking%20of%20Unlawful%20Online%20Content%20Rules%202021.PDF

The Ministry of IT & Telecommunication legislation page lists PECA and the 2021 online-content rules among approved legislation/rules. Always verify important legal questions against the latest official Gazette/law source.

## Project structure

```text
VenturePilot_AI/
â”œâ”€â”€ app.py
â”œâ”€â”€ rag_engine.py
â”œâ”€â”€ requirements.txt
â”œâ”€â”€ README.md
â”œâ”€â”€ .gitignore
â”œâ”€â”€ data/
â”‚   â””â”€â”€ .gitkeep
â””â”€â”€ cache/
    â””â”€â”€ .gitkeep
```

## Important legal disclaimer

VenturePilot AI is an educational/information tool, not a law firm or a lawyer. Laws can be amended, repealed, challenged, or interpreted by courts. Do not rely on an AI response alone for a legal decision.

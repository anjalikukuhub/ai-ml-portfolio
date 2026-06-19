# 🔗 Project 02 — Candidate Matching Engine

> Match the right candidates to the right roles using semantic similarity

---

## 🎯 Problem Statement

Keyword-based resume matching misses great candidates who describe their skills differently. A candidate who writes "people management" shouldn't be penalized vs one who writes "team leadership." This engine understands *meaning*, not just words.

## 💡 Solution

Uses **sentence transformers** to embed resumes and job descriptions into a shared vector space, then ranks candidates by semantic closeness to each role.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| `sentence-transformers` | Semantic embeddings |
| `FAISS` | Fast vector similarity search |
| `pandas` | Data processing |
| `Streamlit` | Web interface |

---

## ▶️ How to Run

```bash
cd projects/02-candidate-matching-engine
pip install -r requirements.txt
streamlit run app.py
```

## 🔮 Future Improvements
- Multi-role matching in one pass
- Candidate self-scoring interface
- ATS integration via API

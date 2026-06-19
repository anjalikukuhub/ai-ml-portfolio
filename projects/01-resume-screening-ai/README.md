# 📄 Project 01 — Resume Screening AI

> Automatically ranks and scores resumes against a Job Description using NLP

---

## 🎯 Problem Statement

Recruiters receive **hundreds of resumes** per job posting. Manually reading each one is time-consuming and prone to unconscious bias. This tool automates the initial screening layer — ranking candidates by relevance so recruiters can focus on the top matches.

## 💡 Solution

An NLP pipeline that:
1. Parses resumes (PDF/DOCX)
2. Extracts key skills, experience, and education
3. Compares against a Job Description using TF-IDF + cosine similarity
4. Outputs a ranked shortlist with match scores

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| `PyMuPDF` / `python-docx` | Resume parsing |
| `spaCy` | NLP entity extraction |
| `scikit-learn` | TF-IDF vectorizer + cosine similarity |
| `pandas` | Data handling |
| `Streamlit` | Web interface |

## ▶️ How to Run

```bash
cd projects/01-resume-screening-ai
pip install -r requirements.txt
python main.py --jd "path/to/jd.txt" --resumes "path/to/resumes/"
```

## 🔮 Future Improvements
- Add bias detection layer
- Support for LinkedIn profile URLs
- Integration with ATS systems (Workday, Greenhouse)

---

## 📁 File Structure

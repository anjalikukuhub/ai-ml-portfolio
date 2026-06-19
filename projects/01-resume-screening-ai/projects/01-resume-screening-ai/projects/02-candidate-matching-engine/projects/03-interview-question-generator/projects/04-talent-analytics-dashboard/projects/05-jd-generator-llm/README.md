# 📝 Project 05 — JD Generator with LLM

> Generate professional, bias-free Job Descriptions in seconds using GPT

---

## 🎯 Problem Statement

Writing a compelling, inclusive Job Description takes time — and it's easy to accidentally include biased language that discourages diverse candidates. This tool generates structured, bias-aware JDs instantly.

## 💡 Solution

A Streamlit web app where recruiters input:
- Job title
- Department
- Key responsibilities
- Must-have skills

And receive a fully formatted, bias-checked JD ready to post.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| `OpenAI GPT-4` | JD generation |
| `LangChain` | Prompt management |
| `Streamlit` | Web interface |
| `python-dotenv` | API key management |

Role: Senior Data Analyst — Growth Team
About the Role:

We are looking for a curious, collaborative Senior Data Analyst to join our

Growth team...
What You'll Do:

Analyze large datasets to identify trends
Build dashboards in Tableau / Power BI
Partner with product and marketing on experimentation

What We're Looking For:

3+ years in data analysis
Proficiency in SQL and Python

[Bias Check: ✅ No gendered language | ✅ Inclusive tone]

## ▶️ How to Run

```bash
cd projects/05-jd-generator-llm
pip install -r requirements.txt
cp .env.example .env
# Add your OpenAI API key to .env
streamlit run app.py
```

## 🔮 Future Improvements
- Tone selector (startup vs enterprise)
- Auto-post to LinkedIn / Naukri
- Multi-language JD support

---

## 📸 Sample Output

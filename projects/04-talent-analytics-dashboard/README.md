# 📊 Project 04 — Talent Analytics Dashboard

> Visual dashboard for hiring pipeline metrics — built with Streamlit + Plotly

---

## 🎯 Problem Statement

Hiring data is often scattered across spreadsheets and ATS exports. This dashboard centralizes key recruiting metrics into one visual, interactive view.

## 💡 Solution

Upload your hiring pipeline CSV and get an instant dashboard with:
- Time-to-hire by department
- Offer acceptance rate trends
- Source of hire breakdown
- Pipeline funnel visualization
- Diversity metrics (optional)

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| `pandas` | Data processing |
| `plotly` | Interactive charts |
| `Streamlit` | Dashboard framework |

---

## 📈 Metrics Tracked

| Metric | Description |
|--------|-------------|
| Time to Fill | Days from requisition open to offer accepted |
| Time to Hire | Days from first contact to offer accepted |
| Offer Acceptance Rate | % of offers accepted |
| Source of Hire | LinkedIn / Naukri / Referral / Direct |
| Interview-to-Offer Ratio | Efficiency of interview process |
| Pipeline Conversion | % moving through each stage |

---

## ▶️ How to Run

```bash
cd projects/04-talent-analytics-dashboard
pip install -r requirements.txt
streamlit run dashboard.py
```

## 🔮 Future Improvements
- Real-time ATS sync (Workday API)
- Predictive time-to-fill model
- Automated weekly PDF report

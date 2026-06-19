"""
JD Generator with LLM
Author: Anjali Singh
Description: Generates professional, bias-free Job Descriptions using OpenAI GPT
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_jd(
    job_title: str,
    department: str,
    responsibilities: list,
    required_skills: list,
    experience_years: int,
    company_name: str = "Our Company"
) -> str:

    responsibilities_text = "\n".join(f"- {r}" for r in responsibilities)
    skills_text = "\n".join(f"- {s}" for s in required_skills)

    prompt = f"""
You are an expert HR professional and technical writer. Generate a professional, 
inclusive, and bias-free Job Description for the following role.

Use gender-neutral language. Avoid words like "rockstar", "ninja", "aggressive" 
that discourage diverse applicants.

Job Details:
- Title: {job_title}
- Department: {department}
- Company: {company_name}
- Minimum Experience: {experience_years} years

Key Responsibilities:
{responsibilities_text}

Required Skills:
{skills_text}

Format with these sections:
1. About the Role
2. What You'll Do
3. What We're Looking For
4. Why Join Us
5. Bias Check Summary
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=1000
    )

    return response.choices[0].message.content


def main():
    jd = generate_jd(
        job_title="Senior Talent Acquisition Specialist",
        department="Human Resources",
        responsibilities=[
            "Lead end-to-end recruitment for mid to senior-level roles",
            "Partner with hiring managers to define role requirements",
            "Build talent pipelines using AI-powered tools",
            "Analyze hiring metrics and present insights to leadership"
        ],
        required_skills=[
            "4+ years of talent acquisition experience",
            "Proficiency with ATS platforms (Workday, Greenhouse)",
            "Strong communication and stakeholder management",
            "Familiarity with AI recruiting tools is a plus"
        ],
        experience_years=4,
        company_name="TechCorp India"
    )

    print("\n" + "=" * 60)
    print("GENERATED JOB DESCRIPTION")
    print("=" * 60)
    print(jd)


if __name__ == "__main__":
    main()

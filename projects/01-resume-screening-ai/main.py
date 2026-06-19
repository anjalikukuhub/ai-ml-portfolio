"""
Resume Screening AI
Author: Anjali Singh
Description: Ranks resumes against a Job Description using NLP + cosine similarity
"""

import os
import argparse
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def read_text_file(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def load_resumes(folder_path: str) -> dict:
    resumes = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            filepath = os.path.join(folder_path, filename)
            resumes[filename.replace(".txt", "")] = read_text_file(filepath)
    return resumes


def score_resumes(jd_text: str, resumes: dict) -> pd.DataFrame:
    candidates = list(resumes.keys())
    texts = [jd_text] + list(resumes.values())

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(texts)

    scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    results = pd.DataFrame({
        "Candidate": candidates,
        "Match Score (%)": (scores * 100).round(2)
    }).sort_values("Match Score (%)", ascending=False).reset_index(drop=True)

    results.index += 1
    results.index.name = "Rank"
    return results


def main():
    parser = argparse.ArgumentParser(description="Resume Screening AI")
    parser.add_argument("--jd", required=True, help="Path to Job Description .txt file")
    parser.add_argument("--resumes", required=True, help="Path to folder containing resume .txt files")
    args = parser.parse_args()

    print("\n🔍 Loading Job Description...")
    jd_text = read_text_file(args.jd)

    print("📂 Loading Resumes...")
    resumes = load_resumes(args.resumes)
    print(f"   Found {len(resumes)} resumes.\n")

    print("⚙️  Scoring resumes against JD...\n")
    results = score_resumes(jd_text, resumes)

    print("=" * 50)
    print("📊 RANKED RESULTS")
    print("=" * 50)
    print(results.to_string())

    output_path = "screening_results.csv"
    results.to_csv(output_path)
    print(f"\n✅ Results saved to {output_path}")


if __name__ == "__main__":
    main()

from data_loader import load_all_resumes, load_all_jobs
from elite_scorer import elite_score

resumes = load_all_resumes("data/resume")
jobs = load_all_jobs("data/jobs")

job_text = list(jobs.values())[0]

print("Elite Resume Scoring:\n")

for name, resume_text in resumes.items():
    final, semantic, skill = elite_score(resume_text, job_text)
    print(f"{name}")
    print(f"  Semantic: {semantic:.3f}")
    print(f"  Skill (weighted): {skill:.3f}")
    print(f"  Final Score: {final:.3f}\n")

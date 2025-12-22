from data_loader import load_all_resumes, load_all_jobs
from job_aware_scorer import job_aware_score

resumes = load_all_resumes("data/resume")
jobs = load_all_jobs("data/jobs")

job_text = list(jobs.values())[0]

print("Job-Aware Resume Scoring:\n")

for name, resume_text in resumes.items():
    final, semantic, skill = job_aware_score(resume_text, job_text)
    print(f"{name}")
    print(f"  Semantic: {semantic:.3f}")
    print(f"  Skill Strength: {skill:.3f}")
    print(f"  Final Score: {final:.3f}\n")

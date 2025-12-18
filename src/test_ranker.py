from data_loader import load_all_resumes, load_all_jobs
from ranker import rank_resumes

resumes = load_all_resumes("data/resume")
jobs = load_all_jobs("data/jobs")

job_text = list(jobs.values())[0]

ranked = rank_resumes(resumes, job_text)

print("Resume Ranking:")
for name, score in ranked:
    print(f"{name}: {score:.3f}")

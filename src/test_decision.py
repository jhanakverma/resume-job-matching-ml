from data_loader import load_all_resumes, load_all_jobs
from ranker import rank_resumes
from decision import make_decision

resumes = load_all_resumes("data/resume")
jobs = load_all_jobs("data/jobs")

job_text = list(jobs.values())[0]

ranked = rank_resumes(resumes, job_text)

print("Final Hiring Decisions:\n")

for name, score in ranked:
    decision = make_decision(score)
    print(f"{name}: {score:.3f} → {decision}")

from data_loader import load_all_resumes, load_all_jobs
from final_scorer import final_score

resumes = load_all_resumes("data/resume")
jobs = load_all_jobs("data/jobs")

job_text = list(jobs.values())[0]

print("Skill-aware Resume Ranking:\n")

for name, resume_text in resumes.items():
    final, semantic, skill = final_score(resume_text, job_text)
    print(f"{name}")
    print(f"  Semantic Score: {semantic:.3f}")
    print(f"  Skill Score:    {skill:.3f}")
    print(f"  Final Score:    {final:.3f}\n")

from data_loader import load_all_resumes, load_all_jobs

resumes = load_all_resumes("data/resume")
jobs = load_all_jobs("data/jobs")

print("RESUMES:")
print(resumes)

print("\nJOBS:")
print(jobs)

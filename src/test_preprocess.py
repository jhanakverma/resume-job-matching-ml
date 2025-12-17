from data_loader import load_all_resumes, load_all_jobs
from preprocess import clean_text

resumes = load_all_resumes("data/resume")
jobs = load_all_jobs("data/jobs")

print("CLEANED RESUMES:\n")
for name, text in resumes.items():
    print(name)
    print(clean_text(text))
    print()

print("CLEANED JOBS:\n")
for name, text in jobs.items():
    print(name)
    print(clean_text(text))
    print()

from data_loader import load_all_resumes, load_all_jobs
from preprocess import clean_text
from embedder import get_embedding

resumes = load_all_resumes("data/resume")
jobs = load_all_jobs("data/jobs")

resume_text = clean_text(list(resumes.values())[0])
job_text = clean_text(list(jobs.values())[0])

resume_embedding = get_embedding(resume_text)
job_embedding = get_embedding(job_text)

print("Resume embedding length:", len(resume_embedding))
print("Job embedding length:", len(job_embedding))

import os

def load_text(file_path):
    """
    Reads text from a file and returns it as a string
    """
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    return text


def load_all_resumes(resume_folder):
    resumes = {}
    for file_name in os.listdir(resume_folder):
        file_path = os.path.join(resume_folder, file_name)
        resumes[file_name] = load_text(file_path)
    return resumes


def load_all_jobs(job_folder):
    jobs = {}
    for file_name in os.listdir(job_folder):
        file_path = os.path.join(job_folder, file_name)
        jobs[file_name] = load_text(file_path)
    return jobs

from document_loader import load_document
import os

def load_all_resumes(folder_path):
    resumes = {}
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        resumes[file_name] = load_document(file_path)
    return resumes

def load_all_jobs(folder_path):
    jobs = {}
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        jobs[file_name] = load_document(file_path)
    return jobs

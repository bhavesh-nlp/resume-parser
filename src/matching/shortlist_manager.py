import os
import json
import shutil
from datetime import datetime


def save_shortlisted_resume(
    resume_path: str,
    result: dict,
    base_dir: str = "data/shortlisted"
):
    #  Resolve absolute paths
    project_root = os.getcwd()
    base_dir = os.path.join(project_root, base_dir)

    resumes_dir = os.path.join(base_dir, "resumes")
    metadata_dir = os.path.join(base_dir, "metadata")

    os.makedirs(resumes_dir, exist_ok=True)
    os.makedirs(metadata_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    resume_name = os.path.basename(resume_path)

    resume_dest = os.path.join(resumes_dir, f"{timestamp}_{resume_name}")
    meta_dest = os.path.join(metadata_dir, f"{timestamp}_{resume_name}.json")

    # HARD DEBUG (do not remove yet)
    print("[SHORTLIST] Source resume:", resume_path)
    print("[SHORTLIST] Saving resume to:", resume_dest)
    print("[SHORTLIST] Saving metadata to:", meta_dest)

    #  Copy resume
    shutil.copy2(resume_path, resume_dest)

    #  Save metadata
    with open(meta_dest, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4)

    return resume_dest, meta_dest

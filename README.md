# Resume Parsing and Matching System (ATS-like)

An end-to-end Resume Parsing and Job Description (JD) Matching system built using Python, NLP, and FastAPI.  
The system extracts resume content, matches it against job requirements, computes explainable scores, and shortlists candidates while following privacy-first design principles.



# Key Features

- Resume ingestion using PDF text extraction with OCR fallback
- Text cleaning and normalization
- Skill-based matching using employer-provided skills
- Semantic similarity using TF-IDF
- Explainable scoring (skill score + semantic score)
- Automatic shortlisting logic
- Privacy-first design (only shortlisted resumes are stored)
- REST API built with FastAPI
- Modular, production-ready `src` project structure



# Project Architecture
```t
resume_parser/
|
|-- src/
|    |-- api/                # FastAPI routes and schemas
|    |-- ingestion/          # PDF and OCR ingestion (DOC/DOCX planned)
|    |-- preprocessing/      # Text cleaning and normalization
|    |-- matching/           # Skill matching, scoring, shortlisting
│    |-- utils/              # Configuration, constants, paths
│    |-- main.py             # Local pipeline testing
│
|-- data/
│    |-- shortlisted/        # Stored only for shortlisted candidates
│    |     |-- resumes/
│    |     |-- metadata/
|    |
│    |-- sample_resumes/     # Sample resumes for local testing only
│    |-- sample_jd/          # Sample job descriptions for local testing only
│
|-- uploads/                 # Temporary uploaded files 
|
|-- requirements.txt
|-- README.md

```

##  Environment Setup (Conda)

```bash
conda env create -f environment.yml
conda activate resume_parser
 
or
 
pip install -r requirements.txt
```

# End-to-End Flow

1. Resume is uploaded via API
2. Text is extracted from PDF (OCR fallback if required)
3. Resume and JD text are cleaned and normalized
4. Employer provides required skills (comma-separated)
5. Skill matching is performed
6. Semantic similarity between resume and JD is computed
7. Final score is calculated
8. Decision is made:
   - Rejected resumes are discarded
   - Shortlisted resumes and metadata are stored


# Scoring Logic

Final score is computed as:

`Final Score = (Skill Match Score × 0.6) + (Semantic Similarity × 0.4)`

- Skill Match Score: proportion of required skills found in the resume
- Semantic Similarity: TF-IDF cosine similarity between resume and JD

Weights are configurable via configuration files.



# Privacy and Compliance Design

- Rejected resumes are never stored
- Only shortlisted resumes are persisted
- `No` raw extracted resume text is saved
- Stored data includes only:
  - Resume file
  - Structured JSON metadata (scores, skills, decision)

This design aligns with privacy-first and ATS compliance practices.



# Local Pipeline Testing

Run the pipeline without the API:

```bash
python src/main.py
```
You will be prompted to enter required skills, `for example: python, ml, nlp, pandas`


# API Usage (FastAPI)
Start the API
```bash
python -m uvicorn api.app:app --app-dir src --port 8001
```

# Swagger Documentation

Open in browser:  http://127.0.0.1:8001/docs

# POST /`match` Endpoint Inputs

`resume`: PDF file
`jd_text`: Job description text
`skills`: Comma-separated skill list


# Example API Response
{
  "required_skills": ["python", "pandas"],
  
  "matched_skills": ["python"],
  
  "skill_score": 0.5,
  
  "semantic_score": 0.72,
  
  "final_score": 0.61,
  
  "decision": "shortlisted"
}


# Technology Stack
- Python
  
- FastAPI

- scikit-learn

- pdfplumber

- Tesseract OCR

- OpenCV

- TF-IDF (NLP)


# Future Enhancements
- DOC and DOCX resume ingestion
- LLM-based skill extraction (LLaMA, GPT, etc.)
- Skill ontology integration
- Configurable scoring through UI
- Cloud deployment with Docker
- Dashboard and analytics




# Project Status

- `Core pipeline:` Completed
- `API:` Completed
- `Shortlisting logic:` Completed
- `DOC/DOCX ingestion:` Planned
- `LLM-based skill extraction:` Future scope
- `Deployment:` Planned

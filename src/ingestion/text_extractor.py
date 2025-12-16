from src.ingestion.pdf_reader import extract_text_from_pdf
from src.ingestion.ocr_reader import extract_text_with_ocr

MIN_CHAR_THRESHOLD = 200

def extract_resume_text(pdf_path: str):
    """
    Decide whether to use PDF text or OCR
    """
    pdf_text = extract_text_from_pdf(pdf_path)

    if not pdf_text or len(pdf_text) < MIN_CHAR_THRESHOLD:
        print("[INFO] PDF text insufficient → switching to OCR")
        ocr_text = extract_text_with_ocr(pdf_path)
        return ocr_text, "ocr"

    return pdf_text, "pdf"

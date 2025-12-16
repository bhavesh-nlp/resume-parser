import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

from pdf2image import convert_from_path
import cv2
import numpy as np

def extract_text_with_ocr(pdf_path: str) -> str:
    """
    Extract text from scanned PDFs using OCR
    """
    text = ""

    try:
        images = convert_from_path(pdf_path)

        for img in images:
            img_np = np.array(img)
            gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
            thresh = cv2.threshold(
                gray, 150, 255, cv2.THRESH_BINARY
            )[1]

            page_text = pytesseract.image_to_string(thresh)
            text += page_text + "\n"

    except Exception as e:
        print(f"[OCR ERROR] {e}")

    return text.strip()

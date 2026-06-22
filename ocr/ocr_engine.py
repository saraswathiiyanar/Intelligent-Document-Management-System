from PIL import Image
import pytesseract

def extract_text(image_path):
    """
    OCR: Extract text from image file
    """
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return f"Error in OCR processing: {str(e)}"
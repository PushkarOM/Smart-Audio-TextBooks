import pytesseract  # For character Recognition
from PIL import Image # For handelling images
import io
from pdf2image import convert_from_path 
import tempfile


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def extract_text_from_image(image_file):
    # Write the uploaded file to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(image_file.read())
        tmp_path = tmp.name

    # If the file is an image
    image = Image.open(tmp_path)
    text = pytesseract.image_to_string(image)
    return text


def extract_text_from_pdf(pdf_file):
    text = ""
    # Write the uploaded file to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(pdf_file.read())
        tmp_path = tmp.name

    # Now convert that PDF path to images
    images = convert_from_path(tmp_path)
    for image in images:
        text += pytesseract.image_to_string(image)
    return text
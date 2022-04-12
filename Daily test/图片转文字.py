import pytesseract
from PIL import Image
def OCR(path):
    pic_to_text = pytesseract.image_to_string(Image.open(path), lang='chi_sim')
    return pic_to_text
path = r"C:/Users/57060/Desktop/111.jpg"

print(OCR(path))
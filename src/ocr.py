
import pytesseract

class ocr:
    def toNumber(self, img):
        number = pytesseract.image_to_string(img)
        return number
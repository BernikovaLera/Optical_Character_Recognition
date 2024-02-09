from PIL import Image
import pytesseract
import cv2

# Путь к нашему установленному Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Programs\Tesseract-OCR\tesseract.exe'

# Открываем изображение
image_path = 'image_name.jpg'
image = cv2.imread(image_path)

# Преобразуем изображение в черно-белое
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Распознаем текст с изображения
text = pytesseract.image_to_string(gray_image)

# Выводим распознанный текст
print(text)

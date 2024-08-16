import cv2 as cv
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

img = cv.imread("../Images/tata-safari-range-rover-featured.jpg")

# put this inside a function

x1, y1 = (219, 428)
x2, y2 = (438, 470)

# Crop the region of interest (ROI)
roi = img[y1:y2, x1:x2]

print(roi)
cv.imshow("roi", roi)
gray_roi = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)

text = pytesseract.image_to_string(gray_roi)

print(text)
cv.waitKey(0)
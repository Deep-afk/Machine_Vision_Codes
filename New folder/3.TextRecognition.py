# text recognition
import cv2
import pytesseract
# read image
pytesseract.pytesseract.tesseract_cmd = r'D:/tess/tesseract.exe'
im = cv2.imread('text.jpg')
cv2.imshow('hello', im)
# configurations
config = ('-l eng --oem 1 --psm 3')
# pytesseract
text = pytesseract.image_to_string(im, config=config)
# print text
text = text.split('\n')
print("The detected and recognized text is -> {}".format(text))

cv2.waitKey(0)
cv2.destroyAllWindows()

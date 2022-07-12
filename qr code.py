import pyqrcode
import cv2
import png
s="www.google.org"
url=pyqrcode.create(s)
url.png('qrcode.png', scale=6)
img=cv2.imread("qrcode.png")
detect=cv2.QRCodeDetector()
val,pts,st_code=detect.detectAndDecode(img)
print(val)
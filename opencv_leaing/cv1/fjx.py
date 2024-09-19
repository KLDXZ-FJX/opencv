import cv2
logo = cv2.imread('3-1.jpg')
# print(logo[198, 168])
# [ 210 148 188]
blue=logo[190,168,0]
green=logo[190,168,1]
red=logo[190,168,2]
print(blue,green,red)
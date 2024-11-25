import numpy 
import cv2

cap = cv2.VideoCapture(f'C:\\Users\\hossein\\OneDrive\\Desktop\\vison\\park_palce_car\\video.mp4')
ret , frame = cap.read()
cv2.imwrite('vids_car_park.png',frame)
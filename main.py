import cv2 
import numpy as np 
import pickle

cap = cv2.VideoCapture(r'C:\\Users\\hossein\\OneDrive\\Desktop\\vison\\park_palce_car\\video.mp4')

with open(r'C:\\Users\\hossein\\OneDrive\\Desktop\\vison\\park_palce_car\\CarParkPos','rb') as f:
    poslist = pickle.load(f)
    
width, height = 37, 80

def puttex(img, pos, text, scla=3, thickness=3, colorT=(255,255,255), 
           colorR=(255,0,255), font=cv2.FONT_HERSHEY_PLAIN, ofset=10, border=None, colorB=(0,225,0)):
    ox, oy = int(pos[0]), int(pos[1])  
    (w, h), _ = cv2.getTextSize(str(text), font, scla, thickness)
    x1, y1, x2, y2 = ox - ofset, oy + ofset, ox + w + ofset, oy - h - ofset
    cv2.rectangle(img, (x1, y1), (x2, y2), colorR, cv2.FILLED)
    if border is not None:
        cv2.rectangle(img, (x1, y1), (x2, y2), colorB, border)
    cv2.putText(img, str(text), (ox, oy), font, scla, colorT, thickness)
    return img, [x1, y2, x2, y2]


def carParkCheck(img):
    car_park_count = 0
    for pos in poslist:
        x, y = pos
        car_img = img[y:y+height, x:x+width]  
        count = cv2.countNonZero(car_img)
        if count < 110:
            car_park_count += 1
            color = (0, 255, 0)
        else:
            color = (0, 0, 255)
        cv2.rectangle(frame, pos, (pos[0]+width, pos[1]+height), color, 4)
        puttex(frame, (x, y+height-3), str(count), scla=1, thickness=2, ofset=0, colorR=color)

    puttex(frame, (100, 50), f'Free: {car_park_count}/{len(poslist)}', scla=3, thickness=3, ofset=20, colorR=(0,200,0))


while True:
    ret, frame = cap.read()
    if not ret:
        break
    imggray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    imageblur = cv2.GaussianBlur(imggray, (3,3), 1)
    imageThereshHold = cv2.adaptiveThreshold(imageblur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    imgaeMedian = cv2.medianBlur(imageThereshHold, 5)

    carParkCheck(imgaeMedian)
    
    cv2.imshow('image', frame)
    keyexit = cv2.waitKey(5) & 0xFF
    if keyexit == 27:
        break

cap.release()
cv2.destroyAllWindows()

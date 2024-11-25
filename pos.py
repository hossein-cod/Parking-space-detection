import cv2 
import pickle
import numpy
width , height = 37,80

try: 
    with open('CarParkPos','rb') as f:
        poslist = pickle.load(f)
except:
    poslist=[]
    
def mouseClick(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        poslist.append((x,y))
    if event == cv2.EVENT_RBUTTONDOWN:
        for i , pos in enumerate(poslist):
            x1,y1 = pos
            if x1 < x <x1 + width and y1 < y <y1 + height:
                poslist.pop(i)
    with open('CarParkPos','wb') as f:
        pickle.dump(poslist,f)

while True:
        img = cv2.imread(f'C:\\Users\\hossein\\OneDrive\\Desktop\\vison\\park_palce_car\\vids_car_park.png')
        for pos in poslist:
            cv2.rectangle(img , pos ,(pos[0]+width,pos[1]+height),(255,0,255),2)
        
        cv2.imshow('image',img)
        cv2.setMouseCallback('image',mouseClick)            
        keyexit = cv2.waitKey(5) & 0xFF
        if keyexit == 27:
            break

cv2.destroyAllWindows()
        
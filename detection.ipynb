import cv2 as cv
import numpy as np

image = cv.imread(r"yellow_detect.jpeg")
image_copy = image.copy()
hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
blur = cv.medianBlur(hsv,9)

lower_yellow = np.array([22, 93, 0], dtype = "uint8") 
upper_yellow= np.array([45, 255, 255], dtype = "uint8")
mask = cv.inRange(blur, lower_yellow, upper_yellow)
detected_output = cv.bitwise_and(blur, blur, mask =  mask)

kernel = np.ones((5,5),np.uint8)
out = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
b_filtered = cv.bilateralFilter(out,9,75,75)

ret,thresh = cv.threshold(mask,1,255,0)
contours, hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

for c in contours:
    x,y,w,h = cv.boundingRect(c)
    img = cv.rectangle(image_copy, (x,y), (x+w,y+h), (255, 255, 255), 2)
    rect = cv.minAreaRect(c)
    box = cv.boxPoints(rect)
    box = np.int0(box)

    M = cv.moments(box)

    img1 = cv.drawContours(image,[box],0,(255,255,255),2)

    if M['m00'] != 0:
        c_x = int(M['m10']/M['m00'])
        c_y = int(M['m01']/M['m00'])
        c#v.circle(image, (c_x, c_y), 3, (0, 0, 255), -1)
        #cv.putText(image, "centeroid", (c_x - 20, c_y - 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    print(f"{c_x} {c_y}")

    #cv.imshow("Bounding Rectangles", img1)
    #cv.waitKey(0)
    #cv.destroyAllWindows()

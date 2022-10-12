from turtle import shape
import cv2 as cv
import numpy as np


blank = np.zeros((500, 500,3), dtype="uint8")
cv.imshow("Blank", blank)

blank[200:300, 300:400] = 0, 255, 0
cv.imshow("green", blank)

# draw rectangle
cv.rectangle(blank, (100,100), (200,300), (0,255,0), thickness=2)
cv.imshow("rectangle", blank) 

# draw circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40,(0,0,255), thickness=3)
cv.imshow("circle", blank)

# write text
cv.putText(blank, "Hello world", (255, 255), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0),2)
cv.imshow("my text", blank)






cv.waitKey(0)










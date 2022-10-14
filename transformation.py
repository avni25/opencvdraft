import cv2 as cv
import numpy as np


img = cv.imread("photos/cat.jpg")
cv.imshow("cat", img)

# Transaltion
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


""" 
-x --> left
-y --> up
 x --> right
 y --> down

"""
tr = translate(img, 300, 100)
cv.imshow("trasnlated", tr)


# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, 45)
cv.imshow("rotated img", rotated)


# resize

resized = cv.resize(img, (200,200), interpolation=cv.INTER_CUBIC)
cv.imshow("resized", resized)

# flipping
flipped = cv.flip(img, 0)  # for vertical flip =0, for horizontal flip = 1
cv.imshow("flipped", flipped)

# cropping
cropped = img[200:400, 200:400]
cv.imshow("cropped", cropped)








cv.waitKey(0)
import cv2 as cv


img = cv.imread("photos/cat.jpg")

cv.imshow("dog", img)

# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray dog", gray)


# blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow("blurred cat", blur)

# edge cascade
canny = cv.Canny(img, 125, 75)
cv.imshow("canny cat", canny)

canny2 = cv.Canny(blur, 125, 75)
cv.imshow("canny cat2", canny2)


# dilating the image
dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow("dilated", dilated)

# resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow("resized img", resized)

# cropping
cropped = img[50:200, 200:500]
cv.imshow("cropped img", cropped)






cv.waitKey(0)

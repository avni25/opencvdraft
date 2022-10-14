import cv2 as cv



img = cv.imread("photos/dog.jpg")
cv.imshow("dog", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("grayscale", gray)


blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow("blurred", blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow("canny", canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} counters found!')



cv.waitKey(0)

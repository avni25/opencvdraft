import cv2 as cv

# reading and displaying images 
def display_img(path, win_name):
    img = cv.imread(path)
    resized_img = rescaleFrame(img, 0.7)
    cv.imshow(win_name, resized_img)
    cv.waitKey(0)


# reading videos and displaying
def display_video(path, win_name):
    capture = cv.VideoCapture(path)
    while True:
        isTrue, frame = capture.read()
        frame_resized = rescaleFrame(frame, 0.5)
        # cv.imshow(win_name, frame)
        cv.imshow(win_name, frame_resized)

        if cv.waitKey(20) & 0xFF==ord('d'):
            break

    capture.release()
    cv.destroyAllWindows()

# sets the scales of image/video
def rescaleFrame(frame, scale=1.0):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)




display_video("videos/taylan1.mp4", "qweqwe")
display_img("photos/cat.jpg", "Mycat")











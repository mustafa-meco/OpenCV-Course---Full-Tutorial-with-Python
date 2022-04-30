import cv2 as cv


img = cv.imread('Resources/Photos/cat .jpg')
cv.imshow("Cat", img)

def rescaleframe(frame, scale=0.75):
    # Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleframe(img)
cv.imshow("Image", resized_image)

cv.waitKey(0)

def changeRes(width,height):
    # Live Video
    capture.set(3,width)
    capture.set(4,height)
# Reading Videos
capture = cv.VideoCapture('./Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleframe(frame,.2)

    cv.imshow('Video', frame)
    cv.imshow("Video Resized", frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()



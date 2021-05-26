import cv2

videoCaptureObject = cv2.VideoCapture(1)


#videoCaptureObject.set(3, 1920.)
#videoCaptureObject.set(4, 1080.)

videoCaptureObject.set(3, 5268.)
videoCaptureObject.set(4, 2907.)
result = True
while(result):
    ret,frame = videoCaptureObject.read()
    cv2.imwrite("c920_9.jpg",frame)
    result = False
videoCaptureObject.release()
cv2.destroyAllWindows()
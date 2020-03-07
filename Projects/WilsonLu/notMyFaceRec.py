import cv2 as cv
eye_cascade = cv.CascadeClassifier('Send-Archive/haarcascade_eye_tree_eyeglasses.xml')
face_cascade= cv.CascadeClassifier('Send-Archive/haarcascade_frontalface_alt.xml')
video_capture = cv.VideoCapture(0)
def detectFacesandEyes(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
    print("Eyes found: ", len(eyes))

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print("Faces found: ", len(faces))
    for (x,y,w,h) in eyes:
        cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    for(x,y,w,h) in faces:
        cv.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 2)

#ret,img = video_capture.read()
#cv.imshow('image',img)

img = cv.imread("spooder.jpg")
img2 = cv.imread("colonelSanders.jpg")
img3 = cv.imread("supremeLeader.jpg")
detectFacesandEyes(img)
cv.imshow("spooder", img)
cv.waitKey(0)
cv.destroyAllWindows()
detectFacesandEyes(img2)
cv.imshow("colonel", img2)
cv.waitKey(0)
cv.destroyAllWindows()
detectFacesandEyes(img3)
cv.imshow("supremeLeader", img3)
cv.waitKey(0)
cv.destroyAllWindows()

#video_capture.release()

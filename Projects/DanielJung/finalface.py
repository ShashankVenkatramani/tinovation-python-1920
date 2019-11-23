import cv2 as cv
eye_cascade = cv.CascadeClassifier(r'C:\Users\thecu\Documents\Python\haarcascade_eye_tree_eyeglasses.xml')
face_cascade= cv.CascadeClassifier(r'C:\Users\thecu\Documents\Python\haarcascade_frontalface_alt_tree.xml')
video_capture = cv.VideoCapture(0)
def Video(video_capture):
    while(True):
        ret, frame = video_capture.read()
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame', gray)
        if cv.waitKey(1) & 0xff == ord('q'):
            break

    video_capture.release()
    cv.destroyAllWindows()

def detectFacesandEyes(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
    #print(len(eyes))

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print(len(faces))
    for (x,y,w,h) in eyes:
        cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    for(x,y,w,h) in faces:
       cv.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 2)

#ret, img = video_capture.read()
#cv.imshow('image',img)
path = 'face.jpeg'
img = cv.imread(path, 1)
detectFacesandEyes(img)
cv.imshow("new", img)
cv.waitKey(0)
cv.destroyAllWindows()
#video_capture.release()

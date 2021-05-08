import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_glasses = cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
frontFaceAlt = cv2.CascadeClassifier("haarcascade_frontalface_alt2")
eyeball = cv2.CascadeClassifier("haarcascade_eye.xml")
fullBody = cv2.CascadeClassifier("haarcascade_fullbody.xml"
lowerBody = cv2.CascadeClassifier("haarcascade_lowerbody.xml")
upperBody = cv2.CascadeClassifier("haarcascade_upperbody.xml")


cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        exit(1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    eye_glasses_people = eye_glasses.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    altFace = frontFaceAlt.detectMultiScale(gray, 1.5, 5)
    eyeBallFind = eyeball.detectMultiScale(gray, 1.5, 5)
    fullBodyGet = fullBody.detectMultiScale(gray, 1.5, 2)
    lowerBodyGet = lowerBody.detectMultiScale(gray, 1.5, 2)
    uppperBodyGet = upperBody.detectMultiScale(gray, 1.5, 2)


    for (x, y, w, h) in face:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    for (x, y, w, h) in eye_glasses_people:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 4, 2), 3)

    for (x, y, w, h) in altFace:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 2), 3)

    for (x, y, w, h) in eyeBallFind:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 2), 3

    for (x, y, w, h) in fullBodyGet:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 2), 3)

    for (x, y, w, h) in lowerBodyGet:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 2), 3)

    for (x, y, w, h) in uppperBodyGet:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 2), 3)


    cv2.imshow('Detected', frame)

    if cv2.waitKey(20) & 0xFF == ord(' '):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

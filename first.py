import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_glasses = cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")


cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        exit(1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    eye_glasses_people = eye_glasses.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    for (x, y, w, h) in face:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    for (x, y, w, h) in eye_glasses_people:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 4, 2), 3)

    cv2.imshow('Detected', frame)

    if cv2.waitKey(20) & 0xFF == ord(' '):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

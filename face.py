# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import numpy as np
import cv2
import face_recognition
import dlib

def get_encodings() -> list:
    imgTrain = face_recognition.load_image_file("C:\\Users\\vijay\\PycharmProjects\\pythonProject\\train\\Frost.jpeg")
    imgTrain2 = face_recognition.load_image_file("C:\\Users\\vijay\\PycharmProjects\\pythonProject\\train\\Frost2.jpg")
    imgTrain = cv2.cvtColor(imgTrain, cv2.COLOR_BGR2RGB)
    imgTrain2 = cv2.cvtColor(imgTrain2, cv2.COLOR_BGR2RGB)

    master_encode = []
    master_encode.append(face_recognition.face_encodings(imgTrain)[0])
    master_encode.append(face_recognition.face_encodings(imgTrain2)[0])

    return master_encode


def main() -> int:

    cap = cv2.VideoCapture(0)
    database = get_encodings()

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            exit(1)

        usable_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faceLocations = face_recognition.face_locations(img=usable_frame, model="cnn")

        for a in faceLocations:
            if any(face_recognition.compare_faces(database, a)):
                frame = cv2.rectangle(frame, (a[3], a[0]), (a[1], a[2]), (0, 255, 0), 2)
            else:
                frame = cv2.rectangle(frame, (a[3], a[0]), (a[1], a[2]), (255, 0, 0), 2)

        cv2.imshow('Detected', frame)

        if cv2.waitKey(0.1) & 0xFF == ord(' '):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    return 0


if __name__ == "__main__":
    while True:
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cv2.imshow("Test", frame)
    #print("Started")
    #print("Exited with code " + str(main()))

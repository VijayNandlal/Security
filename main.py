from __future__ import annotations
import numpy as np
import cv2
import face_recognition
import dlib
from cv2 import VideoCapture
import threading


def get_encodings() -> list:
    imgTrain = face_recognition.load_image_file('/home/vijay/Documents/orange/training/Frost.jpeg')
    imgTrain2 = face_recognition.load_image_file('/home/vijay/Documents/orange/training/Frost2.jpeg')
    img3 = face_recognition.load_image_file('/home/vijay/Documents/orange/training/Barry_Allen.jpg')
    img4 = face_recognition.load_image_file('/home/vijay/Documents/orange/training/Barry_Allen2.jpg')
    img5 = face_recognition.load_image_file('/home/vijay/Documents/orange/training/Barry_Allen.jpg')

    master_encode = []
    cv2.cvtColor(imgTrain, cv2.COLOR_BGR2RGB)
    cv2.cvtColor(imgTrain2, cv2.COLOR_BGR2RGB)
    cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
    cv2.cvtColor(img4, cv2.COLOR_BGR2RGB)
    cv2.cvtColor(img5, cv2.COLOR_BGR2RGB)

    master_encode = [face_recognition.face_encodings(imgTrain)[0], face_recognition.face_encodings(imgTrain2)[0], face_recognition.face_encodings(img3)[0], face_recognition.face_encodings(img4)[0], face_recognition.face_encodings(img5)[0]]

    return master_encode

def frame_capture(framebuf: list, cap: VideoCapture) -> None:
    print("Capturing Camera\n")
    while True:
        ret, frame = cap.read()

        if not ret:
            exit(1)
        cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        framebuf.append(frame)

# def image_show(frames: list) -> None:
#     print("Launching Window\n")
#     while True:
#         try:
#             frame = frames.pop(-1)
#             frames.clear()
#             cv2.imshow("Detected", frame)
#         finally:
#             continue

def main() -> int:

    cap = cv2.VideoCapture(0)
    database = get_encodings()
    framebuf = []
    frameshow = []

    frames_handle = threading.Thread(target=frame_capture, args=[framebuf, cap])
    frames_handle.start()

    # image_handle = threading.Thread(target=image_show, args=[frameshow])
    # image_handle.start()

    while True:
        try:
            frame = framebuf.pop(-1)
            framebuf.clear()

            faceLocations = face_recognition.face_locations(img=frame, model="hog")
            faceComps = face_recognition.face_encodings(frame, faceLocations)

            cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            for a in range(len(faceLocations)):
                if any(face_recognition.compare_faces(database, faceComps[a])):
                    frame = cv2.rectangle(frame, (faceLocations[a][3], faceLocations[a][0]), (faceLocations[a][1], faceLocations[a][2]), (0, 255, 0), 2)
                else:
                    frame = cv2.rectangle(frame, (faceLocations[a][3], faceLocations[a][0]), (faceLocations[a][1], faceLocations[a][2]), (255, 255 ,255), 2)

            #frameshow.append(frame)
            cv2.imshow("Detected", frame)

            if cv2.waitKey(1) & 0xFF == ord(' '):
                cap.release()
                cv2.destroyAllWindows()
                frames_handle.join()
                exit(0)

        finally:
            continue

    # When everything done, release the capture

    return 0


if __name__ == "__main__":

    print("Started")
    print("Exited with code " + str(main()))

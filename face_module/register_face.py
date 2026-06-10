from database.db_operations import (
    save_user,
    username_exists
)

from face_module.face_utils import (
    encoding_to_string
)

import cv2
import face_recognition


def register_face(username):

    if username_exists(username):

        print("Username already exists.")

        return False

    camera = cv2.VideoCapture(0)

    while True:

        success, frame = camera.read()

        if not success:
            break

        cv2.imshow("Face Registration", frame)

        key = cv2.waitKey(1)

        if key == ord("c"):

            small_frame = cv2.resize(
                frame,
                (0, 0),
                fx=0.25,
                fy=0.25
            )

            rgb_small_frame = cv2.cvtColor(
                small_frame,
                cv2.COLOR_BGR2RGB
            )

            face_locations = face_recognition.face_locations(
                rgb_small_frame
            )

            if len(face_locations) == 0:
                print("No face detected.")
                continue

            face_encodings = face_recognition.face_encodings(
                rgb_small_frame,
                face_locations
            )

            encoding = face_encodings[0]

            encoding_string = encoding_to_string(
                encoding
            )

            save_user(
                username,
                encoding_string
            )

            camera.release()
            cv2.destroyAllWindows()

            return True

        elif key == ord("q"):

            camera.release()
            cv2.destroyAllWindows()

            return False
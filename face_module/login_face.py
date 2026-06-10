from database.db_operations import get_all_users
from face_module.face_utils import (
    compare_faces,
    string_to_encoding
)

import cv2
import face_recognition


def authenticate_face():

    camera = cv2.VideoCapture(0)

    while True:

        success, frame = camera.read()

        if not success:
            break

        cv2.imshow("Face Login", frame)

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

            login_encoding = face_encodings[0]

            users = get_all_users()

            for username, stored_encoding in users:

                stored_encoding = string_to_encoding(
                    stored_encoding
                )

                if compare_faces(
                    stored_encoding,
                    login_encoding
                ):

                    camera.release()
                    cv2.destroyAllWindows()

                    return username

            camera.release()
            cv2.destroyAllWindows()

            return None

        elif key == ord("q"):

            camera.release()
            cv2.destroyAllWindows()

            return None
        
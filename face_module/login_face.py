from database.db_operations import get_all_users
from face_module.face_utils import (
    compare_faces,
    string_to_encoding
)

import cv2
import face_recognition

camera = cv2.VideoCapture(0)

while True:

    success, frame = camera.read()

    if not success:
        break

    cv2.imshow("Face Login", frame)

    key = cv2.waitKey(1)

    if key == ord("c"):

        face_locations = face_recognition.face_locations(frame)

        if len(face_locations) == 0:
            print("No face detected.")
            continue

        face_encodings = face_recognition.face_encodings(
            frame,
            face_locations
        )

        login_encoding = face_encodings[0]

        users = get_all_users()

        match_found = False

        for username, stored_encoding in users:

            stored_encoding = string_to_encoding(
                stored_encoding
            )

            if compare_faces(
                stored_encoding,
                login_encoding
            ):

                print(
                    f"Login successful. Welcome {username}"
                )

                match_found = True
                break

        if not match_found:
            print("Face not recognized.")

        break

    elif key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
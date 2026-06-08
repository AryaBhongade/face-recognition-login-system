import cv2
import face_recognition

camera = cv2.VideoCapture(0)

while True:
    success, frame = camera.read()

    if not success:
        break

    cv2.imshow("Face Registration", frame)

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

        encoding = face_encodings[0]

        print("Face encoding generated successfully.")
        print(f"Encoding length: {len(encoding)}")

        break

    elif key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
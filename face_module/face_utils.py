import face_recognition
import json


def get_face_locations(image):
    return face_recognition.face_locations(image)


def get_face_encodings(image):
    return face_recognition.face_encodings(image)


def compare_faces(known_encoding, unknown_encoding):
    return face_recognition.compare_faces(
        [known_encoding],
        unknown_encoding
    )[0]


def encoding_to_string(encoding):
    return json.dumps(encoding.tolist())


def string_to_encoding(text):
    return json.loads(text)
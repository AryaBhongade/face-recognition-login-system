import face_recognition


def get_face_locations(image):
    return face_recognition.face_locations(image)


def get_face_encodings(image):
    return face_recognition.face_encodings(image)


def compare_faces(known_encoding, unknown_encoding):
    return face_recognition.compare_faces(
        [known_encoding],
        unknown_encoding
    )[0]
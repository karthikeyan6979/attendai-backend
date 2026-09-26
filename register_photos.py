import face_recognition
import numpy as np
from face_engine.database import Database

def register_from_photos(name, roll_number, image_paths):
    encodings = []
    for path in image_paths:
        image = face_recognition.load_image_file(path)
        face_locations = face_recognition.face_locations(image, model='hog')
        if len(face_locations) != 1:
            print(f"  Skipped {path}: found {len(face_locations)} faces, need exactly 1")
            continue
        encoding = face_recognition.face_encodings(image, face_locations)[0]
        encodings.append(encoding)

    if len(encodings) < 1:
        print(f"  Failed: no valid photos for {name}")
        return False

    averaged = np.mean(encodings, axis=0)
    db = Database()
    success = db.add_student(name, roll_number, averaged)
    db.close()
    print(f"  Registered {name} using {len(encodings)} photo(s)")
    return success

register_from_photos("Daksh",    "A001", ["photos/daksh1.jpeg"])
register_from_photos("Varun",    "A002", ["photos/varun1.jpeg", "photos/varun2.jpeg"])
register_from_photos("Ritik",    "A003", ["photos/ritik1.jpeg"])
register_from_photos("Akshat",   "A004", ["photos/akshat1.jpeg"])
register_from_photos("Shourya",  "A005", ["photos/shourya1.jpeg"])
register_from_photos("Kamalesh", "A006", ["photos/kamalesh1.jpeg"])
register_from_photos("Rohan",    "A007", ["photos/rohan2.jpeg"])
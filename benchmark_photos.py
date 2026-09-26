from face_engine.recognize import FaceRecognizer
import face_recognition

test_photos = {
    "Daksh":   "photos/daksh2.jpeg",
    "Varun":   "photos/varun3.jpeg",
    "Ritik":   "photos/ritik2.jpeg",
    "Akshat":  "photos/akshat2.jpeg",
    "Shourya": "photos/shourya2.jpeg",
    "Rohan":   "photos/rohan1.jpeg",
}

recognizer = FaceRecognizer(tolerance=0.5)

correct = 0
total = 0
for expected_name, path in test_photos.items():
    image = face_recognition.load_image_file(path)
    results = recognizer.recognize_faces(image)
    got = results[0][0] if results else "no_face_detected"
    total += 1
    match = expected_name.lower() in got.lower()
    if match:
        correct += 1
    print(f"expected={expected_name:10s} got={got:30s} {'✓' if match else '✗'}")

print(f"\nAccuracy: {correct}/{total} = {correct/total*100:.1f}%")
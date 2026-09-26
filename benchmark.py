import time
from face_engine.camera import Camera
from face_engine.recognize import FaceRecognizer
import face_recognition

frame = face_recognition.load_image_file(f"test_photos/{expected}.jpg")
recognizer = FaceRecognizer(tolerance=0.5)
camera = Camera(camera_index=0, scale_factor=0.25)
camera.start()

latencies = []
results = []  # (expected_name, got_name)

num_trials = 30
print(f"Running {num_trials} recognition trials. Press Enter before each capture.")

for i in range(num_trials):
    expected = input(f"[{i+1}/{num_trials}] Who's in front of the camera right now? (name or 'unknown'): ")

    frame = camera.capture_single_frame()
    if frame is None:
        print("  capture failed, skipping")
        continue

    start = time.time()
    recognized = recognizer.recognize_faces(frame)
    elapsed = time.time() - start
    latencies.append(elapsed)

    got = recognized[0][0] if recognized else "no_face_detected"
    results.append((expected, got))
    print(f"  got: {got}  |  took {elapsed*1000:.1f} ms")

camera.stop()
recognizer.stop()

# --- Metrics ---
avg_latency = sum(latencies) / len(latencies)
print(f"\nAverage latency: {avg_latency*1000:.1f} ms over {len(latencies)} trials")

valid_results = [(e, g) for e, g in results if e.strip()]  # drop blank entries
correct = 0
for expected, got in valid_results:
    if expected.strip().lower() in got.lower():
        correct += 1
accuracy = correct / len(valid_results) * 100 if valid_results else 0
print(f"Accuracy: {accuracy:.1f}% ({correct}/{len(valid_results)}) — {len(results) - len(valid_results)} blank inputs discarded")
accuracy = correct / len(results) * 100
print(f"Accuracy: {accuracy:.1f}% ({correct}/{len(results)})")

for expected, got in results:
    print(f"  expected={expected:15s} got={got}")
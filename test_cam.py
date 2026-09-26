import cv2
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
print("Camera opened:", cap.isOpened())
print("Frame captured:", ret)
if ret:
    cv2.imwrite("test_capture.jpg", frame)
    print("Saved test_capture.jpg - check it")
cap.release()
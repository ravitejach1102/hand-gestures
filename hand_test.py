import cv2
from cvzone.HandTrackingModule import HandDetector

# Initialize camera
cap = cv2.VideoCapture(0)

# Initialize hand detector
detector = HandDetector(detectionCon=0.7, maxHands=1)

print("Show your hand to the camera...")

while True:
    success, img = cap.read()
    if not success:
        break

    # Detect hands
    hands, img = detector.findHands(img)

    if hands:
        print("Hand detected")

    cv2.imshow("Hand Detection (cvzone)", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
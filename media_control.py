import cv2
import time
import pyautogui
from cvzone.HandTrackingModule import HandDetector

# Initialize camera
cap = cv2.VideoCapture(0)

# Initialize hand detector
detector = HandDetector(detectionCon=0.7, maxHands=1)

# Delay to avoid continuous toggling
last_action_time = 0
action_delay = 2  # seconds

print("Show hand to Play/Pause media")

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)

    hands, img = detector.findHands(img)

    current_time = time.time()

    if hands:
        if current_time - last_action_time > action_delay:
            print("Play / Pause triggered")
            pyautogui.press('space')  # Play / Pause
            last_action_time = current_time

    cv2.imshow("Touchless Media Control", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
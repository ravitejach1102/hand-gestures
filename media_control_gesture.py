import cv2
import time
import pyautogui
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.7, maxHands=1)

last_action_time = 0
action_delay = 2  # seconds

print("✋ Open Palm = PLAY | ✊ Fist = PAUSE")

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)

    current_time = time.time()

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        finger_count = fingers.count(1)

        # OPEN PALM (5 fingers)
        if finger_count == 5 and current_time - last_action_time > action_delay:
            print("PLAY")
            pyautogui.press('space')
            last_action_time = current_time

        # FIST (0 fingers)
        elif finger_count == 0 and current_time - last_action_time > action_delay:
            print("PAUSE")
            pyautogui.press('space')
            last_action_time = current_time

    cv2.imshow("Gesture Media Control", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
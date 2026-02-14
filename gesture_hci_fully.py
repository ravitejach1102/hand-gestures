import cv2
import time
import pyautogui
from cvzone.HandTrackingModule import HandDetector
import math

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.7, maxHands=1)

last_action_time = 0
action_delay = 1.5

media_state = "PAUSED"

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

        lmList = hand["lmList"]

        
        thumb_tip = lmList[4]
        index_tip = lmList[8]

        
        distance = math.hypot(
            index_tip[0] - thumb_tip[0],
            index_tip[1] - thumb_tip[1]
        )

        if current_time - last_action_time > action_delay:

           
            if finger_count == 5 and media_state == "PAUSED":
                pyautogui.press("playpause")
                print("PLAY")
                media_state = "PLAYING"
                last_action_time = current_time

            
            elif finger_count == 0 and media_state == "PLAYING":
                pyautogui.press("playpause")
                print("PAUSE")
                media_state = "PAUSED"
                last_action_time = current_time

            
            elif fingers == [1, 0, 0, 0, 0]:
                pyautogui.press("volumeup")
                print("VOLUME UP")
                last_action_time = current_time

            
            elif fingers == [0, 0, 0, 0, 1]:
                pyautogui.press("volumedown")
                print("VOLUME DOWN")
                last_action_time = current_time

            
            elif finger_count == 2:
                pyautogui.scroll(300)
                print("SCROLL UP")
                last_action_time = current_time

            elif finger_count == 3:
                pyautogui.scroll(-300)
                print("SCROLL DOWN")
                last_action_time = current_time


            elif distance < 40:
                pyautogui.hotkey("ctrl", "+")
                print("ZOOM IN")
                last_action_time = current_time

            elif distance > 120:
                pyautogui.hotkey("ctrl", "-")
                print("ZOOM OUT")
                last_action_time = current_time

    cv2.imshow("Advanced Touchless HCI", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key, Controller

cap = cv2.VideoCapture(0)
cap.set(3, 750)
cap.set(4, 520)

detector = HandDetector(detectionCon=0.9, maxHands=1)

keyboard = Controller()
while True:
    _, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        fingers = detector.fingersUp(hands[0])
        if fingers == [0, 0, 0, 0, 0]:
            keyboard.press(Key.down)
            keyboard.release(Key.left)
            keyboard.release(Key.up)
            keyboard.release(Key.right)
        elif fingers == [1, 1, 1, 1, 1]:
            keyboard.press(Key.up)
            keyboard.release(Key.left)
            keyboard.release(Key.right)
            keyboard.release(Key.down)
        elif fingers == [0, 1, 0, 0, 0]:  # All one finger is up
            keyboard.press(Key.left)
            keyboard.release(Key.up)
            keyboard.release(Key.right)
            keyboard.release(Key.down)
        elif fingers == [0, 1, 1, 0, 0]:  # Only the two fingers are up
            keyboard.press(Key.right)
            keyboard.release(Key.left)
            keyboard.release(Key.down)
            keyboard.release(Key.up)
    else:
        keyboard.release(Key.left)
        keyboard.release(Key.right)
        keyboard.release(Key.up)
        keyboard.release(Key.down)

    cv2.imshow("Shimon Race", img)
    if cv2.waitKey(1) == ord("0"):
        break

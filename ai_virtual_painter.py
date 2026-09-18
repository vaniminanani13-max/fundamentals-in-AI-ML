import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    max_num_hands=1,
    model_complexity=0,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

canvas = np.zeros((480, 640, 3), np.uint8)

old_x = 0
old_y = 0

while True:
    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (640, 480))

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:

        hand = result.multi_hand_landmarks[0]
        points = []

        for landmark in hand.landmark:
            x = int(landmark.x * 640)
            y = int(landmark.y * 480)
            points.append((x, y))

        index_x, index_y = points[8]
        middle_x, middle_y = points[12]

        index_finger = index_y < points[6][1]
        middle_finger = middle_y < points[10][1]

        if index_finger and not middle_finger:

            cv2.circle(
                frame,
                (index_x, index_y),
                8,
                (255, 0, 255),
                -1
            )

            if old_x == 0 and old_y == 0:
                old_x = index_x
                old_y = index_y

            cv2.line(
                canvas,
                (old_x, old_y),
                (index_x, index_y),
                (255, 0, 255),
                7,
                cv2.LINE_AA
            )

            old_x = index_x
            old_y = index_y

        elif index_finger and middle_finger:

            cv2.circle(
                frame,
                (index_x, index_y),
                15,
                (0, 0, 0),
                2
            )

            cv2.circle(
                canvas,
                (index_x, index_y),
                22,
                (0, 0, 0),
                -1
            )

            old_x = 0
            old_y = 0

        else:
            old_x = 0
            old_y = 0

    else:
        old_x = 0
        old_y = 0

    gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)

    _, mask = cv2.threshold(
        gray,
        10,
        255,
        cv2.THRESH_BINARY
    )

    frame[mask == 255] = canvas[mask == 255]

    cv2.putText(
        frame,
        "Draw: One Finger | Erase: Two Fingers | C: Clear | Q: Quit",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        (0, 255, 0),
        2
    )

    cv2.imshow("Virtual Painter", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("c"):
        canvas = np.zeros((480, 640, 3), np.uint8)

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

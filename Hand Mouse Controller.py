# Hand-Controlled Mouse Movement and Click Detection
# --------------------------------------------------
# This script uses OpenCV, MediaPipe, and PyAutoGUI
# to track the user's hand via webcam and control the
# mouse cursor using index fingertip position. When the
# index and thumb tips come close together, a mouse click
# is triggered.

import cv2
import numpy as np
import mediapipe
import pyautogui

# Initialize fingertip coordinates
x1 = x2 = y1 = y2 = 0

# Initialize MediaPipe Hands solution
capture_hand = mediapipe.solutions.hands.Hands()
drawing_options = mediapipe.solutions.drawing_utils

# Start capturing video from webcam
camera = cv2.VideoCapture(0)

# Get screen size for mouse positioning
screen_width, screen_height = pyautogui.size()

while True:
    ret, image = camera.read()
    if not ret:
        break

    # Flip image horizontally for mirror view
    image = cv2.flip(image, 1)

    # Convert image to RGB (required by MediaPipe)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output_hands = capture_hand.process(rgb_image)
    all_hands = output_hands.multi_hand_landmarks
    image_height, image_width, _ = image.shape

    # Process detected hands
    if all_hands:
        for hand_landmarks in all_hands:
            # Draw hand landmarks on the image
            drawing_options.draw_landmarks(image, hand_landmarks)
            one_hand_landmarks = hand_landmarks.landmark

            for id, lm in enumerate(one_hand_landmarks):
                x = int(lm.x * image_width)
                y = int(lm.y * image_height)

                # Index fingertip (landmark ID 8)
                if id == 8:
                    mouse_x = int(screen_width / image_width * x)
                    mouse_y = int(screen_height / image_height * y)
                    cv2.circle(image, (x, y), 8, (255, 0, 0), thickness=3)
                    pyautogui.moveTo(mouse_x, mouse_y)
                    x1, y1 = x, y

                # Thumb tip (landmark ID 4)
                if id == 4:
                    cv2.circle(image, (x, y), 8, (0, 255, 0), thickness=3)
                    x2, y2 = x, y

            # Calculate distance between index and thumb tip
            distance = abs(y1 - y2)
            print("Distance between thumb and index finger:", distance)

            # Click if fingers are close together
            if distance < 70:
                pyautogui.click()

    # Show the processed video
    cv2.imshow("Hand Movement Video Capture", image)
    key = cv2.waitKey(10)
    if key == 27:  # Press ESC to exit
        break

# Cleanup
camera.release()
cv2.destroyAllWindows()

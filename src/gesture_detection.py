import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

def detect_gesture(image):
    """Detect hand gesture using MediaPipe Hands."""
    with mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7) as hands:
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)

        if not results.multi_hand_landmarks:
            return "No hand detected", None

        hand_landmarks = results.multi_hand_landmarks[0]
        h, w, _ = image.shape
        landmarks = [(int(lm.x * w), int(lm.y * h)) for lm in hand_landmarks.landmark]

        # Draw hand landmarks
        mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Finger tip and pip (base) indexes
        tips = [4, 8, 12, 16, 20]
        pips = [3, 6, 10, 14, 18]

        fingers_up = []

        # Thumb: check if thumb tip is to the right of its base
        fingers_up.append(landmarks[4][1] < landmarks[3][1])

        # Other fingers: tip is above the pip
        for tip, pip in zip(tips[1:], pips[1:]):
            fingers_up.append(landmarks[tip][1] < landmarks[pip][1])

        # Gesture detection for Rock, Paper, Scissors, Lizard, Spock
        up_count = fingers_up.count(True)

        if up_count <= 1:
            return "Rock", hand_landmarks
        elif fingers_up[1] and fingers_up[2] and not fingers_up[3] and not fingers_up[4]:
            return "Scissors", hand_landmarks
        elif up_count == 5:
            return "Paper", hand_landmarks
        elif fingers_up[3] and fingers_up[4] and not fingers_up[1] and not fingers_up[2]:
            return "Lizard", hand_landmarks
        elif fingers_up[1] and fingers_up[2] and fingers_up[3] and not fingers_up[4]:
            return "Spock", hand_landmarks
        else:
            return "Unknown", hand_landmarks

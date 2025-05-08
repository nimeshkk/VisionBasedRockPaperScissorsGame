import cv2
import time
from src.gesture_detection import detect_gesture
from src.game_logic import get_computer_choice, determine_winner
from src.utils import add_text_overlay, countdown, EMOJIS, REACTIONS

VALID_GESTURES = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

def main():
    cap = cv2.VideoCapture(0)
    last_gesture_time = 0
    gesture_cooldown = 3  # Seconds between gestures
    game_state = "detecting"
    user_choice = None
    computer_choice = None
    result = None

    print(">> Show your gesture in front of the camera. Press ESC to exit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Resize frame for display
        frame = cv2.resize(frame, (1280, 1024))

        # Live gesture detection
        gesture, landmarks = detect_gesture(frame)

        # Display gesture text
        display_text = f"Gesture: {gesture} {EMOJIS.get(gesture, '')}"
        frame = add_text_overlay(
            frame, display_text, (10, 10),
            font_size=40, text_color=(0, 255, 0), overlay_alpha=0.5
        )

        if game_state == "detecting" and gesture in VALID_GESTURES:
            current_time = time.time()
            if current_time - last_gesture_time > gesture_cooldown:
                countdown(frame)
                ret, frame = cap.read()
                if not ret:
                    print("Failed to grab frame")
                    break
                frame = cv2.resize(frame, (800, 600))
                gesture, landmarks = detect_gesture(frame)

                if gesture in VALID_GESTURES:
                    user_choice = gesture
                    computer_choice = get_computer_choice()
                    result = determine_winner(user_choice, computer_choice)
                    last_gesture_time = current_time
                    game_state = "result"
                else:
                    print(f"Ignored invalid gesture after countdown: {gesture}")

        # Display result and emojis
        if game_state == "result":
            user_emoji = EMOJIS.get(user_choice, "❓")
            comp_emoji = EMOJIS.get(computer_choice, "❓")
            reaction = REACTIONS.get(result, "")

            frame = add_text_overlay(frame, f"You: {user_choice} {user_emoji}", (10, 80), font_size=40, overlay_alpha=0.5)
            frame = add_text_overlay(frame, f"Computer: {computer_choice} {comp_emoji}", (10, 130), font_size=40, overlay_alpha=0.5)
            frame = add_text_overlay(frame, f"{result} {reaction}", (10, 180), font_size=40, text_color=(0, 255, 255), overlay_alpha=0.5)
            frame = add_text_overlay(frame, "Press SPACE to play again, ESC to quit", (10, 230), font_size=40, text_color=(255, 255, 0), overlay_alpha=0.5)

        cv2.imshow("Rock Paper Scissors Lizard Spock", frame)
        key = cv2.waitKey(1)

        if key == 27:  # ESC
            break
        elif game_state == "result":
            if key == 32:  # SPACE
                game_state = "detecting"
                user_choice = None
                computer_choice = None
                result = None

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
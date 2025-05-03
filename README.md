Rock Paper Scissors Lizard Spock
A computer vision-based game using MediaPipe to detect hand gestures for playing Rock, Paper, Scissors, Lizard, Spock.
Folder Structure
rpsls_project/
├── assets/
│   └── seguiemj.ttf  # Emoji font file
├── src/
│   ├── gesture_detection.py  # Hand gesture detection logic
│   ├── game_logic.py        # Game rules and computer choice
│   ├── utils.py            # Text overlay and countdown utilities
│   └── main.py             # Main game loop
└── README.md

Prerequisites

Python 3.8+
Install dependencies:pip install opencv-python mediapipe numpy pillow


Ensure seguiemj.ttf is in the assets/ folder (download a font that supports emojis if not available).

Running the Game

Navigate to the project directory:cd rpsls_project


Run the main script:python src/main.py


Show your hand gesture to the webcam.
Press SPACE to play again, ESC to quit.

How to Play

Show a hand gesture to the webcam.
The game detects gestures for Rock, Paper, Scissors, Lizard, or Spock.
After a 3-second countdown, the computer makes a choice, and the winner is determined.
Results are displayed with emojis and a semi-transparent text overlay.


import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Define emojis for each gesture
EMOJIS = {
    "Rock": "✊",
    "Paper": "🖐️",
    "Scissors": "✌️",
    "Lizard": "🦎",
    "Spock": "🖖",
    "Unknown": "❓",
    "No hand detected": "❌"
}

# Define reaction emojis for results
REACTIONS = {
    "You win!": "🎉",
    "Computer wins!": "😢",
    "It's a tie!": "🤝"
}

def add_text_overlay(frame, text, position, font_size=60, text_color=(255, 255, 255), overlay_color=(0, 0, 0), overlay_alpha=0.5):
    """Add text with a semi-transparent overlay to the frame."""
    # Convert OpenCV image (BGR) to PIL image (RGB)
    cv2_im_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_im = Image.fromarray(cv2_im_rgb)
    draw = ImageDraw.Draw(pil_im)

    try:
        # Use a font that supports emojis
        font = ImageFont.truetype("assets/seguiemj.ttf", font_size)
    except IOError:
        # Fallback to default font
        font = ImageFont.load_default()

    # Get text size
    text_bbox = draw.textbbox(position, text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Create overlay
    overlay = Image.new('RGBA', pil_im.size, (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    overlay_draw.rectangle(
        [text_bbox[0] - 10, text_bbox[1] - 10, text_bbox[2] + 10, text_bbox[3] + 10],
        fill=overlay_color + (int(255 * overlay_alpha),)
    )

    # Combine overlay with image
    pil_im = Image.alpha_composite(pil_im.convert('RGBA'), overlay)

    # Draw text
    draw = ImageDraw.Draw(pil_im)
    draw.text(position, text, font=font, fill=text_color)

    # Convert back to OpenCV image (BGR)
    frame = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGBA2BGR)
    return frame

def countdown(frame, duration=3):
    """Display a countdown on the frame."""
    for i in range(duration, 0, -1):
        temp_frame = frame.copy()
        text = f"Get Ready: {i}"
        temp_frame = add_text_overlay(temp_frame, text, (50, 50), font_size=80, text_color=(0, 0, 255), overlay_alpha=0.7)
        cv2.imshow("Rock Paper Scissors Lizard Spock", temp_frame)
        cv2.waitKey(1000)
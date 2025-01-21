from PIL import Image
import pytesseract
from mss import mss

def capture_and_extract_text():
    with mss() as sct:
        screenshot = sct.grab(sct.monitors[1])  # Capture the primary monitor
        img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)
        text = pytesseract.image_to_string(img)
        return text

# Test the function
text = capture_and_extract_text()
print("Extracted Text:\n", text)
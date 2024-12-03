import pyautogui
import pytesseract
from PIL import ImageGrab
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

bet_int = 1
def read_chat_and_respond():
    global bet_int  # Declare bet_int as global so we can modify it

    chat_box = ImageGrab.grab(bbox=(0,720, 1000, 1340))
    chat_text = pytesseract.image_to_string(chat_box)

    # Split text into lines and print each line separately
    chat_lines = chat_text.splitlines()
    for line in reversed(chat_lines):
        if line.strip():  # Ignore empty lines
            print(f"Chat line: {line.strip()}")

            # Check for "You won" or "Tou won"
            if "You won" in line or "Tou won" in line or "You wom" in line or "Tou wom" in line or "You wor" in line:
                print("Detected a win! Typing the bet command.")
                bet_int = 1

                pyautogui.typewrite("cf "+ get_bet_string(bet_int) + " heads")  # Type the command
                pyautogui.press("enter")
                command_spam()
                pyautogui.press("/")

            elif "You lost" in line or "Tou lost" in line:
                print("Detected a loss! Doubling the bet!")
                bet_int = bet_int + 1

                pyautogui.typewrite("cf " + get_bet_string(bet_int) + " heads")  # Type the command
                pyautogui.press("enter")
                command_spam()
                pyautogui.press("/")

def take_image():
    img = ImageGrab.grab(bbox=(0,720, 1000, 1340))
    img.show()  # Opens the captured area so you can verify
# Main loop
print("Script running... Logging chat text line by line.")

def get_bet_string(number: int) -> str:
    # Define the base values
    base_values = ["250b", "500b", "1t", "2t", "4t", "8t", "16t", "32t", "64t", "128t", "256t"]


    return base_values[number - 1]


# take_image()

# Clears the chat

def command_spam():
    for i in range(10):
        pyautogui.press("/")
        pyautogui.typewrite("plop")
        pyautogui.press("enter")

while True:
    read_chat_and_respond()
    time.sleep(1)
import os
import time
import sys
import termios
import tty
import datetime

# Terminal settings
orig_settings = termios.tcgetattr(sys.stdin)

# Constants
SENSOR_FILES = {"CO2": "co2.txt", "O2": "o2.txt", "IRIS": "iris.txt", "PULSE": "pulse.txt", "TIME": "time.txt"}
QUESTION_FILE = "questions.txt"
RESULTS_FILE = "results.csv"
MAIN_MENU_TEXT = "[Main Menu]"
BACK_BUTTON_TEXT = "[back]"
NEXT_BUTTON_TEXT = "[next]"
BUTTONS = {27: {"right": 67, "left": 68, "up": 65, "down": 66}}  # Arrow key codes

# Load questions
with open(QUESTION_FILE, "r") as f:
    questions = [line.strip() for line in f.readlines() if line.strip()]

# Create results file if it doesn't exist
if not os.path.isfile(RESULTS_FILE):
    with open(RESULTS_FILE, "w") as f:
        f.write("timestamp,question,time,response,result\n")

# Get sensor readings
def get_sensor_reading(sensor):
    with open(SENSOR_FILES[sensor], "r") as f:
        return int(f.read().strip())

# Update sensor readings
def update_sensor_readings():
    return {sensor: get_sensor_reading(sensor) for sensor in SENSOR_FILES}

# Save result to CSV
def save_result(result):
    with open(RESULTS_FILE, "a") as f:
        f.write(f"{datetime.datetime.now()},{result['question']},{result['time']},{result['response']},{result['result']}\n")

# Render question and sensor readings
def render(question_text, time_left, co2, o2, iris, pulse, elapsed_time):
    # Clear screen
    os.system("clear")

    # Render sensor readings
    sensor_line = f'[CO2 {co2}]  [O2 {o2}]  [IRIS {iris}]  [PULSE {pulse}]  [TIME {elapsed_time}]'
    print(sensor_line)

    # Render question
    for line in question_text:
        print(line)

    # Render time left
    filled_blocks = int((1 - time_left) * 50)
    print(" " * filled_blocks + "█" * (50 - filled_blocks))

    # Render buttons
    buttons_line = f"{BACK_BUTTON_TEXT}  {NEXT_BUTTON_TEXT}"
    print(buttons_line)

    # Render main menu
    main_menu_line = MAIN_MENU_TEXT.rjust(80)
    print(main_menu_line)

# Main loop
def main():
    # Initialize
    current_question = 0
    sensor_readings = update_sensor_readings()
    co2 = sensor_readings["CO2"]
    o2 = sensor_readings["O2"]
    iris = sensor_readings["IRIS"]
    pulse = sensor_readings["PULSE"]
    elapsed_time = sensor_readings["TIME"]
    results = []

    while True:
        # Render
        question_text = questions[current_question].split("\n")
        time_left = elapsed_time / int(questions[current_question].split(" ")[-1].replace(")", ""))
        render(question_text, time_left, co2, o2, iris, pulse, elapsed_time)

        # Input
        tty.setraw(sys.stdin.fileno())
        char_code = ord(sys.stdin.read(1))
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)

        # Process input
        if char_code == BUTTONS
        
        #TODO: What happened here?  ChatGPT just stop?
        

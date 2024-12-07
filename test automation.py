
import pyautogui
import time
import random
from datetime import datetime

# Start button
sbtnCoordinates = (1297, 308)

# Coordinates of the components
corebtn = (553, 170)
daemonbtn = (555, 191)
webbtn = (555, 212)
driverbtn = (556, 230)
certificationbtn = (554, 254)
buslibbtn = (558, 279)
projectbtn = (557, 299)
# custombtn = (558, 320)

# List of buttons to click
buttons = [corebtn, daemonbtn, webbtn, driverbtn, certificationbtn, buslibbtn, projectbtn]

initial_components = []

print("The application is starting")
time.sleep(6)

start_time = time.time()
start_datetime = datetime.fromtimestamp(start_time)

while True:
    # Select and save the first 5 buttons
    initial_components = random.sample(buttons, 7)
    print("Initially selected:", initial_components)

    # First execution
    for component in initial_components:
        x, y = component
        pyautogui.moveTo(x, y, duration=0.5)
        pyautogui.doubleClick()
        time.sleep(2)

    pyautogui.moveTo(*sbtnCoordinates, duration=0.5)
    pyautogui.click()

    print("Update Tool start time:", start_datetime.strftime("%Y-%m-%d %H:%M:%S"))
    print("Update tool is running")
    time.sleep(1080)  # Wait for 18 minutes

    print("Clicking 'Done'")
    time.sleep(2)
    pyautogui.moveTo(1108, 601, duration=0.5)
    pyautogui.doubleClick()
    time.sleep(2)

    # Second execution (cancel selection and make a new selection)
    print("Canceling buttons")
    for component in initial_components:
        x, y = component
        pyautogui.moveTo(x, y, duration=0.5)
        pyautogui.doubleClick()
        time.sleep(2)

    # Select new 5 buttons
    print("Selecting new buttons")
    random_components = random.sample(buttons, 5)
    print("Newly selected:", random_components)

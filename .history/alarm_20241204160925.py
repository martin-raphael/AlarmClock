import datetime
from playsound import playsound
import time
import keyboard  # Requires the `keyboard` module

# Get alarm time input
alarmHour = int(input("Enter Hour (1-12): "))
alarmMin = int(input("Enter Minute (0-59): "))
alarmAm = input("am/pm: ").lower()

# Convert 12-hour format to 24-hour format
if alarmAm == "pm" and alarmHour != 12:
    alarmHour += 12
elif alarmAm == "am" and alarmHour == 12:
    alarmHour = 0

print(f"Alarm set for {alarmHour:02d}:{alarmMin:02d}")
print("Press 'Esc' to stop the alarm.")

# Wait for the alarm time
while True:
    now = datetime.datetime.now()
    if alarmHour == now.hour and alarmMin == now.minute:
        print("Playing alarm... Press 'Esc' to stop.")
        while True:
            PlaySound("onrepeat.mp3")  # Play in non-blocking mode
            if keyboard.is_pressed("esc"):  # Check if 'Esc' key is pressed
                print("Alarm stopped.")
                break
        break
    elif keyboard.is_pressed("esc"):  # Allow exiting before alarm time
        print("Alarm canceled.")
        break
    time.sleep(1)  # Wait for 1 second to reduce CPU usage

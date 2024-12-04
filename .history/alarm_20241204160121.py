import datetime
from playsound import playsound
import time

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

# Wait for the alarm time
while True:
    now = datetime.datetime.now()
    if alarmHour == now.hour and alarmMin == now.minute:
        print("Playing alarm...")
        playsound("onrepeat.mp3")
        break
    time.sleep(1)  # Wait for 1 second to reduce CPU usage

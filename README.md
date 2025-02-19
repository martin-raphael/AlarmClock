# Python Alarm Clock

This is a simple Python-based alarm clock that plays an audio file at a specified time. It uses the `playsound` module to play MP3 files and checks the current system time to trigger the alarm.

## Features
- Set an alarm using 12-hour format (AM/PM).
- Automatically converts the entered time to a 24-hour format.
- Plays an MP3 file when the alarm time is reached.

## Requirements
- Python 3.6 or higher
- `playsound` module installed:
  ```bash
  pip install playsound
  ```
- An MP3 file (default: `onrepeat.mp3`) placed in the same directory as the script.

## How to Use
1. Save the script to a file (e.g., `alarm_clock.py`).
2. Place your desired MP3 file in the same directory as the script.
3. Run the script:
   ```bash
   python alarm_clock.py
   ```
4. Enter the alarm time in the prompted format:
   - **Hour**: A number between 1 and 12.
   - **Minute**: A number between 0 and 59.
   - **AM/PM**: Enter `am` or `pm`.

### Example:
If you want to set an alarm for **8:30 AM**:
```
Enter Hour (1-12): 8
Enter Minute (0-59): 30
am/pm: am
```

The script will notify you that the alarm is set, and it will play the MP3 file at the specified time.

## File Structure
Ensure the directory structure looks like this:
```
alarm_clock/
    alarm_clock.py
    onrepeat.mp3
```

## Troubleshooting
- **Alarm doesn’t play**: Ensure `onrepeat.mp3` is in the same directory and is a valid MP3 file.
- **Module not found**: Install the `playsound` module by running:
  ```bash
  pip install playsound
  ```
- **Time format issues**: Enter the time in the 12-hour format, and ensure AM/PM is correctly specified.

## Customization
- **Change the alarm sound**: Replace `onrepeat.mp3` with any MP3 file of your choice. Update the filename in the script if necessary.
- **Add snooze functionality**: Modify the script to allow snoozing for a few minutes.

## License
This script is free to use and modify. Contributions and suggestions are welcome!

---

Let me know if you'd like to enhance the functionality or documentation further!
from playsound import playsound
import time

class AlarmTimer:
    def __init__(self):
        self.time_elapsed = 0

    def countdown(self, seconds):
        """
        Countdown timer for the alarm.
        """
        self.time_elapsed = 0

        while self.time_elapsed < seconds:
            time.sleep(1)
            self.time_elapsed += 1

            # Calculate remaining time
            time_left = seconds - self.time_elapsed
            minutes_left = time_left // 60
            seconds_left = time_left % 60

            # Display the countdown timer
            print(f"\rAlarm will sound in: {minutes_left:02d}:{seconds_left:02d}", end="", flush=True)

        print()  # Move to the next line after the countdown is complete
        self.play_alarm_sound()

    def play_alarm_sound(self):
        """
        Plays the alarm sound effect.
        """
        playsound("alarm_sound_effect.mp3")

def main():
    # Get the waiting time from the user
    minutes = int(input("How many minutes to wait: "))
    seconds = int(input("How many seconds to wait: "))
    total_seconds = minutes * 60 + seconds  # Convert the total waiting time to seconds

    # Initialize and start the alarm countdown
    timer = AlarmTimer()
    timer.countdown(total_seconds)

if __name__ == "__main__":
    main()


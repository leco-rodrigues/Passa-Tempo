from time import sleep
from datetime import datetime as dt
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer

def set_alarm(alarm_time: str) -> None:
    print(f"Alarm set for {alarm_time}")
    sound_file: str = "Misc/icecreamtrucksong.wav"
    is_running: bool = True

    while is_running:
        current_time = dt.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("Short break time! 🥱")

            mixer.init()
            mixer.music.load(sound_file)
            mixer.music.play()

            while mixer.music.get_busy:
                sleep(1)
            
            is_running = False

        sleep(1)


if __name__ == "__main__":
    print("=" * 33 + f"\n\tSetting the alarm\n" + "=" * 33 + "\n")
    alarm_time: str = str(input("Enter the alarm time (HH:MM:SS): "))
    set_alarm(alarm_time)

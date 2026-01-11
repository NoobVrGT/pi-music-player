# main.py
# Entry point for the music player

from lcd_driver import LCD
from joystick import Joystick
from ui import UI
from audio import AudioPlayer

def main():
    lcd = LCD()
    joystick = Joystick()
    ui = UI()
    audio = AudioPlayer()

    # TODO: load config, load music list, show menu

    while True:
        # TODO: read joystick input
        # TODO: update UI
        # TODO: control audio
        pass

if __name__ == "__main__":
    main()

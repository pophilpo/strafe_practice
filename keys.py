import time

import keyboard


class KeyListener:
    def __init__(self, stop_key="c"):

        self.stop_key = stop_key
        self.events = list()

    def listen(self, event):

        for code in keyboard._pressed_events:
            print(code)

    def start(self):
        keyboard.hook(self.listen)
        keyboard.wait(self.stop_key)


def main():

    logger = KeyListener()
    logger.start()


if __name__ == "__main__":
    main()

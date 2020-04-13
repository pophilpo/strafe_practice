import time

import keyboard


class Event:
    def __init__(self, key_code, timestamp):
        self.key_code = key_code
        self.timestamp = timestamp

    def __repr__(self):

        return f"Pressed key {self.key_code} at {self.timestamp}"


class KeyListener:
    def __init__(self, stop_key="c"):

        self.stop_key = stop_key
        self.events = list()

    def listen(self, event):

        for code in keyboard._pressed_events:
            timestamp = time.time()
            event = Event(code, timestamp)
            self.events.append(event)

    def start(self):
        keyboard.hook(self.listen)
        keyboard.wait(self.stop_key)

    def __repr__(self):

        events = [event.__repr__() for event in self.events]

        return "\n".join(events)


def main():

    logger = KeyListener()
    logger.start()
    print(logger)


if __name__ == "__main__":
    main()

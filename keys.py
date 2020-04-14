import time

import keyboard


class KeyEvent:
    def __init__(self, key_code, timestamp):
        self.key_code = key_code
        self.timestamp = timestamp

    def __repr__(self):

        return f"Pressed key {self.key_code} at {self.timestamp}"


class KeyListener:
    def __init__(self, stop_key="c"):

        self.stop_key = stop_key
        self.events = list()

        # My keyboard specific A/D keys.
        self.left_strafe = 30
        self.right_strafe = 32

    def listen(self, event):

        for code in keyboard._pressed_events:
            timestamp = time.time()
            event = KeyEvent(code, timestamp)
            self.events.append(event)

    def start(self):

        keyboard.hook(self.listen)

    def map_strafe_scan_codes(self):
        print("\rPress your right strafe key")

        time.sleep(0.5)

        right_strafe_key = keyboard.read_key()
        right_strafe = keyboard.key_to_scan_codes(right_strafe_key)[0]

        print("\rPress your left strafe key")
        time.sleep(0.5)

        left_strafe_key = keyboard.read_key()
        left_strafe = keyboard.key_to_scan_codes(left_strafe_key)[0]

        self.left_strafe = left_strafe
        self.right_strafe = right_strafe

        print("\rStrafe keys are now mapped")

    def __repr__(self):

        events = [event.__repr__() for event in self.events]

        return "\n".join(events)

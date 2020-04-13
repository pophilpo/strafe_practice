import fileinput
import json
import sys
import time

import mouse

# TODO: Handle cases wiht 0 events


class MouseEvent:
    def __init__(self, direction, start_time, end_time):

        self.direction = direction
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):

        return (
            f"Direction: {self.direction}, Duration: {self.end_time - self.start_time}"
        )


class MouseLogger:
    def __init__(self):

        self.events = list()

    def listen(self, event):

        data = event._asdict()

        if self.events:
            if data["x"] != self.events[-1]["x"]:

                self.events.append(data)
        else:
            self.events.append(data)

    def start(self):
        mouse.hook(self.listen)

    def generate_data(self):

        data = list()

        first_event = self.events[0]
        second_event = self.events[1]

        start_time = first_event["time"]
        x_coord = first_event["x"]
        second_x_coord = second_event["x"]
        if x_coord > second_x_coord:
            direction = "Left"
        else:
            direction = "Right"

        print(direction)
        for event in self.events[1:]:

            event_x = event["x"]

            if direction == "Left":
                if x_coord < event_x:
                    end_time = event["time"]
                    new_mouse_event = MouseEvent(direction, start_time, end_time)
                    data.append(new_mouse_event)

                    start_time = end_time
                    direction = "Right"
                    print(direction)

            elif direction == "Right":
                if x_coord > event_x:
                    end_time = event["time"]

                    new_mouse_event = MouseEvent(direction, start_time, end_time)
                    data.append(new_mouse_event)

                    start_time = end_time
                    direction = "Left"
                    print(direction)

            x_coord = event_x

        end_time = self.events[-1]["time"]
        last_mouse_event = MouseEvent(direction, start_time, end_time)
        data.append(last_mouse_event)

        return data


def main():

    logger = MouseLogger()
    logger.start()
    time.sleep(2)
    data = logger.generate_data()

    for e in data:
        print(e)


if __name__ == "__main__":
    main()

from datetime import time, timedelta

class Event:
    def __init__(self, person: str, title: str, start_time: time, end_time: time):
        self.person = person
        self.title = title
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"Event({self.person}, {self.title}, {self.start_time}, {self.end_time})"
    
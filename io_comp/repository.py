import csv
from pathlib import Path
from typing import List
from datetime import datetime
from io_comp.models import Event


class CsvCalendarRepository:
    def __init__(self, file_path: str = "resources/calendar.csv"):
        self.file_path = Path(file_path)

    def load_events(self) -> List[Event]:
        events = []
        if not self.file_path.exists():
            return events

        with open(self.file_path, mode="r", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # נרמול מפתחות המילון (הסרת רווחים והמרת לאותיות קטנות)
                normalized_row = {k.strip().lower(): v for k, v in row.items() if k}

                person = normalized_row.get("person", "").strip()
                title = normalized_row.get("title", "").strip()
                start_str = normalized_row.get("start_time", "").strip()
                end_str = normalized_row.get("end_time", "").strip()

                if not person or not start_str or not end_str:
                    continue

                start_time = datetime.strptime(start_str, "%H:%M").time()
                end_time = datetime.strptime(end_str, "%H:%M").time()

                events.append(Event(person, title, start_time, end_time))

        return events
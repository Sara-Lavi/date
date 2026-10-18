from typing import List
from datetime import time, timedelta, datetime
from io_comp.repository import CsvCalendarRepository

def find_available_slots(person_list: List[str], event_duration: timedelta) -> List[time]:
    """
    Find all available time slots for a meeting with the given pfople and duration.

    Args:
        person_list: List of person names who should attend the meeting
        event_duration: Duration of the desired meeting

    Returns:
        List of start times when all persons are available
    """
    repository = CsvCalendarRepository()
    events = repository.load_events()

    # סינון אירועים לפי האנשים המבוקשים
    relevant_events = [e for e in events if e.person in person_list]

    # הגדרת שעות פעילות יום העבודה (לדוגמה: 09:00 עד 17:00)
    day_start = time(9, 0)
    day_end = time(17, 0)

    # המרת שעות לתאריך בסיס לצורך חישובים נוחים
    base_date = datetime.today().date()
    current_dt = datetime.combine(base_date, day_start)
    end_limit = datetime.combine(base_date, day_end)
    step = timedelta(minutes=30)

    available_slots = []

    while current_dt + event_duration <= end_limit:
        slot_start = current_dt.time()
        slot_end = (current_dt + event_duration).time()

        # בדיקה האם יש התנגשות עם פגישה קיימת של מי מהאנשים
        is_conflict = False
        for event in relevant_events:
            # תנאי חפיפה בין טווחי זמנים
            if not (slot_end <= event.start_time or slot_start >= event.end_time):
                is_conflict = True
                break

        if not is_conflict:
            available_slots.append(slot_start)

        current_dt += step

    return available_slots

def main():
    # דוגמת הרצה לבדיקה
    duration = timedelta(minutes = 60)
    slots = find_available_slots(["Alice", "Jack"], duration)
    print("Available slots:", slots)

if __name__ == "__main__":
    main()
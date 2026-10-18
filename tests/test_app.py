from datetime import timedelta, time
from io_comp.app import find_available_slots


def test_find_available_slots_standard():
    duration = timedelta(hours=1)
    slots = find_available_slots(["Alice", "Jack"], duration)
    assert isinstance(slots, list)


def test_find_available_slots_empty_person_list():
    duration = timedelta(minutes=30)
    slots = find_available_slots([], duration)
    assert isinstance(slots, list)


def test_find_available_slots_long_duration():
    # בדיקה עבור משך זמן של 9 שעות (ארוך מיום העבודה המוגדר)
    duration = timedelta(hours=9)
    slots = find_available_slots(["Alice", "Jack"], duration)

    assert isinstance(slots, list)
    assert len(slots) == 0
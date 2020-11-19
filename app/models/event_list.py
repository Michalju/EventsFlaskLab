from app.models.event import *



event1 = Event("12th September 2020", "AC/DC", "111", "blue room", "AC/DC playing in blue room")
event2 = Event("11th November 2020", "Metallica", "110", "grey room", "Metallica playing in grey room")
events = [event1, event2]


def add_new_event(event):
    events.append(event)

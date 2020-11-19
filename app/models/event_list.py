from app.models.event import *



event1 = Event("12th September 2020", "AC/DC", "120000", "blue", "AC/DC playing in blue room",True)
event2 = Event("11th November 2020", "Metallica", "110000", "orange", "Metallica playing in orange room", False)
event3 = Event("12th December 2020", "Slipknot", "50000", "blue", "Slipknot playing in blue room",True)
event4 = Event("11th January 2021", "Death", "110000", "black", "Death playing in grey room", False)
events = [event1, event2, event3, event4]


def add_new_event(event):
    events.append(event)

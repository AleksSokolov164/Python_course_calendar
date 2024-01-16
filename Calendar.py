"""
Класс календаря - хранит события.
он умеет искать все события из промежутка (в том числе повторяющиеся)
он умеет добавлять/удалять события.
У каждого календаря ровно один пользователь.
"""
import datetime
import Event



class Calendar:
    events = list()
    extradition = list()

    def __init__(self):
        self.events = list()
        self.extradition = list()

    def add_event(self, ets, eta, name, description, user, a, b):
        ev = Event.Event()
        ev.edit_name(name)
        ev.edit_description(description)
        ev.edit_ets(ets)
        ev.edit_eta(eta)
        ev.edit_period(a, b)
        ev.add_users(user)

    def del_event(self, ev):
        self.events.remove(ev)

    def search_events(self, ets1, eta2):
        events1 = list()
        for i in self.events:
            if i.ets >= ets1 and i.eta <= eta2:
                events1.append(i)
        return events1

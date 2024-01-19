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
    welcome = list()

    def __init__(self):
        self.events = list()
        self.welcome = list()

    def __repr__(self):
        return (f'{self.events}')

    def add_event(self, author, name, description, ets, eta, users, period):
        ev = Event.Event(author, name, description, ets, eta, users, period)
        self.events.append(ev)

    def append_event(self, event):
        self.events.append(event)

    def del_event(self, ev):
        self.events.remove(ev)

    def search_events(self, ets1, eta2):
        events1 = list()
        for ev in self.events:
            if ev._ets >= ets1 and ev._eta <= eta2:
                events1.append(ev)
                if ev._period == 1:
                    a, b = ev._ets, ev._eta
                    k = datetime.timedelta(days=1)
                    while True:
                        x = datetime.datetime(a.year, a.month, a.day, a.hour, a.minute, a.second) + k
                        y = datetime.datetime(b.year, b.month, b.day, b.hour, b.minute, b.second) + k
                        if x >= ets1 and y <= eta2:
                            ev1 = Event.Event(ev._author_id, ev._name, ev._description, x, y, ev._users, ev._period)
                            events1.append(ev1)
                            k += datetime.timedelta(days=1)
                        else:
                            break
                elif ev._period == 2:
                    a, b = ev._ets, ev._eta
                    k = datetime.timedelta(days=7)
                    while True:
                        x = datetime.datetime(a.year, a.month, a.day, a.hour, a.minute, a.second) + k
                        y = datetime.datetime(b.year, b.month, b.day, b.hour, b.minute, b.second) + k
                        if x >= ets1 and y <= eta2:
                            ev1 = Event.Event(ev._author_id, ev._name, ev._description, x, y, ev._users, ev._period)
                            events1.append(ev1)
                            k += datetime.timedelta(days=7)
                        else:
                            break
                elif ev._period == 3:
                    a, b = ev._ets, ev._eta
                    k = 0
                    n = 0
                    while True:
                        if k == 13:
                            k = 1
                            n += 1
                        x = datetime.datetime(a.year + n, a.month + k, a.day, a.hour, a.minute, a.second)
                        y = datetime.datetime(b.year + n, a.month + k, b.day, b.hour, b.minute, b.second)
                        if x >= ets1 and y <= eta2:
                            ev1 = Event.Event(ev._author_id, ev._name, ev._description, x, y, ev._users, ev._period)
                            events1.append(ev1)
                            k += 1
                        else:
                            break
                elif ev._period == 4:
                    a, b = ev._ets, ev._eta
                    k = datetime.timedelta(days=365)
                    while True:
                        x = datetime.datetime(a.year, a.month, a.day, a.hour, a.minute, a.second) + k
                        y = datetime.datetime(b.year, b.month, b.day, b.hour, b.minute, b.second) + k
                        if x >= ets1 and y <= eta2:
                            ev1 = Event.Event(ev._author_id, ev._name, ev._description, x, y, ev._users, ev._period)
                            events1.append(ev1)
                            k += datetime.timedelta(days=365)
                        else:
                            break

        return events1

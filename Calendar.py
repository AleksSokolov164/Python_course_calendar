"""
Класс календаря - хранит события.
он умеет искать все события из промежутка (в том числе повторяющиеся)
он умеет добавлять/удалять события.
У каждого календаря ровно один пользователь.
"""
import datetime
import Event
import User


class Calendar:
    _user = User.User()
    _events = list()
    _welcome = list()

    def __init__(self, user=User.User(), events=list(), welcome=list()):
        self._user = user
        self._events = events
        self._welcome = welcome


    def add_event(self, author_id, name, description, ets, eta, period, users):
        event = Event.Event(author_id, name, description, ets, eta, period, users)
        self._events.append(event)

    def append_event(self, event):
        self._events.append(event)

    def del_event(self, event):
        self._events.remove(event)

    def add_welcome(self, author_id, name, description, ets, eta, period, users):
        event = Event.Event(author_id, name, description, ets, eta, period, users)
        self._welcome.append(event)

    def append_welcome(self, event):
        self._welcome.append(event)

    def del_welcome(self, event):
        self._welcome.remove(event)

    def search_events(self, ets1, eta2):
        events1 = list()
        for ev in self._events:
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


def edit_iteration(self, iteration):
    b = iteration
    if b != 1 or b != 2 or b != 3 or b != 4:
        raise Exception("Введено неверное значение периода': \n"
                        "'1 - ежедневное'\n"
                        "'2 - еженедельное'\n"
                        "'3 - ежемесячное'\n"
                        "'4 - ежегодное'\n")
    else:
        self._period = iteration

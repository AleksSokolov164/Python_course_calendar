"""
Класс календаря - хранит события.
он умеет искать все события из промежутка (в том числе повторяющиеся)
он умеет добавлять/удалять события.
У каждого календаря ровно один пользователь.
"""
import datetime
import Event


class Calendar:
    calendar_id = ''
    events = list()
    welcome = list()

    def __init__(self):
        self.calendar_id = dict()
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
                #events1.append(ev)
                if ev._period == 1:
                    a, b = ev._ets, ev._eta
                    k = 1
                    while True:
                        x = datetime.datetime(a.year, a.month, a.day + k, a.hours, a.minute, a.second)
                        y = datetime.datetime(b.year, b.month, b.day + k, b.hours, b.minute, b.second)
                        if x >= ets1 and y <= eta2:
                            ev1 = Event.Event(ev._author_id, ev._name, ev._description, x, y, ev._users, ev._period)
                            events1.append(ev1)
                            k += 1
                        else:
                            break
                elif ev._period == 2:
                    a, b = ev._ets, ev._eta
                    k = 7
                    while True:
                        x = datetime.datetime(a.year, a.month, a.day + k, a.hours, a.minute, a.second)
                        y = datetime.datetime(b.year, b.month, b.day + k, b.hours, b.minute, b.second)
                        if x >= ets1 and y <= eta2:
                            ev1 = Event.Event(ev._author_id, ev._name, ev._description, x, y, ev._users, ev._period)
                            events1.append(ev1)
                            k += 7
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
                    k = 1
                    while True:
                        x = datetime.datetime(a.year + k, a.month, a.day, a.hour, a.minute, a.second)
                        y = datetime.datetime(b.year + k, b.month, b.day, b.hour, b.minute, b.second)
                        if x >= ets1 and y <= eta2:
                            ev1 = Event.Event(ev._author_id, ev._name, ev._description, x, y, ev._users, ev._period)
                            events1.append(ev1)
                            k += 1
                        else:
                            break

        return events1


c = Calendar()
x1 = datetime.datetime(2023, 12, 31, 23, 59, 59)
y1 = datetime.datetime(2024, 1, 1, 00, 00, 1)

print(c)
ev1 = Event.Event("@1", 'Новый год', 'Ёлка, семья, Дед. Мороз и подарки', x1, y1, [1, 1, 1], 4)
c.append_event(ev1)
print(c)
x2 = datetime.datetime(2024, 1, 13, 23, 59, 59)
y2 = datetime.datetime(2024, 1, 14, 00, 00, 1)
c.add_event("@2", "Старый Новый год", "Ёллллка", x2, y2, [1, 1, 1], 4)
print(c)
x4 = datetime.datetime(2024, 2, 17, 00, 00, 00)
y4 = datetime.datetime(2024, 2, 18, 00, 00, 1)
c.add_event("@3", "ДР", "Нет Ёллллка", x2, y2, [1, 1, 1], 3)
print(c)

x3 = datetime.datetime(2023, 12, 20, 23, 59, 59)
y3 = datetime.datetime(2025, 3, 14, 00, 00, 1)
c.search_events(x3, y3)
for i in c.search_events(x3, y3):
    print(i)

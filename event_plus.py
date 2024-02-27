import pandas as pd

print(pd.date_range(start='1/1/1980', end='11/1/1982', freq='M'))
# import datetime
# import Event
#
#
# def calendary_admin(self):  # вывод календаря по заданному периоду
#     user = self._admin
#     events1 = list()
#     print('Для вывода вашего календаря задайте период')
#     y, m, d = map(int, input("Введите первую дату в формате yy-mm-dd").split("-"))
#     h, mi, s = map(int, input("Введите первое время в формате hh:mm:ss").split(":"))
#     ets1 = datetime.datetime(y, m, d, h, mi, s)
#     y, m, d = map(int, input("Введите вторую дату в формате yy-mm-dd").split("-"))
#     h, mi, s = map(int, input("Введите второе время в формате hh:mm:ss").split(":"))
#     eta2 = datetime.datetime(y, m, d, h, mi, s)
#     for ev in self._events:
#         if ev._ets >= ets1 and ev._eta <= eta2:
#             events1.append(ev)
#             if ev._period == 1 or ev._period == 2 or ev._period == 4:
#                 day = 1 if ev._period == 1 else (7 if ev._period == 2 else 365)
#                 a, b = ev._ets, ev._eta
#                 k = datetime.timedelta(days=day)
#                 while True:
#                     x = datetime.datetime(a.year, a.month, a.day, a.hour, a.minute, a.second) + k
#                     y = datetime.datetime(b.year, b.month, b.day, b.hour, b.minute, b.second) + k
#                     if x >= ets1 and y <= eta2:
#                         ev1 = Event.Event(ev._author_id, ev._name, ev._description, x, y, ev._users, ev._period)
#                         events1.append(ev1)
#                         k += datetime.timedelta(days=day)
#                     else:
#                         break
#             elif ev._period == 3:
#                 a, b = ev._ets, ev._eta
#                 if ev._ets.day in range(1, 28):
#                     n = 0
#                     k = 1
#                     while True:
#                         if k == 13:
#                             n += 1
#                             k = 1
#                             x = datetime.datetime(a.year + n, a.month + k, a.day, a.hour, a.minute, a.second)
#                             y = datetime.datetime(b.year + n, a.month + k, b.day, b.hour, b.minute, b.second)
#                                                         if x >= ets1 and y <= eta2:
#                                 ev1 = Event.Event(ev._author_id, ev._name, ev._description, x, y, ev._users, ev._period)
#                                 events1.append(ev1)
#                                 k += 1
#                             else:
#                                 break
#                         else:
#                             x = datetime.datetime(a.year, a.month + k, a.day, a.hour, a.minute, a.second)
#                             y = datetime.datetime(b.year, a.month + k, b.day, b.hour, b.minute, b.second)
#                             if x >= ets1 and y <= eta2:
#                                 ev1 = Event.Event(ev._author_id, ev._name, ev._description, x, y, ev._users, ev._period)
#                                 events1.append(ev1)
#                                 k += 1
#                             else:
#                                 break
#                 else:
#                     d = b - a
#                     n = 0
#                     k = 1
#                     while True:
#                         if k == 13:
#                             n += 1
#                             k = 1
#                             x = datetime.datetime(a.year + n, a.month + k, 28, a.hour, a.minute, a.second)
#                             y = x + d
#                             if x >= ets1 and y <= eta2:
#                                 ev1 = Event.Event(ev._author_id, ev._name, ev._description, x, y, ev._users, ev._period)
#                                 events1.append(ev1)
#                                 k += 1
#                             else:
#                                 break
#                         else:
#                             x = datetime.datetime(a.year, a.month + k, 28, a.hour, a.minute, a.second)
#                             y = x + d
#                             if x >= ets1 and y <= eta2:
#                                 ev1 = Event.Event(ev._author_id, ev._name, ev._description, x, y, ev._users, ev._period)
#                                 events1.append(ev1)
#                                 k += 1
#                             else:
#                                 break
#
#
#
#






                a, b = ev._ets, ev._eta


    for event in events1:
        print(f'число:{event._ets.day}, месяц:{event._ets.month}, год:{event._ets.year}')
        print(event)

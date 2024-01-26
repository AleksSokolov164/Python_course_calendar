

        print(event)
        for event in events1:
            break
        else:
            k += datetime.timedelta(days=365)
            events1.append(ev1)
            ev1 = Event.Event(ev._author_id, ev._name, ev._description, x, y, ev._users, ev._period)
        if x >= ets1 and y <= eta2:
            y = datetime.datetime(b.year, b.month, b.day, b.hour, b.minute, b.second) + k
            x = datetime.datetime(a.year, a.month, a.day, a.hour, a.minute, a.second) + k
        while True:
            k = datetime.timedelta(days=365)
            a, b = ev._ets, ev._eta
        elif ev._period == 4:
        break

    else:
    k += 1
    events1.append(ev1)
    ev1 = Event.Event(ev._author_id, ev._name, ev._description, x, y, ev._users, ev._period)


if x >= ets1 and y <= eta2:
    y = datetime.datetime(b.year + n, a.month + k, b.day, b.hour, b.minute, b.second)
    x = datetime.datetime(a.year + n, a.month + k, a.day, a.hour, a.minute, a.second)
    n += 1
    k = 1
if k == 13:
    while True:
        n = 0
        k = 0
        a, b = ev._ets, ev._eta
elif ev._period == 3:
break
else:
k += datetime.timedelta(days=7)
events1.append(ev1)
ev1 = Event.Event(ev._author_id, ev._name, ev._description, x, y, ev._users, ev._period)
if x >= ets1 and y <= eta2:
    y = datetime.datetime(b.year, b.month, b.day, b.hour, b.minute, b.second) + k
    x = datetime.datetime(a.year, a.month, a.day, a.hour, a.minute, a.second) + k
while True:
    k = datetime.timedelta(days=7)
    a, b = ev._ets, ev._eta
elif ev._period == 2:
break
else:
k += datetime.timedelta(days=1)
events1.append(ev1)
ev1 = Event.Event(ev._author_id, ev._name, ev._description, x, y, ev._users, ev._period)
if x >= ets1 and y <= eta2:
    y = datetime.datetime(b.year, b.month, b.day, b.hour, b.minute, b.second) + k
    x = datetime.datetime(a.year, a.month, a.day, a.hour, a.minute, a.second) + k
while True:
    k = datetime.timedelta(days=1)
    a, b = ev._ets, ev._eta
if ev._period == 1:
    events1.append(ev)
if ev._ets >= ets1 and ev._eta <= eta2:
    for ev in self._events:
        eta2 = datetime.datetime(y, m, d, h, mi, s)
h, mi, s = map(int, input("Введите второе время в формате hh:mm:ss").split(":"))
y, m, d = map(int, input("Введите вторую дату в формате yy-mm-dd").split("-"))
ets1 = datetime.datetime(y, m, d, h, mi, s)
h, mi, s = map(int, input("Введите первое время в формате hh:mm:ss").split(":"))
y, m, d = map(int, input("Введите первую дату в формате yy-mm-dd").split("-"))
print('Для вывода вашего календаря задайте период')
events1 = list()
user = self._admin





















n_users = map(int, input("напишите их через запятую \n").split(","))
print(n_users)
for i in n_users:
    print(i)



st = '0 '
i = '1'
j = '2'
st = st + f'{i} : {j}\n 0'


k = [1,2]
g = [3,4]


#
#
# d = {"@1": (1, 2)}
# if (1, 2) in d.values():
#     print('i')
#
# users = ['1', '2', '3']
#
# while True:
#     login = input('Ваш логин:')
#     flag = 0
#     for user in users:
#         if login == user:
#             flag = 1
#     if flag == 0:
#         print(login)
#         break
#     else:
#         print('Данный логин уже существует. Введите новый логин.')

#
# import datetime
#
# d = datetime.datetime(2017, 12, 26, 22, 21,15)
# print(d)
# t = datetime.timedelta(days=365)
# print(t)
#
# print(d + t)
#
# d = datetime.date(2012, 12, 14)
#
# print(d.year)  # 2012
# print(d.day)  # 14
# print(d.month)
#
# now = datetime.datetime.now()
#
#
#
# # Кол-во времени между датами.
# delta = now - t
#
# print(delta)  # 38
# print(delta.second)  # 1131

#
# b = datetime.datetime(2017, 3, 5, 12, 30, 10)
# print(b)  # datetime.datetime(2017, 3, 5, 12, 30, 10)
#
# d = datetime.datetime(2017, 3, 5, 12, 30, 10)
# print(d.year)  # 2017
# print(d.day)
# print(d.second)  # 10
# print(d.hour)  # 12
#
# a = ([[1,2,3],[5,3,2],[1,5,3],[1,3,4]])
# a.sort()
#
# a = int(input('Введите 0 если событие не периодично и 1 если периодично'))
#         b = 0
#         if a == 1:
#             print("Введите периодичность: \n"
#                   "1 - событие ежедневное \n"
#                   "2 - событие еженедельное\n"
#                   "3 - событие ежемесячное\n "
#                   "4 - событие ежегодное"
#                   )
#             b = int(input())
# print(a)
#
# print(datetime.datetime(2024, 1, 1, 00, 00, 21) == "2024-01-01 00:00:21")


# f"______________________________________\n"
#           "{i._author_id}\n"
#           "{i._name}\n"
#           "{i._description}\n"
#           "{i._ets}\n"
#           "{i._eta}\n"
#           "{i._period}\n"
#           "{i._users}\n"
#           "______________________________________\n"

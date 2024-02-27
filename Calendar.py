"""
У каждого календаря ровно один пользователь.

он умеет добавлять/удалять события.

умеет искать все события из промежутка (в том числе повторяющиеся)

Класс календаря - хранит события.
"""

import User
import Event
import datetime


class Calendar:
    # _events = list()
    # _users = list()
    # _admin = User.User

    def __init__(self):
        self._admin = User.User
        self._users = list()
        self._events = list()


    def add_event(self, author_id, name, description, ets, eta, users, period):
        event = Event.Event(author_id, name, description, ets, eta, users, period)
        self._events.append(event)


    def get_users(self):
        return self._users

    def add_user(self, login, password):
        user = User.User(login, password)
        self._users.append(user)

    def get_calendars(self):
        return self._events

    def get_admin(self):
        return self._admin

    def new_user(self):  # новый пользователь
        while True:
            flag = 0
            login = input('Ваш логин:')
            for user in self._users:
                if login == user._login:
                    flag = 1
            if flag == 1:
                print('Данный логин уже существует. Введите новый логин.')
            else:
                break
        password = input('Ваш пароль:')
        new_user = User.User(login, password)
        self._users.append(new_user)

    def check_user(self):  # проверка логина и пароля
        print('Авторизация')
        n = 1
        while n <= 3:
            login1 = None
            login = input('Введите ваш логин:')
            for user in self._users:
                if user._login == login:
                    login1 = login
                    user1 = user
            if login1 == login:
                password = input('Ваш пароль:')
                if password == user1._password:
                    self._admin = user1
                    break
                else:
                    print(f'Вы ввели неверный пароль для {login} \n')
                    n += 1
            else:
                n += 1
                print(f'Пользователя с логином {login} не существует \n')

    def check_welcome(self):  # проверка приглашений на мероприятия
        user = self._admin
        for event in self._events:
            if event._author_id != user._id:
                if user._id in event._users.keys():
                    if event._users[user._id] == 0:
                        print('Вас приглашают принять участие в событии')
                        print(event)
                        dn = input('1 - внести данное событие в ваш календарь, \n'
                                   '2 - не внoсить событие в ваш календарь \n')
                        if dn == '1':
                            event._users[user._id] = 1
                        elif dn == '2':
                            event.del_user(user._id, user._id)
                    elif event._users[user._id] == 2:
                        print('Вас исключили из списка участников событи')
                        print(event)

    def calendary_admin(self):  # вывод календаря по заданному периоду
        user = self._admin
        events1 = list()
        print('Для вывода вашего календаря задайте период')
        y, m, d = map(int, input("Введите первую дату в формате yy-mm-dd").split("-"))
        h, mi, s = map(int, input("Введите первое время в формате hh:mm:ss").split(":"))
        ets1 = datetime.datetime(y, m, d, h, mi, s)
        y, m, d = map(int, input("Введите вторую дату в формате yy-mm-dd").split("-"))
        h, mi, s = map(int, input("Введите второе время в формате hh:mm:ss").split(":"))
        eta2 = datetime.datetime(y, m, d, h, mi, s)
        for ev in self._events:
            if ev._ets >= ets1 and ev._eta <= eta2:
                events1.append(ev)
                if ev._period == 1 or ev._period == 2 or ev._period == 4:
                    day = 1 if ev._period == 1 else (7 if ev._period == 2 else 365)
                    a, b = ev._ets, ev._eta
                    k = datetime.timedelta(days=day)
                    while True:
                        x = datetime.datetime(a.year, a.month, a.day, a.hour, a.minute, a.second) + k
                        y = datetime.datetime(b.year, b.month, b.day, b.hour, b.minute, b.second) + k
                        if x >= ets1 and y <= eta2:
                            ev1 = Event.Event(ev._author_id, ev._name, ev._description, x, y, ev._users, ev._period)
                            events1.append(ev1)
                            k += datetime.timedelta(days=day)
                        else:
                            break
                elif ev._period == 3:
                    a, b = ev._ets, ev._eta
                    if ev._ets.day in range(1, 28):
                        n = 0
                        k = 1
                        while True:
                            if (a.month + k) == 13 or k == 13:
                                n += 1
                                k = 0
                                x = datetime.datetime(a.year + n, a.month + k, a.day, a.hour, a.minute, a.second)
                                y = datetime.datetime(b.year + n, a.month + k, b.day, b.hour, b.minute, b.second)
                                if x >= ets1 and y <= eta2:
                                    ev1 = Event.Event(ev._author_id, ev._name, ev._description, x, y, ev._users, ev._period)
                                    events1.append(ev1)
                                    k += 1
                                else:
                                    break
                            else:
                                x = datetime.datetime(a.year, a.month + k, a.day, a.hour, a.minute, a.second)
                                y = datetime.datetime(b.year, a.month + k, b.day, b.hour, b.minute, b.second)
                                if x >= ets1 and y <= eta2:
                                    ev1 = Event.Event(ev._author_id, ev._name, ev._description, x, y, ev._users, ev._period)
                                    events1.append(ev1)
                                    k += 1
                                else:
                                    break
                    else:
                        d = b - a
                        n = 0
                        k = 1
                        while True:
                            if k == 13:
                                n += 1
                                k = 1
                                x = datetime.datetime(a.year + n, a.month + k, 28, a.hour, a.minute, a.second)
                                y = x + d
                                if x >= ets1 and y <= eta2:
                                    ev1 = Event.Event(ev._author_id, ev._name, ev._description, x, y, ev._users, ev._period)
                                    events1.append(ev1)
                                    k += 1
                                else:
                                    break
                            else:
                                x = datetime.datetime(a.year, a.month + k, 28, a.hour, a.minute, a.second)
                                y = x + d
                                if x >= ets1 and y <= eta2:
                                    ev1 = Event.Event(ev._author_id, ev._name, ev._description, x, y, ev._users, ev._period)
                                    events1.append(ev1)
                                    k += 1
                                else:
                                    break
        for event in events1:
            print(f'число:{event._ets.day}, месяц:{event._ets.month}, год:{event._ets.year}')
            print(event)

    def edit_events(self):  # редактирование мероприятия
        events1 = list
        number = 1
        n_events = dict()
        for i in range(len(self._events)):
            event = self._events[i]
            if self._admin._id == event._author_id or self._admin._id in event._users.keys():
                n_events[number] = i
                print(f' НОМЕР - {number}')
                number += 1
                print(event)
        if self._admin._id == event._author_id or self._admin._id in event._users.keys():
            print('Для редактирования события введите его номер')
            n_event = n_events[int(input())]
            if self._events[n_event]._author_id == self._admin._id:
                n_edit = int(input('Введите номер изменения: \n'
                                   '1 - редактировать название события \n'
                                   '2 - редактировать описание события \n'
                                   '3 - редактировать список участников события \n'
                                   '4 - удалить событие \n'
                                   ))
                if n_edit == 1:
                    new_name = input('Введите новое название:')
                    self._events[n_event].edit_name(new_name, self._admin._id)
                elif n_edit == 2:
                    new_description = input('Введите новое описание:')
                    self._events[n_event].edit_description(new_description, self._admin._id)
                elif n_edit == 3:
                    z = int(input('Введите номер изменения: \n'
                                  '1 - добавить участника\n'
                                  '2 - удалить участника\ покинуть событие\n'))
                    if z == 2:
                        print('Участники:')
                        for i in self._events[n_event]._users:
                            print(f'{i} ')
                        n_user = input('Введите id участника:')
                        if self._admin._id == n_user:
                            print('Вы не можете удалить себя из списка, т.к. вы - организатор. Вы можете удалить  событие')
                        else:
                            del self._events[n_event]._users[n_user]
                    elif z == 1:
                        print('Возможные участники события:')
                        for j in self._users:
                            if j._id not in self._events[n_event]._users:
                                print(f'{j._id}')
                        n_user = input('Введите id участника:')
                        self._events[n_event]._users[n_user] = 0
                elif n_edit == 4:
                    self._events.pop(n_event)
            else:     # elif self._events[n_event]._author_id == self._admin._id and self._admin._id in self._events[n_event]._users
                n_edit = int(input('Хотите покинуть данное событие?: \n'
                                   '1 - ДА \n'
                                   '2 - НЕТ\n'))
                if n_edit == 1:
                    del self._events[n_event]._users[self._admin._id]
        else:
            print("У вас нет событий для редактирования")

    def new_event(self):  # новое мероприятие
        author_id = self._admin._id
        name = (input("Введите название события: \n")).strip()
        description = (input("Введите описание события: \n")).strip()
        y, m, d = map(int, input("Введите дату начала мероприятия в формате yy-mm-dd").split("-"))
        h, mi, s = map(int, input("Введите время начала мероприятия в формате hh:mm:ss").split(":"))
        ets = datetime.datetime(y, m, d, h, mi, s)
        y, m, d = map(int, input("Введите дату окончания мероприятия в формате yy-mm-dd").split("-"))
        h, mi, s = map(int, input("Введите время окончания мероприятия в формате hh:mm:ss").split(":"))
        eta = datetime.datetime(y, m, d, h, mi, s)
        period = int(input("Введите периодичность события \n"
                           "4 - событие ежегодное \n"
                           "3 - событие ежемесячное\n"
                           "2 - событие еженедельное\n"
                           "1 - событие ежедневное \n"
                           "0 - событие не периодичное \n"))
        print("_______________________________________\n"
              " N   ПОЛЬЗОВАТЕЛИ               \n")
        for i in range(len(self._users)):
            print(f' {i + 1}   {self._users[i]}   ')
        print("Введите номерa пользователей, чтобы пригласить их на мероприятие ")
        n = list(map(int, input("(напишите их через запятую):\n").split(",")))
        users = dict()
        for i in n:
            users[self._users[i - 1]._id] = 0
        event = Event.Event(author_id, name, description, ets, eta, users, period)
        self._events.append(event)

    def __str__(self):
        return (f'{self._users} ,\n'
                f'{self._events} ,\n'
                f'{self._admin}')

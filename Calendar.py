s.add_event(u)
u = s.new_user()
s = Calendar()


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
    def calendary_admin(self):


                self._events.remove(event)
            if event._name == name_event:
        for event in self._events:
        name_event = (input('Для удаления события введите его название')).strip()
''' Необходимо вставить переименование, тзменение описания, изменени списка удаление события'''
                print(event)
            if event._author_id == user._id:
        for event in self._events:
        user = self._admin
    def edit_event(self):


        self._events.append(event)
        event = Event.Event(author_id, name, description, ets, eta, period, users)
            users[self._users[j - 1]._id] = 0
        for j in n:
        users = dict()
        n = map(int, input("напишите их через запятую \n").split(","))

        print("Введите номерa пользователей, чтобы пригласить их на мероприятие \n")
            print(f' {i + 1}   {self._users[i]}   ')
        for i in range(len(self._users)):
              " N          пользователь               \n")
        print("_______________________________________\n"
                           "4 - событие ежегодное \n"))
                           "3 - событие ежемесячное\n "
                           "2 - событие еженедельное\n"
                           "1 - событие ежедневное \n"
                           "0 - событие не периодичное \n"
        period = int(input("Введите периодичность события \n"
        eta = datetime.datetime(y, m, d, h, mi, s)
        h, mi, s = map(int, input("Введите время окончания мероприятия в формате hh:mm:ss").split(":"))
        y, m, d = map(int, input("Введите дату окончания мероприятия в формате yy-mm-dd").split("-"))
        ets = datetime.datetime(y, m, d, h, mi, s)
        h, mi, s = map(int, input("Введите время начала мероприятия в формате hh:mm:ss").split(":"))
        y, m, d = map(int, input("Введите дату начала мероприятия в формате yy-mm-dd").split("-"))
        description = (input("Введите описание события: \n")).strip()
        name = (input("Введите название события: \n")).strip()
        author_id = user._id
        user = self._admin
    def add_event(self):

                    print(f'{event._author_id} удалил Вас из списка приглашенных на событие \n')
                elif event._users[user._id] == 2:
                        event.del_user(user._id, user._id)
                    elif dn == '2':
                        event._users[user._id] == 1
                    if dn == '1':
                                '2 - не внoсить событие в ваш календарь \n'))
                    dn = (input('1 - внести данное событие в ваш календарь, \n'
                    print(f'Вас приглашают на событие {event}\n')
                if event._users[user._id] == 0:
            if user._id in event._users.keys:
        for event in self._events:
        user = self._admin
    def check_welcome(self):

        return None
        print(f'Пользователя с логином {login} не существует \n')
                    return None
                    print(f'Вы ввели неверный пароль для {login} \n')
                else:
                    self._admin = user
                if password == user._password:
                password = input('Ваш пароль:')
            if login == user._login:
        for user in self._users:
        login = input('Введите ваш логин:')
    def check_user(self):  # проверка логинаf'Вас приглашают на событие {event}\n' и пароля


        self._users.append(self._admin)
        self._admin = User.User(login, password)
        password = input('Ваш пароль:')
                break
            else:
                print('Данный логин уже существует. Введите новый логин.')
            if flag == 1:
                    flag = 1
                if login == user._login:
            for user in self._users:
            login = input('Ваш логин:')
            flag = 0
        while True:
    def new_user(self):

        self._events = list()
        self._users = list()
        self._admin = User.User
    def __init__(self):

    _events = list()
    _users = list()
    _admin = User.User
class Calendar:


import User
import Event
import datetime
"""
У каждого календаря ровно один пользователь.

он умеет добавлять/удалять события.

умеет искать все события из промежутка (в том числе повторяющиеся)

Класс календаря - хранит события.
"""
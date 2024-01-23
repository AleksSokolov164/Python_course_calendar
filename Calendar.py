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
    _admin = User.User
    _users = list()
    _events = list()

    def __init__(self):
        self._admin = User.User
        self._users = list()
        self._events = list()

    def new_user(self):
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
        self._admin = User.User(login, password)
        self._users.append(self._admin)


    def check_user(self):  # проверка логина и пароля
        login = input('Введите ваш логин:')
        for user in self._users:
            if login == user._login:
                password = input('Ваш пароль:')
                if password == user._password:
                    self._admin = user
                else:
                    print(f'Вы ввели неверный пароль для {login} \n')
                    return None
        print(f'Пользователя с логином {login} не существует \n')
        return None

    def check_welcome(self):
        user = self._admin
        for event in self._events:
            if user._id in event._users.keys:
                if event._users[user._id] == 0:
                    print(f'Вас приглашают на событие {event}\n')
                    dn = (input('1 - внести данное событие в ваш календарь, \n'
                                '2 - не внoсить событие в ваш календарь \n'))
                    if dn == '1':
                        event._users[user._id] == 1
                    elif dn == '2':
                        event.del_user(user._id, user._id)

    def add_event(self):
        user = self._admin
        author_id = user._id
        name = (input("Введите название события: \n")).strip()
        description = (input("Введите описание события: \n")).strip()
        y, m, d = map(int, input("Введите дату начала мероприятия в формате yy-mm-dd").split("-"))
        h, mi, s = map(int, input("Введите время начала мероприятия в формате hh:mm:ss").split(":"))
        ets = datetime.datetime(y, m, d, h, mi, s)
        y, m, d = map(int, input("Введите дату окончания мероприятия в формате yy-mm-dd").split("-"))
        h, mi, s = map(int, input("Введите время окончания мероприятия в формате hh:mm:ss").split(":"))
        eta = datetime.datetime(y, m, d, h, mi, s)
        period = int(input("Введите периодичность события \n"
                           "0 - событие не периодичное \n"
                           "1 - событие ежедневное \n"
                           "2 - событие еженедельное\n"
                           "3 - событие ежемесячное\n "
                           "4 - событие ежегодное \n"))
        print("_______________________________________\n"
              " N          пользователь               \n")
        for i in range(len(self._users)):
            print(f' {i + 1}   {self._users[i]}   ')
        print("Введите номерa пользователей, чтобы пригласить их на мероприятие \n")

        n = map(int, input("напишите их через запятую \n").split(","))
        users = dict()
        for j in n:
            users[self._users[j - 1]._id] = 0
        event = Event.Event(author_id, name, description, ets, eta, period, users)
        self._events.append(event)


    def del_event(self):
        user = self._admin
        for event in self._events:
            if event._author_id == user._id:
                print(event)
        name_event = (input('Для удаления события введите его название')).strip()
        for event in self._events:
            if event._name == name_event:
                self._events.remove(event)


    def calendary_admin(self):
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
        for event in events1:
            print(event)


s = Calendar()
u = s.new_user()
s.add_event(u)
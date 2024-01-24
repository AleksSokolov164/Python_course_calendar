"""
Позволяет зайти по логину-паролю или создать нового пользователя (а так же выйти из аккаунта)
Позволяет выбрать календарь, узнать ближайшие события, события из промежутка времени а так же
Создать событие или удалить событие
После создания события можно добавить туда пользователей
Если нас добавили в событие или удалили мы получаем уведомление.

в main можно использовать ТОЛЬКО interface
"""

import Calendar
import User
import Event


class Interface:


    users = list()
    events = list()
    calendars = list()

    def __init__(self):
        self._users = list()
        self._calendars = list()

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
        new_user = User.User(login, password)
        calendar = Calendar.Calendar(user=new_user)
        self._users.append(new_user)
        self._calendars.append(calendar)

    def check_user(self):  # проверка логина и пароля
        login = input('Введите ваш логин:')
        for user in self._users:
            if login == user._login:
                password = input('Ваш пароль:')
                if password == user._password:
                    return user
                else:
                    print(f'Вы ввели неверный пароль для {login} \n')
                    return None
        print(f'Пользователя с логином {login} не существует \n')
        return None

    def check_welcome(self, user):
        for event in user._calendars._welcome:
            print(f'Вас приглашают на событие {event}\n')
            dn = (input('1 - внести данное событие в ваш календарь, \n'
                        '2 - не внoсить событие в ваш календарь \n'))
            if dn == '1':
                user._calendar.append_event(event)
            elif dn == '2':

    def __str__(self):
        r = ''
        for i in self.users:
            r = r + i._id + ' ' + i._login + ' ' + i._password + ', \n'

        return f'{r}'

    def add_user(self, user):
        self.users.append(user)

    def get_users(self):
        return self.users


m = Backend()
m.new_user()

u2 = User.User("login1", "password1")

m.add_user(u2)
print(m)

m.new_user()
print(m)

n1 = m.check_user()
n2 = m.check_user()
n3 = m.check_user()

print(n1, n2, n3)

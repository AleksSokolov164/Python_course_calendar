"""
Описывает некоторе "событие" - промежуток времени с присвоенными характеристиками
У события должно быть описание, название и список участников
Событие может быть единожды созданым
Или периодическим (каждый день/месяц/год/неделю)

Каждый пользователь ивента имеет свою "роль"
организатор умеет изменять названия, список участников, описание, а так же может удалить событие
участник может покинуть событие

запрос на хранение в json
Уметь создавать из json и записывать в него

Иметь покрытие тестами
Комментарии на нетривиальных методах и в целом документация
"""
import datetime


class Event:
    '''Создаем событие поэлементно: название, описание,  дата начала, дата завершения, периодичность,
     список участников'''
    _author: str = ""
    _name = ""
    _description = ""
    _ets = datetime.datetime
    _eta = datetime.datetime
    _period = dict()
    _users = list()

    def __init__(self, author, name, description, ets, eta, users, period):
        self._author = author
        self._ets = ets
        self._eta = eta
        self._name = name
        self._description = description
        self._users = users
        self._period = period

    def edit_author(self, author):
        self._author = author

    def get_author(self):
        return self._author

    def edit_name(self, new_name):
        self._name = new_name

    def edit_description(self, new_description):
        self._description = new_description

    def get_description(self):
        return self._description

    def edit_ets(self, ets):
        self._ets = ets

    def get_ets(self):
        return self._ets

    def edit_eta(self, eta):
        self._eta = eta

    def get_eta(self):
        return self._eta

    def get_timings(self):
        return self._ets, self._eta

    def edit_period(self, a, b):
        self._period = {a: b}

    def get_period(self):
        return self._period

    def add_users(self, users):
        for user in users:
            if user is not self._users:
                self._users.append(user)

    def get_users(self):
        return self._users

    def print_users(self):
        for i in self._users:
            print(i)

    def del_user(self, user):
        return self._users.remove(user)

    def __str__(self):
        return (f"Событие {self._name},\n {self._description},\n дата и время начала: {self._ets},\n "
                f"дата и время завершения: {self._eta},\n организатор события: {self._author},\n"
                f"участники: {self._users}" )

    def __repr__(self):
        return f"{self._name}"

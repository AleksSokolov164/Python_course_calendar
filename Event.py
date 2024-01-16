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

    _name = ""
    _description = ""
    _ets = datetime.datetime
    _eta = datetime.datetime
    _frequency = dict()
    _users = list()

    def __init__(self):
        self._ets = datetime.datetime
        self._eta = datetime.datetime
        self._name = ""
        self._description = ""
        self._users = list()
        self._frequency = dict()

    def edit_name(self, new_name):
        self._name = new_name

    def edit_description(self, new_description):
        self._description = new_description

    def edit_ets(self, ets):
        self._ets = ets

    def edit_eta(self, eta):
        self._eta = eta

    def edit_period(self, a, b):
        self._frequency = {a: b}

    def add_users(self, user):
        if user is not self._users:
            self._users.append(user)

    def get_timings(self):
        return self._ets, self._eta


    def get_users(self):
        return self._users

    def print_users(self):
        for i in self._users:
            print(i)

    def del_user(self, user):
        return self._users.remove(user)





    def __str__(self):
        return (f"Событие {self._name},\n {self._description},\n дата и время начала: {self._ets},\n "
                f"дата и время завершения: {self._eta}\n")
    def __repr__(self):
        return f"{self._name}"

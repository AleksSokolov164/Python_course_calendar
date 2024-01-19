"""
Пользователь - имеет логин и пароль, а так же календарь.
у пользователя есть итендифекатор начинающийся с @
"""
import Calendar


class User:

    __id_counter__ = 0

    def __init__(self, login="", password="", calendar=Calendar.Calendar()):
        self._id = "@" + str(self.__class__.__id_counter__)
        self.__class__.__id_counter__ += 1
        self._login = login
        self._password = password
        self._calendar = calendar


    def get_login(self):
        return self._login

    def get_password(self):
        return self._password

    def get_id(self):
        return self._id

    def __str__(self):
        return f" Пользователь {self._id}\n"

    def __repr__(self):
        return f"{self._id}]"

    def __hash__(self):
        return int(self._id[1:])

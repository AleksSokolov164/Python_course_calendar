"""
Пользователь - имеет логин и пароль, а так же календарь.
у пользователя есть итендифекатор начинающийся с @
"""
import Calendar


class User:
    _login = ""
    _pasword = ""
    __id_counter__ = 0
    _plan = Calendar.Calendar()
    _message = ""

    def __init__(self, login, pasword, plan):
        self._id = "@" + str(self.__class__.__id_counter__)
        self.__class__.__id_counter__ += 1
        self._login = login
        self._pasword = pasword
        self._plan = plan

    def get_login(self):
        return self._login

    def get_pasword(self):
        return self._pasword

    def get_id(self):
        return self._id

    def __str__(self):
        return f" Пользователь {self._id}\n"

    def __repr__(self):
        return f"{self._id}]"

    def __hash__(self):
        return int(self._id[1:])

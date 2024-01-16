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

    def __init__(self, login, pasword):
        self._id = "@" + str(self.__class__.__id_counter__)
        self.__class__.__id_counter__ += 1
        self._login = login
        self._pasword = pasword
        self._plan = Calendar.Calendar()

    def get_2(self):
        return self._login, self._pasword

    def get_pasword(self):
        return self._pasword

    def __str__(self):
        return f" {self._id}\n"

    def __repr__(self):
        return f"Пользователь {self._id}]"

    def __hash__(self):
        return int(self._id[1:])

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
    _author_id = ""  # организатор события
    _name = ""  # название события
    _description = ""  # описание сабытия
    _ets = datetime.datetime  # дата и время начала события
    _eta = datetime.datetime  # дата и время окончания собития
    _period = int()  # периодичность события
    _users = dict()  # список участников {@идентификатор: флаг участия} , 0 - если учстник еще не решил, 1- если участвует

    def __init__(self,
                 author_id="",
                 name="",
                 description="",
                 ets=datetime.datetime,
                 eta=datetime.datetime,
                 users=dict(),
                 period=int()):
        self._author_id = author_id
        self._ets = ets
        self._eta = eta
        self._name = name
        self._description = description
        self._users = users
        self._period = period

    def edit_name(self, new_name):
        self._name = new_name

    def get_name(self):
        return self._name

    def edit_description(self, new_description):
        self._description = new_description

    def get_description(self):
        return self._description


    def add_user(self, user_id):
        if user_id not in self._users.keys():
            self._users[user_id] = 0
        elif self._users[user_id] == 1:
            print('Данный пользователь уже приглашен и дал согласие на участие')
        else:
            print('Данный пользователь уже приглашен к участию')

    def del_user(self, user_id):
        if user_id in self._users.keys():
            del self._users[user_id]
        else:
            print('Пользователь, которого вы хотите удалить, отсутсвует в списке участников')


    def print_users(self):
        st = ''
        for i, j in self._users.items():
            st = st + f'{i} : {j}\n'
            print(st)


    def __str__(self):
        st = ''
        for i, j in self._users.items():
            st = st + f'{i} : {j}\n'
        return (f"_________________________________\n"
                f"СОБЫТИЕ {self._name},\n "
                f"ОПИСАНИЕ {self._description},\n "
                f"ДАТА И ВРЕМЯ\n   "
                f"НАЧАЛО {self._ets},\n   "
                f"ЗАВЕРШЕНИЕ {self._eta},\n "
                f"ОРГАНИЗАТОР: {self._author_id},\n "
                f"ПЕРИОДИЧНОСТЬ: {self._users}, \n"
                f"ПРИГЛАШЕННЫЕ: \n {st}\n")

    def __repr__(self):
        return f"{self._name}, {self._ets}, {self._eta}"

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
    '''_author_id = "" идентификатор, организатор события
    _name = ""   название события
    _description = "" описание сабытия
    _ets = datetime.datetime   дата и время начала события
    _eta = datetime.datetime   дата и время окончания собития
    _period = int()   периодичность события:
                     1 - событие ежедневное
                     2 - событие еженедельное
                     3 - событие ежемесячное
                     4 - событие ежегодное
    _users = dict() список участников {@идентификатор: флаг участия} ,
                                                   0 -  еще не решил,
                                                   1 - участвует,
                                                   2 - удалили из списка

      '''
    _author_id = ""
    _name = ""
    _description = ""
    _ets = datetime.datetime
    _eta = datetime.datetime
    _period = int()
    _users = dict()

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

    def edit_name(self, new_name, user_id):
        if user_id == self._author_id:
            self._name = new_name
        else:
            print('Вы не обладаете правами организатора данного события')

    def get_name(self):
        return self._name

    def edit_description(self, new_description, user_id):
        if user_id == self._author_id:
            self._description = new_description
        else:
            print('Вы не обладаете правами организатора данного события')

    def get_description(self):
        return self._description

    def add_user(self, new_user_id, user_id):
        if user_id == self._author_id:
            if new_user_id not in self._users.keys():
                self._users[new_user_id] = 0
            elif self._users[new_user_id] == 0:
                print('Данный пользователь уже приглашен к участию')
            else:
                print('Данный пользователь уже приглашен и дал согласие на участие')
        else:
            print('Вы не обладаете правами организатора данного события')

    def del_user(self, new_user_id, user_id):
        if user_id == self._author_id:
            if new_user_id in self._users.keys():
                self._users[new_user_id] = 2
            else:
                print('Пользователь, которого вы хотите удалить, отсутсвует в списке участников')
        elif new_user_id == user_id and user_id in self._users.keys():
            del self._users[user_id]
        elif user_id not in self._users.keys():
            print('Вы не обладаете правами на удаление данного участника')

    def print_users(self):
        st = ''
        for i, j in self._users.items():
            if j == 0:
                k = 'приглашен'
            else:
                k = 'принял приглашение'
            st = st + f'Пользователь: {i} - {j}\n'
            print(st)

    def __str__(self):
        if self._period == 0:
            period = 'непериодичное'
        elif self._period == 1:
            period = 'ежедневное'
        elif self._period == 2:
            period = 'еженедельное'
        elif self._period == 3:
            period = 'ежемесячное'
        elif self._period == 4:
            period = 'ежегодное'
        guests = ''
        users1 = self._users.items()
        for i,j in users1:
            if i != self._author_id:
                if j == 0:
                    guests = guests + f"{i} - приглашен "
                elif j == 1:
                    guests = guests + f"{i} - дал согласие на участие "
                elif j == 2:
                    guests = guests + f"{i} - удален из списка "

        return (f"_________________________________\n"
                f"ОРГАНИЗАТОР: {self._author_id}\n"
                f"СОБЫТИЕ {self._name}\n"
                f"ОПИСАНИЕ {self._description}\n"
                f"ДАТА И ВРЕМЯ\n"
                f"НАЧАЛО {self._ets}\n"
                f"ЗАВЕРШЕНИЕ {self._eta}\n"                
                f"ПЕРИОДИЧНОСТЬ: {period} \n"
                f"ПРИГЛАШЕННЫЕ: \n {guests}\n")

    def __repr__(self):
        return f"{self._name}, {self._users.items()}"

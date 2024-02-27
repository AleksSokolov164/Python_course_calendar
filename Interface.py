"""
Позволяет зайти по логину-паролю или создать нового пользователя (а так же выйти из аккаунта)
Позволяет выбрать календарь, узнать ближайшие события, события из промежутка времени а так же
Создать событие или удалить событие
После создания события можно добавить туда пользователей
Если нас добавили в событие или удалили мы получаем уведомление.

в main можно использовать ТОЛЬКО interface
"""
from Calendar import Calendar
import User
import Event
import datetime
import csv
import ast
import re

class Interface:
    calendar = None
    state = "start"
    func_request = list()

    @staticmethod
    def work():
        Interface.func_request = [Interface.start]

        while Interface.func_request:
            Interface.func_request[0]()
            del Interface.func_request[0]



        print("Воркер интерфейса закончил работу")

    @staticmethod
    def start():
        Interface.state = "start"
        print("Старт програмы")
        Interface.calendar = Calendar()
        Interface.func_request.append(Interface.load_user)
        Interface.func_request.append(Interface.load_calendars)
        Interface.func_request.append(Interface.read)


    @staticmethod
    def save_users():
        if Interface.calendar is None:
            return

        with open("saved_users.txt", "w", newline="") as f:
            w = csv.DictWriter(f, ["id", "login", "password"])
            w.writeheader()

            users = Interface.calendar.get_users()
            for user in users:
                data_user = dict()
                data_user["id"] = user._id
                data_user["login"] = user._login
                data_user["password"] = user._password
                w.writerow(data_user)

    @staticmethod
    def save_calendars():
        if Interface.calendar is None:
            return
        with open("saved_calendars.txt", "w", newline="") as v:
            w = csv.DictWriter(v, ["author_id", "name", "description", "ets", "eta", "users", "period"])
            w.writeheader()

            calendary = Interface.calendar.get_calendars()
            for event in calendary:
                data_event = dict()
                data_event["author_id"] = event._author_id
                data_event["name"] = event.get_name()
                data_event["description"] = event.get_description()
                data_event["ets"] = event._ets  # ФОРМАТ ДАТЫ
                data_event["eta"] = event._eta # ФОРМАТ ДАТЫ
                data_event["users"] = str(event._users)  # ФОРМАТ список\строка
                data_event["period"] = event._period
                w.writerow(data_event)

    @staticmethod
    def load_user():
        if Interface.calendar is None:
            Interface.calendar = Calendar()


        with open("saved_users.txt", "r") as f:
            w = csv.DictReader(f, ["id", "login", "password"])

            for i in w:
                if i["id"] == "id":
                    continue
                login = i["login"]
                password = i["password"]
                Interface.calendar.add_user(login, password)

    @staticmethod
    def load_calendars():
        if Interface.calendar is None:
            Interface.calendar = Calendar()

        with open("saved_calendars.txt", "r") as f:
            w = csv.DictReader(f, ["author_id", "name", "description", "ets", "eta", "users", "period"])

            for i in w:
                if i["author_id"] == "author_id":
                    continue
                author_id = i["author_id"]
                name = i["name"]
                description = i["description"]
                data_1 = i["ets"]
                data_list1 = re.findall("\d+", data_1)
                yy1 = int(data_list1[0])
                mm1 = int(data_list1[1])
                dd1 = int(data_list1[2])
                hh1 = int(data_list1[3])
                mm1 = int(data_list1[4])
                ss1 = int(data_list1[5])
                ets = datetime.datetime (yy1, mm1, dd1, hh1, mm1, ss1)
                data_2 = i["eta"]
                data_list2 = re.findall("\d+", data_2)
                yy2 = int(data_list2[0])
                mm2 = int(data_list2[1])
                dd2 = int(data_list2[2])
                hh2 = int(data_list2[3])
                mm2 = int(data_list2[4])
                ss2 = int(data_list2[5])
                eta = datetime.datetime(yy2, mm2, dd2, hh2, mm2, ss2)
                users = ast.literal_eval(i["users"])
                period = int(i["period"])
                Interface.calendar.add_event(author_id, name, description, ets, eta, users, period)


    @staticmethod
    def read():
        Interface.state = "read"
        ret = input("""
        Осуществляем вход в Календарь:
        1) зарегистрироваться
        2) войти
        3) завершить работу
        """)
        ret = int(ret)
        if ret == 1:
            Interface.func_request.append(Interface.new_user)
        elif ret == 2:
            Interface.func_request.append(Interface.check_user)
        elif ret == 3:

            Interface.func_request.append(Interface.finish)

        else:
            raise ValueError

    @staticmethod
    def new_user():
        Interface.calendar.new_user()
        Interface.func_request.append(Interface.save_users)
        Interface.func_request.append(Interface.read)




    @staticmethod
    def check_user():
        Interface.calendar.check_user()
        Interface.calendar.check_welcome()
        Interface.func_request.append(Interface.save_calendars)
        Interface.func_request.append(Interface.calendar_event)


    @staticmethod
    def calendar_event():
        ret = input("""
                Календарь:
                1) создать событие
                2) редактировать событие
                3) посмотреть календарь
                4) выйти
                """)
        ret = int(ret)
        if ret == 1:
            Interface.func_request.append(Interface.add)
        elif ret == 2:
            Interface.func_request.append(Interface.edit)
        elif ret == 3:
            Interface.func_request.append(Interface.calendary)
        elif ret == 4:
            Interface.func_request.append(Interface.read)
        else:
            raise ValueError


    @staticmethod
    def add():
        Interface.calendar.new_event()
        Interface.func_request.append(Interface.save_calendars)
        Interface.func_request.append(Interface.calendar_event)


    @staticmethod
    def edit():
        Interface.calendar.edit_events()
        Interface.func_request.append(Interface.save_calendars)
        Interface.func_request.append(Interface.calendar_event)


    @staticmethod
    def calendary():
        Interface.calendar.calendary_admin()
        Interface.func_request.append(Interface.calendar_event)




    @staticmethod
    def finish():
        pass


Interface.work()

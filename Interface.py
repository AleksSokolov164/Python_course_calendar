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

            print(Interface.func_request)

        print("Воркер интерфейса закончил работу")

    @staticmethod
    def start():
        Interface.state = "start"
        print("Старт програмы")
        Interface.calendar = Calendar()
        # Interface.func_request.append(Interface.load_state)
        Interface.func_request.append(Interface.read)

    # @staticmethod
    # def save_state():
    #     if Interface.calendar is None:
    #         return
    #     with open("saved_data.txt", "w", newline="") as f:
    #         w = csv.DictWriter(f, ["from", "to", "start", "end"])
    #         w.writeheader()
    #
    #         routs = Interface.calendar.get_routs()
    #         for point in routs:
    #             for r in routs[point]:
    #                 data = dict()
    #                 data["from"], data["to"] = r.get_points()
    #                 data["from"] = data["from"].get_name()
    #                 data["to"] = data["to"].get_name()
    #                 data["start"], data["end"] = r.get_timings()
    #                 w.writerow(data)
    #
    # @staticmethod
    # def load_state():
    #     if Interface.calendar is None:
    #         Interface.calendar = Calendar()
    #
    #     hubs = dict()
    #     with open("saved_data.txt", "r") as f:
    #         w = csv.DictReader(f, ["from", "to", "start", "end"])
    #
    #         for i in w:
    #             if i["from"] == "from":
    #                 continue
    #
    #             if i["from"] not in hubs:
    #                 hubs[i["from"]] = Hub.Hub(i["from"])
    #             if i["to"] not in hubs:
    #                 hubs[i["to"]] = Hub.Hub(i["to"])
    #
    #             h, m, s = map(int, i["start"].split(":"))
    #             a_time = datetime.time(hour=h, minute=m, second=s)
    #             h, m, s = map(int, i["end"].split(":"))
    #             b_time = datetime.time(hour=h, minute=m, second=s)
    #
    #             r = Route.Route(hubs[i["from"]], hubs[i["to"]], a_time, b_time)
    #
    #             Interface.calendar.add_route(r)
    #
    #     print(Interface.calendar)

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
        Interface.func_request.append(Interface.read)
        #Interface.save_state()

    @staticmethod
    def check_user():
        Interface.calendar.check_user()
        Interface.calendar.check_welcome()

        Interface.func_request.append(Interface.calendar_event)
       # Interface.save_state()

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
        Interface.calendar.add_event()
        Interface.func_request.append(Interface.calendar_event)

    @staticmethod
    def edit():
        Interface.calendar.edit_events()
        Interface.func_request.append(Interface.calendar_event)

    @staticmethod
    def calendary():
        Interface.calendar.calendary_admin()
        Interface.func_request.append(Interface.calendar_event)



    @staticmethod
    def finish():
        pass


Interface.work()

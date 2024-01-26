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
        print("Старт програмы путей")
        Interface.calendar = Calendar()
        Interface.func_request.append(Interface.load_state)
        Interface.func_request.append(Interface.read)

    @staticmethod
    def save_state():
        if Interface.calendar is None:
            return
        with open("saved_data.txt", "w", newline="") as f:
            w = csv.DictWriter(f, ["from", "to", "start", "end"])
            w.writeheader()

            routs = Interface.calendar.get_routs()
            for point in routs:
                for r in routs[point]:
                    data = dict()
                    data["from"], data["to"] = r.get_points()
                    data["from"] = data["from"].get_name()
                    data["to"] = data["to"].get_name()
                    data["start"], data["end"] = r.get_timings()
                    w.writerow(data)

    @staticmethod
    def load_state():
        if Interface.calendar is None:
            Interface.calendar = Calendar()

        hubs = dict()
        with open("saved_data.txt", "r") as f:
            w = csv.DictReader(f, ["from", "to", "start", "end"])

            for i in w:
                if i["from"] == "from":
                    continue

                if i["from"] not in hubs:
                    hubs[i["from"]] = Hub.Hub(i["from"])
                if i["to"] not in hubs:
                    hubs[i["to"]] = Hub.Hub(i["to"])

                h, m, s = map(int, i["start"].split(":"))
                a_time = datetime.time(hour=h, minute=m, second=s)
                h, m, s = map(int, i["end"].split(":"))
                b_time = datetime.time(hour=h, minute=m, second=s)

                r = Route.Route(hubs[i["from"]], hubs[i["to"]], a_time, b_time)

                Interface.calendar.add_route(r)

        print(Interface.calendar)

    @staticmethod
    def read():
        Interface.state = "read"
        ret = input("""
        Производим построение графа:
        0) создать новую вершину
        1) создать новое ребро
        2) удалить вершину
        3) удалить ребро
        4) завершить редактирование графа
        """)
        ret = int(ret)
        if ret == 0:
            Interface.func_request.append(Interface.create_point)
        elif ret == 1:
            Interface.func_request.append(Interface.create_edge)
        elif ret == 4:
            Interface.func_request.append(Interface.request)
        else:
            raise ValueError

    @staticmethod
    def create_point():
        name = input("Введите имя точки: ")
        h = Hub.Hub(name)
        Interface.calendar.add_point(h)
        Interface.func_request.append(Interface.read)
        Interface.save_state()

    @staticmethod
    def create_edge():
        print("Уже существующие точки:")
        points = list(Interface.calendar.get_points())
        for i, p in enumerate(points):
            print(f"{i}) {p.get_name()}")

        a = int(input("Введите номер стартовой точки: "))
        b = int(input("Введите номер конечной точки: "))

        h, m, s = map(int, input("Введите время отбытия в формате: hh-mm-ss").split("-"))
        a_time = datetime.time(hour=h, minute=m, second=s)
        h, m, s = map(int, input("Введите время прибытия в формате: hh-mm-ss").split("-"))
        b_time = datetime.time(hour=h, minute=m, second=s)

        r = Route.Route(points[a], points[b], a_time, b_time)
        Interface.calendar.add_route(r)
        Interface.func_request.append(Interface.read)
        Interface.save_state()

    @staticmethod
    def delete_point():
        pass

    @staticmethod
    def delete_edge():
        pass

    @staticmethod
    def request():
        Interface.state = "request"
        ret = input("""
        Граф готов к запросам:
        0) создать новый зарос
        1) вернуться к редактированию
        2) завершить работу
        """)
        ret = int(ret)
        if ret == 0:
            Interface.func_request.append(Interface.create_request)
        elif ret == 1:
            Interface.func_request.append(Interface.read)
        elif ret == 2:
            Interface.func_request.append(Interface.finish)
        else:
            raise ValueError

    @staticmethod
    def create_request():

        print(Interface.calendar)

        print("Уже существующие точки:")
        points = list(Interface.calendar.get_points())
        for i, p in enumerate(points):
            print(f"{i}) {p.get_name()}")

        a = int(input("Введите номер стартовой точки: "))
        b = int(input("Введите номер конечной точки: "))

        h, m, s = map(int, input("Введите время отбытия в формате: hh-mm-ss").split("-"))
        a_time = datetime.time(hour=h, minute=m, second=s)
        h, m, s = map(int, input("Введите время прибытия в формате: hh-mm-ss").split("-"))
        b_time = datetime.time(hour=h, minute=m, second=s)



        routes = Interface.calendar.find_fastest_route(points[a], points[b], a_time, b_time)

        if routes is not None:
            print("Построен кратчайший маршрут:")
            for i in routes:
                print(routes)
        else:
            print("Путь не существует")

        Interface.func_request.append(Interface.request)

    @staticmethod
    def finish():
        pass


Interface.work()

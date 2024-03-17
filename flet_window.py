import flet as ft
import User
import Event
import datetime
import csv
import ast
import re


def main(page):
    users = dict()
    events = list()

    def print_event(event):
        if event._period == 0:
            period = 'непериодичное'
        elif event._period == 1:
            period = 'ежедневное'
        elif event._period == 2:
            period = 'еженедельное'
        elif event._period == 3:
            period = 'ежемесячное'
        elif event._period == 4:
            period = 'ежегодное'
        guests = ''
        users1 = event._users.items()
        for i,j in users1:
            if i != event._author_id:
                if j == 0:
                    guests = guests + f"{i} - приглашен "
                elif j == 1:
                    guests = guests + f"{i} - дал согласие на участие "
                elif j == 2:
                    guests = guests + f"{i} - удален из списка "

        return (f"_________________________________\n"
                f"ОРГАНИЗАТОР: {event._author_id}\n"
                f"СОБЫТИЕ {event._name}\n"
                f"ОПИСАНИЕ {event._description}\n"
                f"ДАТА И ВРЕМЯ\n"
                f"НАЧАЛО {event._ets}\n"
                f"ЗАВЕРШЕНИЕ {event._eta}\n"                
                f"ПЕРИОДИЧНОСТЬ: {period} \n"
                f"ПРИГЛАШЕННЫЕ: \n {guests}\n")

    def load_users():
        with open("saved_users.txt", "r") as f:
            w = csv.DictReader(f, ["id", "login", "password"])

            for i in w:
                if i["id"] == "id":
                    continue
                login = i["login"]
                password = i["password"]
                user = User.User(login=login, password=password)
                users[login] = user

    load_users()

    def saved_users():
        with open("saved_users.txt", "w", newline="") as f:
            w = csv.DictWriter(f, ["id", "login", "password"])
            w.writeheader()

            for login1 in users:
                data_user = dict()
                data_user["id"] = users[login1]._id
                data_user["login"] = users[login1]._login
                data_user["password"] = users[login1]._password
                w.writerow(data_user)
    def load_calendars():
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
                ets = datetime.datetime(yy1, mm1, dd1, hh1, mm1, ss1)
                data_2 = i["eta"]
                data_list2 = re.findall("\d+", data_2)
                yy2 = int(data_list2[0])
                mm2 = int(data_list2[1])
                dd2 = int(data_list2[2])
                hh2 = int(data_list2[3])
                mm2 = int(data_list2[4])
                ss2 = int(data_list2[5])
                eta = datetime.datetime(yy2, mm2, dd2, hh2, mm2, ss2)
                users1 = eval(i["users"])
                period = int(i["period"])
                event = Event.Event(author_id, name, description, ets, eta, users1, period)
                events.append(event)

    load_calendars()
    print(events)

    def saved_calendars():
        with open("saved_calendars.txt", "w", newline="") as v:
            w = csv.DictWriter(v, ["author_id", "name", "description", "ets", "eta", "users", "period"])
            w.writeheader()

            for event in events:
                data_event = dict()
                data_event["author_id"] = event._author_id
                data_event["name"] = event.get_name()
                data_event["description"] = event.get_description()
                data_event["ets"] = event._ets  # ФОРМАТ ДАТЫ
                data_event["eta"] = event._eta # ФОРМАТ ДАТЫ
                data_event["users"] = str(event._users)  # ФОРМАТ список\строка
                data_event["period"] = event._period
                w.writerow(data_event)
    n_event = ft.Text("")
    def password_click_authorization(e):
        if txt_password.value == users[txt_login.value].get_password():
            row2.visible = not row2.visible
            user = users[txt_login.value]
            for i in range(len(events)):
                event_control = 0
                if events[i]._author_id != user._id:
                    if user._id in events[i]._users.keys():
                        if events[i]._users[user._id] == 0:
                            n_event.value = str(i)
                            event_control = 1
                            text_welcome1 = ft.Text(f"Вас приглашают принять участие в событии:")
                            text_event1 = ft.Text(print_event(events[i]))
                            click_11 = ft.ElevatedButton("Внести данное событие в ваш календарь",
                                                         on_click=next1)
                            click_12 = ft.ElevatedButton("Не внoсить событие в ваш календарь",
                                                         on_click=next1)
                            row66 = ft.Row([click_11, click_12])
                            row6 = ft.Column([text_welcome1, text_event1, row66])
                            break
                        elif events[i]._users[user._id] == 2:
                            event_control = 2
                            text_welcome2 = ft.Text(f"Вас исключили из списка участников событи:")
                            text_event2 = ft.Text(print_event(events[i]))
                            del events[i]._users[user._id]
                            saved_calendars()
                            print(events)
                            click_13 = ft.ElevatedButton("Далее", on_click=password_click_authorization)
                            row7 = ft.Column([text_welcome2, text_event2, click_13])
                            break
            if event_control == 1:
                page.add(row6)
            elif event_control == 2:
                page.add(row7)
            else:
                page.add(row5)
        else:
            txt_password.error_text = "Пароль не подходит"
            page.update()
    def next1(e):
        user = users[txt_login.value]
        events[int(n_event.value)]._users[user._id] = 1
        saved_calendars()
        page.controls.pop(0)
        page.update()
        password_click_authorization(e)

    def next2(e):
        user = users[txt_login.value]
        del events[int(n_event.value)]._users[user._id]
        saved_calendars()
        page.controls.pop(0)
        page.update()
        password_click_authorization(e)

    def login_click_authorization(e):
        if txt_login.value in users.keys():
            row1.visible = not row1.visible
            page.add(row2)
        else:
            txt_login.error_text = "Такой логин отсутствует"
            page.update()

    def authorization_click(e):
        row0.visible = not row0.visible
        page.add(row1)

    def password_click_registration(e):
        password_registration.value = txt_password_registration.value
        user_registration = User.User(login=login_registration.value, password=password_registration.value)
        users[login_registration.value] = user_registration
        saved_users()
        row4.visible = not row4.visible
        row0.visible = not row0.visible
        page.add(row0)
        page.update()


    def login_click_registration(e):
        if txt_login_registration.value in users.keys():
            txt_login_registration.error_text = "Такой логин уже существует"
            page.update()
        else:
            login_registration.value = txt_login_registration.value
            row3.visible = not row3.visible
            page.add(row4)


    def registration_click(e):
        row0.visible = not row0.visible
        page.add(row3)


    login_registration = ft.Text("")
    password_registration = ft.Text("")


    click_1 = ft.ElevatedButton("Авторизация", on_click=authorization_click)
    click_2 = ft.ElevatedButton("Регистрация", on_click=registration_click)

    row0 = (ft.Column([click_1, click_2]))

    txt_login = ft.TextField(label="Введите ваш логин")
    click_3 = ft.ElevatedButton("Ввод", on_click=login_click_authorization)
    txt_password = ft.TextField(label="Введите ваш пароль")
    click_4 = ft.ElevatedButton("Ввод", on_click=password_click_authorization)

    row1 = ft.Row([txt_login, click_3])
    row2 = ft.Row([txt_password, click_4])

    txt_login_registration = ft.TextField(label="Введите ваш логин")
    click_5 = ft.ElevatedButton("Ввод", on_click=login_click_registration)
    txt_password_registration = ft.TextField(label="Введите ваш пароль")
    click_6 = ft.ElevatedButton("Ввод", on_click=password_click_registration)

    row3 = ft.Row([txt_login_registration, click_5])
    row4 = ft.Row([txt_password_registration, click_6])

    click_7 = ft.ElevatedButton("Cоздать событие", on_click=authorization_click)
    click_8 = ft.ElevatedButton("Редактировать событие", on_click=registration_click)
    click_9 = ft.ElevatedButton("Посмотреть календарь", on_click=registration_click)
    click_10 = ft.ElevatedButton("Выйти", on_click=registration_click)

    row5 = ft.Column([click_7, click_8, click_9, click_10])

    page.add(row0)


ft.app(target=main)


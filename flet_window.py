import flet as ft
import User
import csv


def main(page):
    users = dict()

    with open("saved_users.txt", "r") as f:
        w = csv.DictReader(f, ["id", "login", "password"])

        for i in w:
            if i["id"] == "id":
                continue
            login = i["login"]
            password = i["password"]
            user = User.User(login=login, password=password)
            users[login] = user

    def password_click_authorization(e):
        if txt_password.value == users[txt_login.value].get_password():
            row2.visible = not row2.visible
            page.add(row0)
        else:
            txt_password.error_text = "Пароль не подходит"
            page.update()

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
        user_registration = User.User(login= login_registration.value, password=password_registration.value)
        users[login_registration.value] = user_registration
        with open("saved_users.txt", "w", newline="") as f:
            w = csv.DictWriter(f, ["id", "login", "password"])
            w.writeheader()

            for login1 in users:
                data_user = dict()
                data_user["id"] = users[login1]._id
                data_user["login"] = users[login1]._login
                data_user["password"] = users[login1]._password
                w.writerow(data_user)
        row4.visible = not row4.visible
        page.add(row0)


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


    txt_login = ft.TextField(label="Введите ваш логин")
    click_3 = ft.ElevatedButton("Ввод", on_click=login_click_authorization)
    txt_password = ft.TextField(label="Введите ваш пароль")
    click_4 = ft.ElevatedButton("Ввод", on_click=password_click_authorization)

    login_registration = ft.Text("")
    password_registration = ft.Text("")


    click_1 = ft.ElevatedButton("Авторизация", on_click=authorization_click)
    click_2 = ft.ElevatedButton("Регистрация", on_click=registration_click)

    row0 = (ft.Column([click_1, click_2]))
    row1 = ft.Row([txt_login, click_3])
    row2 = ft.Row([txt_password, click_4])

    txt_login_registration = ft.TextField(label="Введите ваш логин")
    click_5 = ft.ElevatedButton("Ввод", on_click=login_click_registration)
    txt_password_registration = ft.TextField(label="Введите ваш пароль")
    click_6 = ft.ElevatedButton("Ввод", on_click=password_click_registration)

    row3 = ft.Row([txt_login_registration, click_5])
    row4 = ft.Row([txt_password_registration, click_6])

    page.add(row0)


ft.app(target=main)

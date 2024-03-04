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

    def password_click(e):
        if txt_password.value == users[txt_login.value].get_password():
            row2.visible = not row2.visible
            page.add(txt_end)
        else:
            txt_password.error_text = "Пароль не подходит"
            page.update()

    def login_click(e):
        if txt_login.value in users.keys():
            row1.visible = not row1.visible
            page.add(row2)
        else:
            txt_login.error_text = "Такой логин отсутствует"
            page.update()

    txt_login = ft.TextField(label="Введите ваш логин")
    click_1 = ft.ElevatedButton("Ввод", on_click=login_click)
    txt_password = ft.TextField(label="Введите ваш пароль")
    click_2 = ft.ElevatedButton("Ввод", on_click=password_click)

    txt_end = ft.Text("Вы прошли авторизацию")

    row1 = ft.Row([txt_login, click_1])
    row2 = ft.Row([txt_password, click_2])

    page.add(row1)


ft.app(target=main)

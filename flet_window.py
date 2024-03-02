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

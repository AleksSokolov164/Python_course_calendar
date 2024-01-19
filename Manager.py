import Calendar
import User



class Manager:
    users = list()
    calendars = dict()

    def __init__(self):
        self.users = list()
        self.calendars = dict()  # {user_id = calendar}

    def new_user(self):
        while True:
            login = input('Ваш логин:')
            flag = 0
            for user in self.users:
                if login == user._login:
                    flag = 1
            if flag == 0:
                break
            else:
                print('Данный логин уже существует. Введите новый логин.')
        password = input('Ваш пароль:')
        calendar = Calendar.Calendar()
        new_user = User.User(login, password, calendar)
        self.users.append(new_user)
        self.calendars[new_user._id] = new_user._calendar

    def __str__(self):
        r = ''
        for i in self.users:
            r = r + i._id + ', \n'

        return f'{r}'

    def add_user(self, user):
        self.users.append(user)

    def get_users(self):
        return self.users



m = Manager()
m.new_user()
u1 = User.User("login1" , "password=")
m.add_user(u1)
print(m)

m.new_user()
print(m)

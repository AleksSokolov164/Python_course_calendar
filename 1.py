import re
just = '2012-11-10 09:08:01'
price = re.findall("\d+", just)
print(price)



# import ast
# sd = ast.literal_eval("{'muffin' : 'lolz', 'foo' : 'kitty'}")
# print(sd['muffin'])
#
#
#
#
#
# n_users = map(int, input("напишите их через запятую \n").split(","))
# print(n_users)
# for i in n_users:
#     print(i)
#
#
#
# st = '0 '
# i = '1'
# j = '2'
# st = st + f'{i} : {j}\n 0'
#
#
# k = [1,2]
# g = [3,4]
#

#
#
# d = {"@1": (1, 2)}
# if (1, 2) in d.values():
#     print('i')
#
# users = ['1', '2', '3']
#
# while True:
#     login = input('Ваш логин:')
#     flag = 0
#     for user in users:
#         if login == user:
#             flag = 1
#     if flag == 0:
#         print(login)
#         break
#     else:
#         print('Данный логин уже существует. Введите новый логин.')

#
# import datetime
#
# d = datetime.datetime(2017, 12, 26, 22, 21,15)
# print(d)
# t = datetime.timedelta(days=365)
# print(t)
#
# print(d + t)
#
# d = datetime.date(2012, 12, 14)
#
# print(d.year)  # 2012
# print(d.day)  # 14
# print(d.month)
#
# now = datetime.datetime.now()
#
#
#
# # Кол-во времени между датами.
# delta = now - t
#
# print(delta)  # 38
# print(delta.second)  # 1131

#
# datetime.datetime(2017, 3, 5, 12, 30, 10)
# print(b)  # datetime.datetime(2017, 3, 5, 12, 30, 10)
#
# d = datetime.datetime(2017, 3, 5, 12, 30, 10)
# print(d.year)  # 2017
# print(d.day)
# print(d.second)  # 10
# print(d.hour)  # 12
#
# a = ([[1,2,3],[5,3,2],[1,5,3],[1,3,4]])
# a.sort()
#
# a = int(input('Введите 0 если событие не периодично и 1 если периодично'))
#         b = 0
#         if a == 1:
#             print("Введите периодичность: \n"
#                   "1 - событие ежедневное \n"
#                   "2 - событие еженедельное\n"
#                   "3 - событие ежемесячное\n "
#                   "4 - событие ежегодное"
#                   )
#             b = int(input())
# print(a)
#
# print(datetime.datetime(2024, 1, 1, 00, 00, 21) == "2024-01-01 00:00:21")


# f"______________________________________\n"
#           "{i._author_id}\n"
#           "{i._name}\n"
#           "{i._description}\n"
#           "{i._ets}\n"
#           "{i._eta}\n"
#           "{i._period}\n"
#           "{i._users}\n"
#           "______________________________________\n"

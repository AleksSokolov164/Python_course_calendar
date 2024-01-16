
import datetime

d = datetime.datetime(2017, 12, 26, 22, 21,15)
print(d)
t = datetime.datetime(d.year, (d.month + 1)%12, d.day , 22, 21,15)
print(t)
d = datetime.date(2012, 12, 14)

print(d.year)  # 2012
print(d.day)  # 14
print(d.month)

now = datetime.datetime.now()



# Кол-во времени между датами.
delta = now - t

print(delta)  # 38
print(delta.seconds)  # 1131

#
# b = datetime.datetime(2017, 3, 5, 12, 30, 10)
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
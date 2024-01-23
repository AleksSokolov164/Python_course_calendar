import Event
import datetime
import Calendar
import unittest

c = Calendar.Calendar()
x1 = datetime.datetime(2023, 12, 31, 23, 59, 59)
y1 = datetime.datetime(2024, 1, 1, 00, 00, 1)

print(c)
ev1 = Event.Event("@1", 'Новый год', 'Ёлка, семья, Дед. Мороз и подарки', x1, y1, [1, 1, 1], 4)
c.append_event(ev1)
print(c)
x2 = datetime.datetime(2024, 1, 13, 23, 59, 59)
y2 = datetime.datetime(2024, 1, 14, 00, 00, 1)
c.add_event("@2", "Старый Новый год", "Ёллллка", x2, y2, [1, 1, 1], 2)
print(c)
x4 = datetime.datetime(2024, 1, 1, 00, 00, 10)
y4 = datetime.datetime(2024, 1, 1, 22, 59, 59)
c.add_event("@3", "ДР", "Нет Ёллллка", x4, y4, [1, 1, 1], 1)
print(c)

x3 = datetime.datetime(2024, 1, 1, 00, 00, 10)
y3 = datetime.datetime(2024, 1, 7, 23, 00, 10)
c.calendary_admin(x3, y3)
for i in c.calendary_admin(x3, y3):
    print(i)


# class TestCalendar(unittest.TestCase):
#
#     def test_search_events(self):
#
#
# if __name__ == '__main__':
#     unittest.main(argv=['first-arg-is-ignored'], exit=False)

users = {
    "Alice": "active",
    "Bob": "inactive",
    "Charlie": "active",
    "Dave": "inactive",
}

for word, status in users.copy().items():
    if status == "inactive":
        del users[word]
print(users)


numbers = [1, 2, 3, 4, 5]
for index, element in enumerate(numbers):
    numbers[index] = element+10
print(numbers)
#enumerate кладет сслылки на значения списка


numbers = [1, 2, 3, 4, 5, 6]
for i in range(len(numbers)-1, -1, -1):
    if numbers[i]%2==0:
        del numbers[i]
print(numbers)
numbers = [1, 2, 3, 4, 5, 6]
numbers = [x for x in numbers if x%2!=0]
print(numbers)
numbers = [1, 2, 3, 4, 5, 6]
for x in numbers[:]:
    if x % 2 == 0:
        numbers.remove(x)
print(numbers)

"""
"""


point = (0, 7)

match point:
    case (0, y):
        result = f"Y={y}"
    case (x, 0):
        result = f"X={x}"
    case (x, y):
        result = f"{x=}, {y=}"

"""
Сработает case (0, y)
Появятся y которому присвоен 7
result равен "Y=7"
"""

data = (1, 2, 3)

match data:
    case (x, y):
        result = "two"
    case _:
        result = "other"
"""
Первый case не сработает потому что в data 3 элемента
а в case 2 элемента
В result будет "other"
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(0, 5)

match p:
    case Point(x=0, y=y):
        result = y
    case _:
        result = None
"""
Да создается и присовен p - внутри match нет
result = 5
Потому что шаблон проверяет что x==0 и присвает y 5
"""

match p:
    case Point(0, y):
        result = y
"""
Нет
Потому что не знаю
незнаю
"""



















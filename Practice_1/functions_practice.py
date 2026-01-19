def square (a: int) -> int:
	return a**2
print(square(4))   # 16
print(square(-3))  # 9

def log(message: str) -> None:
	print(message)
result = log("hello")
print(result)
#Потому что нет return, поэтому функция по умолчанию выводит None

def normalize_name(name: str) -> str:
    if name is None:
    	return "Unknown"
    else:
    	return name.capitalize()
print(normalize_name("прИвет"))

'''
'''
def user_info(name, age, city="Unknown"):
    ...
'''
name and age обязательные
city необязательный
допустимы след вызовы:
	user_info(1,2)
	user_info(name=2,age=1,city="kazan")
	user_info(age=1,name=2)
	user_info(1,age=2)
недопустимы след вызовы:
	user_info()
	user_info(city="kazan",1)
	user_info(name=2,1)
	user_info(1)
	user_info(1,1,1,1)
'''

user_info("Kamil", 19) # да 
user_info("Kamil", age=19) # да
user_info(age=19, name="Kamil") #да
user_info("Kamil", 19, "Kazan") #да
#user_info(name="Kamil", 19) #нет тут лучше использовать просто kamil

'''
def f(a, *args):
    print(a, args)
f(1, 2, 3)# 1, (2,3)
f(a=1)#1, ()
f(1)#1, ()
'''
#f(a=1, 2, 3)# Ошибка a=1 именнованный арг должен до позиционного  

def send_email(to, subject="No subject", body=""):
    print(body)


'''
'''

def debug(*args):
    print(args)

debug()
debug(1)
debug(1, 2, 3)
'''
args это название переменной
*args - это функция которая которая принимает позиционные аргументы и хранит ссылку на кортеж в котором ссылки на эти аргументы
потому что так описана функция. Кортеж обеспечивает хранение данных без изменений элементов
'''

def debug(a, *args):
    print("a:", a)
    print("args:", args)
debug(10)
debug(10, 20, 30)
'''
потому что в первом вызове debug а присвоена 10 и 
во втором вызове тоже a=10, args = (20,30)
'''
#debug(a=10, 20)
# ошибка позиционный аргумент не может идти после именновоного


def sum_all(*numbers: int) -> int:
	if len(numbers) == 0:
		return 0
	else:
		return sum(numbers)

print(sum_all(10,20,100,-1))

'''
'''

def show(**kwargs):
    print(kwargs)
show(a=1, b=2)
show()
'''
Тип kwargs - словарь
ключи это названия переменных в аргументе
'''
def show(a, **kwargs):
    print("a:", a)
    print("kwargs:", kwargs)

show(1, x=10, y=20)
#потому что x и y помещены в словарь в виде ключей

def show(a):
    pass

#show(a=1, b=2)
#я жду ошибку что функция не принимает аргумент b=1
#Потому что в описании функции не описан параметр b или **kwargs

def view(request, **kwargs):
    print(request)
    pk = kwargs.get('pk')
    if 'pk' is None:
    	print('no pk')
    else:
    	print(pk)
view(1, pk =2)

'''
'''

def add(a, b):
    return a + b

values = (2, 3)
print(add(*values))
#add(values) — ошибка потому, что функция не может принять множество, она принимает 2 аргумента
#add(*values) работает, потому что * раскрывает множество и передает элементы в аргументы функции

def f(a,b):
	print(a,b)
f(*[1, 2])#
f(*(1, 2))#Это set?
f(*range(2))#
f(*"hi")#Потому что строка это список из символов

def user(name, age):
    print(name, age)

data = {"name": "Kamil", "age": 19}
user(**data)
'''
python распаковал data в такой вид 'name'='Kamil','age'=19
передал как именнованные аргументы в вызов
'''

'''
'''

def _(x):
	return x*2

nums = [5, 1, 4, 2]
nums.sort(key=lambda x: x)
#key присвоена lambda и поиск происходит по элементам

pairs = [(1, "one"), (2, "two"), (3, "three")]
pairs.sort(key=lambda p: p[1])

'''
p это кортеж
lambda возвращает второй элемент кортежа
список сортируется по второму элементу каждого кортежа
'''

users = [
    {"name": "Kamil", "age": 18},
    {"name": "Amina", "age": 21},
    {"name": "Ilya", "age": 25},
]
users.sort(key=lambda p: (p["age"], p["name"]))

print(users)

leads = [
    {"id": 3, "name": "Dina", "score": 70},
    {"id": 1, "name": "Kamil", "score": 85},
    {"id": 2, "name": "Amina", "score": 85},
]
leads.sort(key=lambda p: (-p["score"], p["name"]))
print(leads)
















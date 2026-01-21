#5.1
a = [1, 2]
a.append((3, 4))
a.extend((5, 6))
#[1,2,3,4]
#не знаю. Внутри extend кортеж он врядли превратиться в список

a = [1]
a.append("hi")
print(a)
#Потому что extend добавляет элементы итерируемого объекта в список
#А append добавляет не знаю. Я сбился. Я не знаю отличий expend append

a = [10]
a.extend({True, 1, 2, 3})
print(a)
#Порядок стабильный.Но не знаю почему

a = [1, 2, 3]
i = len(a) + 1
a.insert(i, 99)
print(a)
#insert заменяет элемент по идексу. Но если 2-й аргумент вышел за достимый идекс(до 0 и после len()-1)
#То insert добавит элемент либо в начало и сдвинет элементы списка или добавит его в конец

a = [3, "10", 2, "1"]
try:
	a.sort()
except Exception as e:
	print("Тип ошибки:", type(e).__name__)
	print("Текст ошибки:", e)
a.sort(key=str)
print(a)
a.sort(key=int)
print(a)

raw = ["  python", "Django ", "django", "", "  ", "API", "api"]
def normalize_tags(raw: list[str]) -> list[str]:
	cleaned = [arg.strip().lower() for arg in raw if arg.strip()]
	result =[]
	for x in cleaned:
		if x not in result:
			result.append(x)
	'''
	[result.append(x) for x in cleaned if x not in result]
	'''
	return result
print(normalize_tags(raw))













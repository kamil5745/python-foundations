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

'''
'''
lst = list()
lst.append('a')
lst.append('b')
lst.append('c')
#lst.extend("abc")
lst.pop()
lst.pop()
print(lst)

'''
def is_balanced(s: str) -> bool:
	if len(s) == 0:
		return True
	if len(s)%2 != 0 or s[0] == ")" or s[len(s)-1] == "(":
		return False
	pair_scob = 0
	for now_scob in s:
		if now_scob == '(':
			pair_scob += 1
		if now_scob == ')':
			pair_scob -= 1
	if pair_scob == 0:
		return True
	else:
		return False
'''
def is_balanced(s: str) -> bool:
	stack = []
	for el in s:
		if el == "(":
			stack.append(el)
		elif el == ')':
			if not stack:
				return False
			stack.pop()
	return not stack
print(is_balanced("()))((()"))

lst = [1,2,3,"4", "5", '6', True, []]
print(lst)
print(lst.pop())
print(lst)
print(lst.pop(0))
print(lst)
# при pop() удаляется последний элемент и возвращатся pop, при это эл-ты списка не переписывается
# при pop(0) удаляется ссылка - первый элемент из списка и остальные ссылки элементы списка все переписываются на предыдущий индекс


history = ['']

def type_text(t: str) -> None:
	history.append(history[-1] + t)

def undo() -> None:
	if len(history) > 1:
		history.pop()

def print_text() -> None:
	print(history[-1])

type_text("Hello")
print_text()        # Hello
type_text(" world")
print_text()        # Hello world
undo()
print_text()        # Hello
print(history)




















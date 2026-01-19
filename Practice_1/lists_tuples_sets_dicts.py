'''
words = {"short": "Гоша", "long": "Георгий"}
items = [5, "Stroka", True, 5.23, 7, 1, False, 0, ()] #Список (изм, добавл, элем не ориг)
items.append("Привет")
unique = set(items) #Множество (элем ориг, изм, добавл)
print(words["long"]+"\n", items, unique)
'''
'''
items = [5, "Stroka", True, 5.23, 7]
items.append("Привет")
b = [5, 8, 1, 9, 6]
items.extend(b)
items.remove(5)
items.remove(5)
items.pop(0)
b.reverse()
b.clear()
items.extend([6, 2, 9, True])
'''

'''
items = [0,1,2,3,4,5,6,7,8,9]
a = items[::3]
b = items[::-1]
c = items[1::2]
print(a,b,c)
'''
'''
t = (10, 20, 30)
lst = list(t)
lst.extend([40,50])
t = tuple(lst)
print(t)
'''
'''
nums = [1, 1, 2, 3, 3, 3, 4, True]
mnozhestvo = set(nums)
#Потому что хеш 1 и True одинаковый и поэтому одна ячейка в внутреннем массиве
l = len(mnozhestvo)
print(l, mnozhestvo)
'''

words = {"short": "Гоша", "middle": "Гера", "long": "Георгий"}
print(words["long"])
for a,b in enumerate(words):
	if b == "middle":
		print(words[b])
print(words.get("middle"))



















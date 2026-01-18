if "":
	print("Истинно подобное")
else:
	print("Ложно подобное")

if 0:
	print("Истинно подобное")
else:
	print("Ложно подобное")

if 0.0:
	print("Истинно подобное")
else:
	print("Ложно подобное")

if None:
	print("Истинно подобное")
else:
	print("Ложно подобное")

if []:
	print("Истинно подобное")
else:
	print("Ложно подобное")

if {}:
	print("Истинно подобное")
else:
	print("Ложно подобное")

if ():
	print("Истинно подобное")
else:
	print("Ложно подобное")
tests = ["", "0", 0, 0.0, -0.0, None, [], [0], {}, {"a": 0}, (), (0,), set(), {0}]
for x in tests:
    print(repr(x), "->", bool(x))

print(bool("0"))      # строка НЕ пустая -> True
print(bool(" "))      # пробел — тоже True
print(bool("\n"))     # перевод строки — True
print(bool("False"))  # строка — True

print(bool([0]))      # True
print(bool([False]))  # True
print(bool([None]))   # True
print(bool({"k": None})) # True
print(bool((0,)))     # True

print(bool(set()))       # False
print(bool({0}))         # True
print(bool(range(0)))    # False
print(bool(range(1)))    # True

print(bool(-1))    # True
print(bool(2))     # True
print(bool(0j))    # False (комплексный ноль)
print(bool(1j))    # True

import math
nan = float("nan")

print(bool(nan))         # True (!)
print(nan == nan)        # False (!)
print(math.isnan(nan))   # True (правильная проверка)

print(bool(b""))         # False
print(bool(b"\x00"))     # True (не пусто)
print(bool(bytearray())) # False
print(bool(bytearray(1)))# True (там один нулевой байт)







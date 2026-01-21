discount = lambda price, percent=10: round(price * (1 - percent / 100))
print(discount(200))
print(discount(200, 25))

def area(w,h,unit="cm2"):
	return f'{w*h} {unit}'
area(3,4)
area(3,4,"m2")
area(w=3,h=4)
area(h=4,w=3,unit="mm2")

def print_double(*params) -> None:
	for num in params:
		#if isinstance(num, (int, float)) and not isinstance(num, bool):
		if isinstance(num, bool):
			continue
		if type(num) in (int, float):
			print(num*2)
print_double(6, "Word", 7, 9.23, True)

def print_dict(**kwargs) -> None:
	for key, value in kwargs.items():
		print(f"{key}={value}")
print_dict(long="Георгий", short="Гоша", x=8, some=True)

lis = [6, 8, "Stroka", False, 46.7, 234, 1]
index = 0
while index<len(lis):
	if index%2==0:
		index+=1
		continue
	print(lis[index])
	index+=1

def analyze_text(text: str, **options: str) -> dict:
	stop_char: str = options.get("stop_char", "l")
	digits: int = 0
	spaces: int = 0
	found: bool = False

	for ch in text:
		if ch == stop_char and ch is not None:
			print("Найдена!")
			found = True
			break
		if ch == " ":
			spaces += 1
		elif ch.isdigit():
			digits += 1
	
	return {
    "found": found, 
    "digits": digits, 
    "space": spaces
    }

result = analyze_text("He11o wor1d", stop_char="None")
print(result)

























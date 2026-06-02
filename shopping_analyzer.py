
def parse_items(raw_text) -> list:
    parts = raw_text.split(',')
    items = list()
    for part in parts:
        clean_part = part.strip()
        name, price_text = clean_part.rsplit(' ', 1)
        price = int(price_text)
        clean_part_dict = {'name': name,
                           'price': price}
        items.append(clean_part_dict)
    return items

def calculate_total(items) -> int:
    total_cost = 0
    for item in items:
        total_cost += item['price']
    return total_cost

def calculate_average(items) -> float:
    total = calculate_total(items)
    count = len(items)
    return total / count

def find_most_expensive(items) -> dict:
    most_expensive_item = items[0]
    for item in items:
        if item['price'] > most_expensive_item['price']:
            most_expensive_item = item
    return most_expensive_item

def find_cheapest(items) -> dict:
    cheapest = items[0]
    for item in items:
        if item['price'] < cheapest['price']:
            cheapest = item
    return cheapest

def count_items2(items) -> dict:
    count_dict = {item['name']:0 for item in items}
    for item in items:
        if item['name'] in count_dict:
            count_dict[item['name']] += 1
    return count_dict

def count_items(items) -> dict:
    count_dict = dict()
    for item in items:
        name = item['name']
        if name in count_dict:
            count_dict[name] += 1
        else:
            count_dict[name] = 1
    return count_dict

def print_report(items):
    total = calculate_total(items)
    average = calculate_average(items)
    most_expensive = find_most_expensive(items)
    cheapest = find_cheapest(items)
    counts = count_items(items)
    unique_count = len(counts)
    print('Количество товаров', len(items))
    print('Уникальных товаров:', unique_count)
    print('Общая сумма:', total)
    print('Средняя цена:', average)
    print('Самый дорогой товар:', most_expensive['name'], most_expensive['price'])
    print('Самый дешёвый товар:', cheapest['name'], cheapest['price'])
    print('Сколько раз каждый товар встречается', counts)
    print('***************************')

items_1 = parse_items('яблоко 120, хлеб 60')
items_2 = parse_items('сыр 250, вода 40')
items_3 = parse_items('яблоко 120, хлеб 60, молоко 90, яблоко 120, сыр 250')
print_report(items_1)
print_report(items_2)
print_report(items_3)




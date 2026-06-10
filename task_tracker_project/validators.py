from exceptions import EmptyTitleError, InvalidPriorityError

def ask_int(message: str) -> int:
    while True:
        a = input(message)
        try:
            int_a = int(a)
            return int_a 
        except ValueError:
            print('Введите число.')

def validate_title(title: str) -> None:
    if not title:
        raise EmptyTitleError('Пустое название')

def ask_non_empty_string(message: str) -> str:
    while True:
        a = input(message)
        clean_a = a.strip()
        try:
            validate_title(clean_a)
            return clean_a
        except EmptyTitleError:
            print('Строка не должна быть пустой')
    
def validate_priority(priority: str) -> None:
    allowed_priorities = {
        'low',
        'medium',
        'high'
    }
    if priority not in allowed_priorities:
        raise InvalidPriorityError('Неправильный приоритет')

def ask_priority(message: str) -> str:
    while True:
        priority = input(message)
        clean_priority = priority.strip().lower()
        try:
            validate_priority(clean_priority)
            return clean_priority
        except InvalidPriorityError as e:
            print(e)

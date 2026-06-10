tasks = list()
next_id = 1

def print_menu():
    print('Выберите действие:')
    print('1. Добавить задачу')
    print('2. Показать все задачи')
    print('3. Отметить задачу выполненной')
    print('4. Удалить задачу')
    print('5. Найти задачу')
    print('0. Выйти')

def menu():
    while True:
        print_menu()
        choice = int(input())
        if choice == 1:
            title = input('Введите название: ')
            priority = input('Введите приоритет: ')
            add_task(tasks, title, priority)
            print('Задача добавлена')
        elif choice == 2:
            show_tasks(tasks)
        elif choice == 3:
            task_id = int(input('Введите id: '))
            mark_done(tasks, task_id)
        elif choice == 4:
            task_id = int(input('Введите id: '))
            delete_task(tasks, task_id)
        elif choice == 5:
            query = input('Введите название задачи: ')
            found_tasks = find_tasks(tasks, query)
            if len(found_tasks) == 0:
                print('Задачи не найдены')
            else:
                for task in found_tasks:
                    print_task(task)
        elif choice == 0:
            print('Вышел')
            break
        else:
            print('Неизвестная команда')
            continue

def add_task(tasks, title, priority):
    task = {
    "id": generate_id(),
    "title": title,
    "priority": priority,
    "done": False
    }
    tasks.append(task)

def generate_id() -> int:
    global next_id
    task_id = next_id
    next_id += 1
    return task_id

def show_tasks(tasks):
    if len(tasks) == 0:
        print('Список задач пуст')
        return
    print('ID | TITLE | PRIORITY | STATUS')
    for task in tasks:
        print_task(task)

def mark_done(tasks, task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = True
            print('Задача выполнена')
            return
    print('Задачи с таким id нет')

def delete_task(tasks, task_id):
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            print('Задача удалена')
            return
    print('Задачи с таким id нет')

def find_tasks(tasks: list, query: str) -> list:
    res = []
    for task in tasks:
        if query.lower() in task['title'].lower():
            res.append(task)
    return res

def print_task(task: dict):
    done = 'done' if task['done'] else 'active'
    print(f"{task['id']} | {task['title']} | {task['priority']} | {done}")

menu()
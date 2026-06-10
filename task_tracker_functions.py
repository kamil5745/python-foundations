tasks = list()

def print_menu() -> None:
    print('Выберите действие:')
    print('1. Добавить задачу')
    print('2. Показать все задачи')
    print('3. Отметить задачу выполненной')
    print('4. Удалить задачу')
    print('5. Найти задачу')
    print('0. Выйти')

def menu() -> None:
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

def add_task(
        tasks: list[dict], 
        title: str, 
        priority: str = 'medium'
    ) -> dict:
    task = create_task(get_next_id(tasks), title, priority)
    tasks.append(task)
    return task

def get_next_id(
        tasks: list[dict]
    ) -> int:
    if len(tasks) == 0:
        return 1
    else:
        max_id = 1
        for task in tasks:
            if task['id'] > max_id:
                max_id = task['id']
        return max_id + 1

def show_tasks(tasks: list[dict]) -> None:
    if len(tasks) == 0:
        print('Список задач пуст')
        return
    print('ID | TITLE | PRIORITY | STATUS')
    for task in tasks:
        print_task(task)

def mark_done(
        tasks: list[dict], 
        task_id: int
    ) -> None:
    task = find_task_by_id(tasks, task_id)
    if task is not None:
        task['done'] = True
        print('Задача выполнена')
    else:
        print('Задачи с таким id нет')

def delete_task(
        tasks: list[dict], 
        task_id: int
    ) -> None:
    task = find_task_by_id(tasks, task_id)
    if task is not None:
        tasks.remove(task)
        print('Задача удалена')
    else:
        print('Задачи с таким id нет')

def find_tasks(
        tasks: list[dict], 
        query: str
    ) -> list[dict]:
    res = []
    for task in tasks:
        if query.lower() in task['title'].lower():
            res.append(task)
    return res

def find_task_by_id(
        tasks: list[dict], 
        task_id: int
    ) -> dict | None:
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None

def print_task(task: dict) -> None:
    done = 'done' if task['done'] else 'active'
    print(f"{task['id']} | {task['title']} | {task['priority']} | {done}")

def create_task(
        task_id: int, 
        title: str, 
        priority: str = 'medium', 
        done: bool = False, 
        **extra
    ) -> dict:
    """Создает словарь задачи."""
    task = {
        'id': task_id,
        'title': title,
        'priority': priority,
        'done' : done
    }
    task.update(extra)
    return task
     
def filter_tasks (
        tasks: list[dict],
        done: bool | None = None,
        priority: str | None = None
    ) -> list[dict]:
    res = []
    for task in tasks:
        if done is not None and task['done'] != done:
            continue
        if priority is not None and task['priority'] != priority:
            continue
        res.append(task)
    return res

menu()
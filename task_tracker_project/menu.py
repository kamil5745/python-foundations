from models import Task
from rich.table import Table
from rich.console import Console


console = Console()

def print_menu() -> None:
    print('1. Добавить задачу')
    print('2. Показать все задачи')
    print('3. Отметить задачу выполненной')
    print('4. Удалить задачу')
    print('5. Найти задачу')
    print('0. Выйти')

def print_task(task: Task) -> None:
    done = 'done' if task.done else 'active'
    print(f"{task.id} | {task.title} | {task.priority} | {done}")

def print_tasks(tasks: list[Task]) -> None:

    if len(tasks) == 0:
        console.print('Список задач пуст', style='yellow')
        return
    table = Table()
    table.add_column("ID")
    table.add_column("Title")
    table.add_column("Priority")
    table.add_column("Status")
    for task in tasks:
        status = 'done' if task.done else 'active'
        table.add_row(str(task.id), task.title, task.priority, status)
    console.print(table)

def print_message_deleted_task() -> None:
    print('Задача удалена')

def print_message_not_found_task() -> None:
    print('Такой задачи нет')

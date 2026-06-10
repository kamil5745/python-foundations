from menu import print_menu, print_task, print_tasks, print_message_deleted_task, print_message_not_found_task
from validators import ask_int, ask_non_empty_string, ask_priority
from storage import load_tasks, save_tasks
from pathlib import Path
from exceptions import TaskNotFoundError, StorageError
from models import TaskManager

def main() -> None:
    path = Path(__file__).parent / 'tasks.json'
    manager = TaskManager()
    try:
        loaded_tasks = load_tasks(path)
    except StorageError:
        print('Ошибка загрузки файла')
        loaded_tasks = []

    manager.load_from_list(loaded_tasks)
    while True:
        print_menu()
        choice = ask_int('Выберите действие: ')
        if choice == 1:
            title = ask_non_empty_string('Введите название: ')
            priority = ask_priority('Введите приоритет: ')
            manager.add_task(title, priority)
            save_tasks(manager.to_list(), path)
            print('Задача добавлена')

        elif choice == 2:
            print_tasks(manager.tasks)

        elif choice == 3:
            task_id = ask_int('Введите id: ')
            try:
                manager.mark_done(task_id)
                save_tasks(manager.to_list(), path)
                print('Задача выполнена')
            except TaskNotFoundError as e:
                print(e)

        elif choice == 4:
            task_id = ask_int('Введите id: ')
            try:
                manager.delete_task(task_id)
                save_tasks(manager.to_list(), path)
                print_message_deleted_task()
            except TaskNotFoundError as e:
                print(e)

        elif choice == 5:
            query = ask_non_empty_string('Введите название задачи: ')
            found_tasks = manager.find_tasks(query)
            if len(found_tasks) == 0:
                print_message_not_found_task()
            else:
                for task in found_tasks:
                    print_task(task)
        elif choice == 0:
            print('Вышел')
            break
        else:
            print('Неизвестная команда')
            continue
if __name__ == '__main__':
    main()
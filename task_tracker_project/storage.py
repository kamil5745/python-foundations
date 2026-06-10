from pathlib import Path
import json
from exceptions import StorageError

def load_tasks(path: str | Path) -> list[dict]:
    storage = Path(path)
    if storage.is_file():
        with open(storage, 'r', encoding='utf-8') as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError as e:
                raise StorageError('Проблемы с хранилищем') from e
            return tasks
    else:
        return []

def save_tasks(tasks: list[dict], path: str | Path) -> None:
    storage = Path(path)
    with open(storage, 'w', encoding='utf-8') as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)
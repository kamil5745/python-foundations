from exceptions import TaskNotFoundError

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

def add_task(
        tasks: list[dict], 
        title: str, 
        priority: str = 'medium'
    ) -> dict:
    task = create_task(get_next_id(tasks), title, priority)
    tasks.append(task)
    return task

def find_task_by_id(
        tasks: list[dict], 
        task_id: int
    ) -> dict | None:
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None

def delete_task(
        tasks: list[dict], 
        task_id: int
    ) -> bool:
    task = find_task_by_id(tasks, task_id)
    if task is None:
        raise TaskNotFoundError("Задача с таким id не найдена")
    else:
        tasks.remove(task)
        return True

def mark_done(
        tasks: list[dict], 
        task_id: int
    ) -> bool:
    task = find_task_by_id(tasks, task_id)
    if task is None:
        raise TaskNotFoundError("Задача с таким id не найдена")
    else:
        task['done'] = True
        return True
    
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

def find_tasks(
        tasks: list[dict], 
        query: str
    ) -> list[dict]:
    res = []
    for task in tasks:
        if query.lower() in task['title'].lower():
            res.append(task)
    return res
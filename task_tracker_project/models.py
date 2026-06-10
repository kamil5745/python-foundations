from exceptions import TaskNotFoundError


class Task:
    def __init__(self, task_id: int, title: str, priority: str = "medium", done: bool = False) -> None:
        self.id = task_id
        self.title = title
        self.priority = priority
        self.done = done
    
    def mark_done(self) -> None:
        self.done = True

    def rename(self, new_title: str) -> None:
        self.title = new_title
    
    def to_dict(self) -> dict:
        return {
        "id": self.id,
        "title": self.title,
        "priority": self.priority,
        "done": self.done,
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Task':
        return cls(
            data['id'], 
            data['title'], 
            data['priority'], 
            data['done']
        )
    

class TaskManager:
    def __init__(self) -> None:
        self.tasks = list()

    def find_task_by_id(self, task_id: int) -> Task | None:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def add_task(self, title: str, priority: str = "medium") -> Task:
        if len(self.tasks) == 0:
            new_id = 1
        else:
            new_id = max([x.id for x in self.tasks]) + 1
        task = Task(new_id, title, priority)
        self.tasks.append(task)
        return task

    def mark_done(self, task_id: int) -> None:
        task = self.find_task_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(f'id {task_id} не найден')
        task.mark_done()

    def delete_task(self, task_id: int) -> None:
        task = self.find_task_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(f'id {task_id} не найден')
        self.tasks.remove(task)

    def get_active_tasks(self) -> list[Task]:
        active_tasks = list()
        for task in self.tasks:
            if not task.done:
                active_tasks.append(task)
        return active_tasks
    
    def get_done_tasks(self) -> list[Task]:
        done_tasks = list()
        for task in self.tasks:
            if task.done:
                done_tasks.append(task)
        return done_tasks

    def find_tasks(self, query: str) -> list[Task]:
        found_tasks = list()
        for task in self.tasks:
            if query.lower() in task.title.lower():
                found_tasks.append(task)
        return found_tasks

    def to_list(self) -> list[dict]:
        result = list()
        for task in self.tasks:
            result.append(task.to_dict())
        return result
    
    def load_from_list(self, data : list[dict]) -> None:
        self.tasks = list()
        for task_data in data:
            obj_task = Task.from_dict(task_data)
            self.tasks.append(obj_task)

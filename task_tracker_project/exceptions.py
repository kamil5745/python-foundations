class TaskTrackerError(Exception):
    pass

class TaskNotFoundError(TaskTrackerError):
    pass

class EmptyTitleError(TaskTrackerError):
    pass

class InvalidPriorityError(TaskTrackerError):
    pass

class StorageError(TaskTrackerError):
    pass

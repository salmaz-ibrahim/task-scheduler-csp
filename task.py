# task.py

class Task:

    def __init__(
        self,
        name,
        duration,
        priority,
        category
    ):

        self.name = name
        self.duration = duration
        self.priority = priority
        self.category = category

        self.assigned_slot = None
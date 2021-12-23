import copy

class Task:

    max_id = -1

    def __init__(
        self,
        name = "",
        duration = 0.0,
        deadline = 0.0
    ):
        self.id = Task.max_id
        self.name = name
        self.duration = duration
        self.deadline = deadline
        Task.max_id += 1
    
    def none_(self):
        self.name = ""
        self.duration = 0.0
        self.deadline = 0.0
    
    def is_none(self):
        return (len(self.name) == 0) or (self.duration <= 0) or (self.deadline <= 0)

    def copy(self):
        return copy.deepcopy(self)

    def __eq__(a, b):
        return (a.id == b.id)

import numpy as np
from .task import Task

class TaskManager:

    def __init__(
        self,
        n_slot = 10
    ):
        self.n_slot = n_slot
        self.dirty_slot = [Task() for _ in range(n_slot)]
        self.slot = [Task() for _ in range(n_slot)]

    def __getitem__(
        self,
        key
    ):
        return self.slot[key]

    def __setitem__(
        self,
        key,
        value
    ):
        assert(type(value) is Task)
        self.slot[key] = value

    def __iter__(
        self
    ):
        return self.slot.__iter__()

    def reset(
        self
    ):
        self.dirty_slot = [Task() for _ in range(self.n_slot)]
        self.slot = [Task() for _ in range(self.n_slot)]
    
    def create(
        self,
        task,
        idx = -1,
        do_override = False
    ):
        if (idx not in range(self.n_slot)):
            idx = np.random.choice(self.n_slot)
        if (self.slot[idx].is_none() or do_override):
            self.dirty_slot[idx] = task

    def decrement_required_effort(
        self,
        task,
        by = 1.0
    ):
        old = task.duration # task.required_effort
        new = old - by
        self.update_required_effort(task, new)
    
    def update_required_effort(
        self,
        task,
        value
    ):
        for _task in self.dirty_slot:
            if (task == _task):
                _task.duration = value

    def decrement_remaining_time(
        self,
        task,
        by = 1.0
    ):
        old = task.deadline # task.remaining_time
        new = old - by
        self.update_remaining_time(task, new)
    
    def update_remaining_time(
        self,
        task,
        value
    ):
        for _task in self.dirty_slot:
            if (task == _task):
                _task.deadline = value

    # def update(
    #     self,
    #     task,
    #     name = None,
    #     duration = None,
    #     deadline = None
    # ):
    #     for _task in range(self.slot):
    #         if (task == _task):
    #             if (name is not None): _task.name = name
    #             if (duration is not None): _task.duration = duration
    #             if (deadline is not None): _task.deadline = deadline
    #             break
    
    def delete(
        self,
        task
    ):
        for idx in range(self.n_slot):
            if (task == self.slot[idx]):
                self.dirty_slot[idx].none_()
                break

    def commit(
        self
    ):
        for idx in range(self.n_slot):
            self.slot[idx] = self.dirty_slot[idx].copy()

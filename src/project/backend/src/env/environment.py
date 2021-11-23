import numpy as np
import gym

from lib.shaRL.src.environment import Environment
from ..task import Task
from ..task import TaskManager

class TaskEnvironment(Environment):

    def __init__(
        self,
        n_slot = 10
    ):
        self.task_manager = TaskManager(n_slot=n_slot)
        self.state_space = None
        self.action_space = gym.spaces.Discrete(n_slot)
        self.observation_space = None
        self.state = None
        self.n_slot = n_slot

    def reset(
        self
    ):
        self.task_manager.reset()
        self.create_new_task(do_commit=True)
        self.set_state()
        observation = self.state
        return observation

    def step(
        self,
        action
    ):
        reward = 0.0
        is_within_deadline = False

        # decrease duration of task which is worked on
        if (action in range(self.n_slot)):
            task = self.task_manager[action]
            if (not task.is_none()):
                task.duration -= 1.0
                if (task.duration <= 0):
                    is_within_deadline = True
                    self.task_manager.delete(task)
                    reward += 1.0
        
        # decrease deadline of all tasks
        for task in self.task_manager:
            if (is_within_deadline): continue
            if (not task.is_none()):
                task.deadline -= 1.0
                if (task.deadline <= 0):
                    self.task_manager.delete(task)
                    reward -= 1.0

        # create new task
        self.create_new_task()

        # commit changes
        self.task_manager.commit()

        self.set_state()
        observation = self.state
        done = False
        info = self.task_manager
        return observation, reward, done, info

    def set_state(
        self
    ):
        buffer = []
        for task in self.task_manager:
            if (task.is_none()):
                buffer.append((0.0, 0.0))
            else:
                buffer.append((task.duration, task.deadline))
        self.state = np.array(buffer).reshape(-1)

    def create_new_task(
        self,
        do_commit = False
    ):
        n = 1 # np.random.poisson(lam=1.0)
        idcs = np.random.choice(self.n_slot, n)
        for idx in idcs:
            name = "task" + str(idx)
            duration = np.random.randint(1, 6)
            deadline = duration + np.random.randint(3, 6)
            task = Task(name, duration, deadline)
            self.task_manager.create(
                task,
                idx=idx,
                do_override=False
            )
        if (do_commit):
            self.task_manager.commit()

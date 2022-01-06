import os
import numpy as np
import pandas as pd
import gym

from ..task import Task
from ..task import TaskManager

class TaskEnvironment:

    def __init__(
        self,
        n_slot = 3,
        n_worker = 2
    ):
        INFO = ["required_effort", "remaining_time"]
        LOWER_BOUND = 0.0
        UPPER_BOUND = 100.0
        d_state_space = n_slot * len(INFO)
        d_action_space = n_slot ** n_worker

        self.task_manager = TaskManager(n_slot=n_slot)
        self.state_space = self.observation_space = gym.spaces.Box(
            low = np.ones(d_state_space, dtype=np.float32) * LOWER_BOUND,
            high = np.ones(d_state_space, dtype=np. float32) * UPPER_BOUND
        )
        self.action_space = gym.spaces.Discrete(d_action_space)
        
        self.t = 0
        self.T = 100
        self.state = None
        self.spec = {}
        self.n_slot = n_slot
        self.n_worker = n_worker

    def reset(
        self
    ):
        self.t = 0
        self.task_manager.reset()
        self.create_new_task(do_commit=True)
        self.set_state()
        observation = np.array(self.state, dtype=np.float32)
        return observation

    def setup(
        self,
        spec = "config/config.csv"
    ):
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), spec))
        df = pd.read_csv(path)
        for _, entry in df.iterrows():
            name = entry["name"]
            required_effort = entry["required_effort"]
            remaining_time = entry["remaining_time"]
            slot = entry["slot"]
            probability = entry["P"]
            self.spec[name] = {
                "required_effort": required_effort,
                "remaining_time": remaining_time,
                "slot": slot,
                "P": probability
            }

    def step(
        self,
        action
    ):
        UNIT_TIME = 1.0
        POSITIVE_REWARD = 1.0
        NEGATIVE_REWARD = -1.0
        reward = 0.0
        info = {
            "before": 0,
            "created": 0,
            "deleted": 0,
            "completed": 0,
            "after": 0
        }

        info["before"] = self.task_manager.count()

        # decode input & remove duplicates
        action = self.decode_action(action)
        action = set(action)

        # update task information
        for idx in range(self.n_slot):

            task = self.task_manager[idx]
            if (task.is_none()): continue
            is_completed = False

            # decrement required_effort
            for a in action:
                if (a == idx):
                    self.task_manager.decrement_required_effort(task, by=UNIT_TIME)
                    if (self.task_manager.dirty_slot[idx].duration <= 0):
                        is_completed = True
                        self.task_manager.delete(task)
                        reward += POSITIVE_REWARD
                        info["completed"] += 1

            # decrement remaining_time
            if (is_completed): continue
            self.task_manager.decrement_remaining_time(task, by=UNIT_TIME)
            if (self.task_manager.dirty_slot[idx].deadline <= 0):
                self.task_manager.delete(task)
                reward += NEGATIVE_REWARD
                info["deleted"] += 1

        # create new task
        info["created"] = self.create_new_task()

        # commit changes
        self.task_manager.commit()

        self.t = self.t + 1
        self.set_state()
        observation = np.array(self.state, dtype=np.float32)

        done = (self.t >= self.T)
        info["after"] = self.task_manager.count()
        # info = self.task_manager
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

    def decode_action(
        self,
        encoded_action # Int
    ):
        decoded_action = []
        for i in range(self.n_worker):
            action = encoded_action % self.n_slot
            encoded_action = encoded_action // self.n_slot
            decoded_action.append(action)
        return decoded_action

    def encode_action(
        self,
        decoded_action # List[Int]
    ):
        encoded_action = 0
        for i in reversed(range(self.n_worker)):
            action = decoded_action[i]
            encoded_action = encoded_action * self.n_slot
            encoded_action = encoded_action + action
        return encoded_action

    def create_new_dummy_task(
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

    def create_new_task(
        self,
        do_commit = False
    ):
        created = [False for _ in range(self.n_slot)]
        for name, value in self.spec.items():
            r = np.random.rand()
            if (value["P"] <= r):
                task = Task(name, value["required_effort"], value["remaining_time"])
                idx = value["slot"]
                created[idx] = self.task_manager.create(
                    task,
                    idx = idx,
                    do_override = False
                )

        if (do_commit):
            self.task_manager.commit()
        return sum(created)

    def score(
        self,
        history,
        info_history = None
    ):
        score_dictionary = {
            "total_reward": None,
            # "before": None,
            "created": None,
            "deleted": None,
            "completed": None,
            # "after": None,
            # "progress": None,
            # "efficiency": None,
            # "effectiveness": None,
            "covered": None,
            "missed": None,
            # "occupancy": None
        }


        H = len(history)
        if (H > 0):

            reward = [ r for (_, _, r, _) in history ]
            total_reward = sum(reward)
            score_dictionary["total_reward"] = total_reward

        if (info_history is None):
            return score_dictionary
        
        I = len(info_history)
        assert(H == I)
        if (I > 0):

            before = info_history[0]["before"]
            created = np.sum([ info["created"] for info in info_history ])
            deleted = np.sum([ info["deleted"] for info in info_history ])
            completed = np.sum([ info["completed"] for info in info_history ])
            after = info_history[-1]["after"]

            score_dictionary["created"] = created
            score_dictionary["deleted"] = deleted
            score_dictionary["completed"] = completed
            if (before + created > 0):
                score_dictionary["covered"] = completed / (before + created)
                score_dictionary["missed"] = deleted / (before + created)
            else:
                score_dictionary["covered"] = 1.0
                score_dictionary["missed"] = 1.0

        return score_dictionary

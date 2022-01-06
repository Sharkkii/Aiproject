#### Controller ####

import numpy as np
from ..lib.shaRL.src.controller import Controller

class TaskController(Controller):

    def __init__(
        self,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)

    def report(
        self,
        train_score,
        test_score
    ):
        print("total_reward", train_score["total_reward"], test_score["total_reward"])
        print("completed", np.mean(train_score["completed"]), np.mean(test_score["completed"]))
        print("deleted", np.mean(train_score["deleted"]), np.mean(test_score["deleted"]))
        print("covered", np.mean(train_score["covered"]), np.mean(test_score["covered"]))
        print("missed", np.mean(train_score["missed"]), np.mean(test_score["missed"]))
    
    def get_best_schedule(
        self,
        n_step = 1,
        n_sample = 1
    ):
        schedules = self.agent.get_best_schedule(
            self.env,
            n_step = n_step,
            n_sample = n_sample
        )
        return schedules

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
    
    def schedule_job(
        self,
        n_step = 1,
        k = 1
    ):
        schedule_list = self.agent.get_best_schedule_list(
            self.env,
            n_step = n_step,
            k = k
        )
        return schedule_list
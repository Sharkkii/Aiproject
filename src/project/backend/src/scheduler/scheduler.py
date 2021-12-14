#### Job Scheduler ####

from ..env import TaskEnvironment
from ..agent import TaskAgent
from ..controller import Controller

class JobScheduler:

    def __init__(
        self,
        n_slot = 3
    ):
        self.env = TaskEnvironment(
            n_slot = n_slot
        )
        self.agent = TaskAgent()
        self.controller = Controller(
            self.env,
            self.agent
        )

    def reset(
        self
    ):
        self.controller.reset()
    
    def setup(
        self
    ):
        self.controller.setup()
    
    def schedule_job(
        self,
        n_step,
        k = 1
    ):
        schedule_list = self.controller.schedule_job(
            n_step = n_step,
            k = k
        )
        return {
            "schedule_list": schedule_list
        }

    
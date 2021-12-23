#### Job Scheduler ####

from ..env import TaskEnvironment
from ..agent import TaskAgent
from ..controller import TaskController

class JobScheduler:

    def __init__(
        self,
        n_slot = 3,
        n_worker = 2
    ):
        self.env = TaskEnvironment(
            n_slot = n_slot,
            n_worker = n_worker
        )
        self.agent = TaskAgent(
            gamma = 0.90,
            tau = 0.01,
            eps = 0.05
        )
        self.controller = TaskController(
            self.env,
            self.agent
        )

    def reset(
        self
    ):
        self.controller.reset()
    
    def setup(
        self,
        policy_network,
        value_network,
        qvalue_network,
        policy_optimizer,
        value_optimizer,
        qvalue_optimizer,
    ):
        self.env.setup()
        self.agent.setup(
            self.env,
            policy_network = policy_network,
            value_network = value_network,
            qvalue_network = qvalue_network,
            policy_optimizer = policy_optimizer,
            value_optimizer = value_optimizer,
            qvalue_optimizer = qvalue_optimizer
        )

    def optimize(
        self,
        *args,
        **kwargs
    ):
        self.controller.fit(
            *args,
            **kwargs
        )
    
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

    
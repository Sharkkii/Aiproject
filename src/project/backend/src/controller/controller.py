#### Controller ####

from ..lib.shaRL.src.controller import Controller

class TaskController(Controller):

    def __init__(
        self,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
    
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
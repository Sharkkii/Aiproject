#### Agent ####

from ..lib.shaRL.src.core import DQN
from ..lib.shaRL.src.controller import Phases

class TaskAgent(DQN):

    def __init__(
        self,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)

    def get_best_schedule_list(
        self,
        env,
        n_step = 1,
        n_sample = 1
    ):
        schedule_list = []
        for _ in range(n_sample):
            schedule = []
            state = env.reset()
            for _ in range(n_step):
                action = self.actor.choose_action(
                    state,
                    phase = Phases.TEST
                )
                schedule.append(action)
            schedule_list.append(schedule)
        return schedule_list

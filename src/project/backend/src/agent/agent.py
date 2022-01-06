#### Agent ####

from ..lib.shaRL.src.const import PhaseType
from ..lib.shaRL.src.core import DQN

class TaskAgent(DQN):

    def __init__(
        self,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)

    def get_best_schedule(
        self,
        env,
        n_step = 1,
        n_sample = 1
    ):
        schedules = []
        for _ in range(n_sample):
            schedule = []
            state = env.reset()
            for _ in range(n_step):
                action = self.actor.choose_action(
                    state,
                    phase = PhaseType.TEST
                )
                state, reward, done, info = env.step(action)
                schedule.append(action)
            schedules.append(schedule)
        return schedules

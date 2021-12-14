#### Agent ####

class TaskAgent:

    def __init__(
        self
    ):
        pass

    def reset(
        self
    ):
        pass

    def setup(
        self,
        env
    ):
        self.env = env

    def choose_action(
        self,
        state
    ):
        action = self.env.action_space.sample()
        return action

    def get_best_schedule_list(
        self,
        env,
        n_step = 1,
        k = 1 # top-k
    ):
        # only the case k=1 is supported
        assert(k == 1)
        schedule_list = []
        for _ in range(k):
            schedule = []
            for _ in range(n_step):
                action = env.action_space.sample()
                schedule.append(action)
            schedule_list.append(schedule)
        return schedule_list

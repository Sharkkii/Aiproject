#### Controller ####

class Controller:

    def __init__(
        self,
        env,
        agent
    ):
        self.env = env
        self.agent = agent

    def reset(
        self
    ):
        _ = self.env.reset()
        self.agent.reset()

    def setup(
        self
    ):
        self.env.setup()
        self.agent.setup(
            env = self.env
        )
    
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
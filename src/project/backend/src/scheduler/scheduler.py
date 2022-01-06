#### Job Scheduler ####

import os
import torch

from ..env import TaskEnvironment
from ..agent import TaskAgent
from ..controller import TaskController

from ..lib.shaRL.src.network import VNet, QNet, PiNet
from ..lib.shaRL.src.network import ValueNetwork, QValueNetwork, PolicyNetwork
from ..lib.shaRL.src.optimizer import Optimizer

class JobScheduler:

    def __init__(
        self,
        n_slot = 3,
        n_worker = 1
    ):

        self.env = TaskEnvironment(
            n_slot = n_slot,
            n_worker = n_worker
        )

        d_action = self.env.action_space.n
        eps = 0.50 / d_action
        self.agent = TaskAgent(
            gamma = 0.90,
            tau = 0.01,
            eps = eps
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
        self
    ):
        d_observation = self.env.observation_space.low.size
        d_action = self.env.action_space.n

        value_network = VNet(input_shape=d_observation)
        value_optimizer = Optimizer(torch.optim.Adam, lr=1e-4)
        value_network = ValueNetwork(value_network=value_network)

        qvalue_network = QNet(input_shape=d_observation, output_shape=d_action)
        qvalue_optimizer = Optimizer(torch.optim.Adam, lr=1e-4)
        qvalue_network = QValueNetwork(qvalue_network=qvalue_network)

        policy_network = PiNet(input_shape=d_observation, output_shape=d_action)
        policy_optimizer = Optimizer(torch.optim.Adam, lr=1e-4)
        policy_network = PolicyNetwork(policy_network=policy_network)
    
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

    def train(
        self,
        *args,
        **kwargs
    ):
        self.controller.fit(
            *args,
            **kwargs
        )

    def save(
        self,
        path_to_policy,
        path_to_value,
        path_to_qvalue
    ):
        PATH_TO_AGENT_MODEL = os.path.abspath(os.path.join(os.path.dirname(__file__), "../agent/model"))
        path_to_policy = os.path.join(PATH_TO_AGENT_MODEL, path_to_policy)
        path_to_value = os.path.join(PATH_TO_AGENT_MODEL, path_to_value)
        path_to_qvalue = os.path.join(PATH_TO_AGENT_MODEL, path_to_qvalue)

        self.agent.save(
            path_to_policy = path_to_policy,
            path_to_value = path_to_value,
            path_to_qvalue = path_to_qvalue
        )
    
    def load(
        self,
        path_to_policy,
        path_to_value,
        path_to_qvalue
    ):
        PATH_TO_AGENT_MODEL = os.path.abspath(os.path.join(os.path.dirname(__file__), "../agent/model"))
        path_to_policy = os.path.join(PATH_TO_AGENT_MODEL, path_to_policy)
        path_to_value = os.path.join(PATH_TO_AGENT_MODEL, path_to_value)
        path_to_qvalue = os.path.join(PATH_TO_AGENT_MODEL, path_to_qvalue)

        self.agent.load(
            path_to_policy = path_to_policy,
            path_to_value = path_to_value,
            path_to_qvalue = path_to_qvalue
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

    
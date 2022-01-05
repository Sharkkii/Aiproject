import sys
import os
sys.path.append(os.path.abspath(os.path.join(__file__, "../..")))

import numpy as np
import torch
from src.scheduler.scheduler import JobScheduler
from src.lib.shaRL.src.network import VNet, QNet, PiNet, ValueNetwork, QValueNetwork, PolicyNetwork
from src.lib.shaRL.src.optimizer import Optimizer

def test_rl():

    scheduler = JobScheduler(
        n_slot = 5,
        n_worker = 1
    )

    d_observation = scheduler.env.observation_space.low.size
    d_action = scheduler.env.action_space.n

    v_net = VNet(input_shape=d_observation)
    v_opt = Optimizer(torch.optim.Adam, lr=1e-2)
    v_net = ValueNetwork(value_network=v_net)

    q_net = QNet(input_shape=d_observation, output_shape=d_action)
    q_opt = Optimizer(torch.optim.Adam, lr=1e-4)
    q_net = QValueNetwork(qvalue_network=q_net)

    pi_net = PiNet(input_shape=d_observation, output_shape=d_action)
    pi_opt = Optimizer(torch.optim.Adam, lr=1e-4)
    pi_net = PolicyNetwork(policy_network=pi_net)

    scheduler.setup(
        policy_network = pi_net,
        value_network = v_net,
        qvalue_network = q_net,
        policy_optimizer = pi_opt,
        value_optimizer = v_opt,
        qvalue_optimizer = q_opt
    )

    scheduler.optimize(
        n_epoch = 1000,
        n_train_eval = 5,
        n_test_eval = 5,
        env_step = 10
    )

    score = scheduler.controller.evaluate(
        n_train_eval = 5,
        n_test_eval = 5
    )
    print(score)

if __name__ == "__main__":
    test_rl()
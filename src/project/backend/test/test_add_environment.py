import sys
import os
sys.path.append(os.path.abspath(os.path.join(__file__, "../..")))

import numpy as np
from src.env import TaskEnvironment

def test_add_environment():
    n_slot = 3
    env = TaskEnvironment(n_slot=n_slot)
    state = env.reset()
    print(state.reshape(n_slot, -1))
    for _ in range(10):
        action = env.action_space.sample()
        state, reward, done, info = env.step(action)
        print(state.reshape(n_slot, -1), reward)

if __name__ == "__main__":
    test_add_environment()

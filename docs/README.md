# Manual of AI-powered progress management system

This document is an instruction manual of AI-powered progress management system (AI-PMS).

## Overview

AI-PMS has 6 main components on its dashboard; **Task Panel**, **Task Monitor**, **Schedule Panel**, **Schedule Monitor**, **RL Panel** and **RL Monitor**. XXX-Panel is a component to receive inputs from users, and XXX-Monitor is to display system outputs to users.

#### Task Panel & Task Monitor

**Task Panel** is used to create a new task from the "reference task list" shown on it. The reference task can be created/deleted via Task Panel. The created (and remaining) tasks are listed on **Task Monitor**, where users can delete them when they complete.

#### Schedule Panel & Schedule Monitor

**Schedule Panel** is used to set configurations of job scheduling. Users can try out job scheduling via Scheduling Panel by pressing the "Try Scheduling" button. The results (best-k schedules) are displayed on **Schedule Monitor**.

#### RL Panel & RL Monitor

**RL Panel** is used to train/use RL models to solve job scheduling problems. After initializing/loading a model, users can train and use it for job scheduling. The trained model can be saved as a user-specified name.

When the training is completed, the results (statistics obtained during the training) are displayed on **RL Monitor** as line graphs. One is "cover rate", which indicates how many tasks the RL agent has finished. Another is "missed rate", which indicated how many tasks the RL agent fails to complete (misses the deadline). Note that the sum of these 2 statistics is almost 100% (but not equal to exactly 100%).
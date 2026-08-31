# Reinforcement Learning for Games

## Project: Q-Learning Grid Game

This project demonstrates Reinforcement Learning (RL) using a simple game environment built with Python and Pygame.

The player/agent learns to reach the goal while avoiding obstacles. The agent uses **Q-Learning** to learn which action is best for each game state.

## Features
- Simple playable grid-based game
- Q-Learning reinforcement learning agent
- Training mode
- Play mode using the trained Q-table
- Reward and penalty system
- Q-table saved to disk
- Project report included

## Requirements
Python 3.9 or newer is recommended.

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the project

### 1. Train the agent

```bash
python train.py
```

This creates:

```text
model/q_table.pkl
```

### 2. Watch the trained agent play

```bash
python play.py
```

### Controls
The game can also be played manually using the arrow keys.

## Reinforcement Learning concept

At every step, the agent observes a state and chooses one action:

- UP
- DOWN
- LEFT
- RIGHT

The environment returns a reward.

Typical rewards:
- +100: reaches the goal
- -100: hits an obstacle
- -1: normal movement

The Q-Learning update is:

Q(s,a) = Q(s,a) + alpha * [reward + gamma * max Q(s',a') - Q(s,a)]

where:
- alpha = learning rate
- gamma = discount factor
- epsilon = exploration probability

## GitHub submission

Upload this entire folder to a GitHub repository.

Do not upload Python virtual environments such as `.venv/`.

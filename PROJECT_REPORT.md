# Reinforcement Learning for Games

## 1. Title
**Reinforcement Learning for Games Using Q-Learning**

## 2. Abstract
Reinforcement Learning is a machine learning technique in which an agent learns by interacting with an environment. This project implements a simple grid-based game where an intelligent agent learns to reach a goal while avoiding obstacles.

The agent uses the Q-Learning algorithm. It receives rewards for good actions and penalties for undesirable actions. After repeated training episodes, the Q-table contains useful information about which action should be selected in each state.

## 3. Objectives
- Understand the basic concepts of Reinforcement Learning.
- Implement an RL environment for a game.
- Implement Q-Learning.
- Train an agent through repeated game episodes.
- Visualize the trained agent playing the game.
- Understand rewards, states, actions and exploration.

## 4. Technologies Used
- Python
- Pygame
- NumPy
- Q-Learning
- Pickle for model storage

## 5. Reinforcement Learning Components

### Agent
The agent is the player that decides what action to take.

### Environment
The environment is the grid game containing the player, goal and obstacles.

### State
The state contains the current agent position and goal position.

### Actions
The agent can:
1. Move Up
2. Move Down
3. Move Left
4. Move Right

### Reward
- Reaching the goal: +100
- Hitting an obstacle: -100
- Normal movement: -1
- Moving outside the grid: -5

## 6. Q-Learning

Q-Learning stores the expected future reward for taking an action in a particular state.

The update equation is:

Q(s,a) = Q(s,a) + alpha [r + gamma max Q(s',a') - Q(s,a)]

Where:

- Q(s,a) = current Q-value
- alpha = learning rate
- gamma = discount factor
- r = immediate reward
- s' = next state
- a' = next action

## 7. Training Process

1. Start with an empty Q-table.
2. Reset the game.
3. Observe the current state.
4. Select an action using epsilon-greedy exploration.
5. Perform the action.
6. Receive a reward.
7. Update the Q-table.
8. Repeat until the episode ends.
9. Reduce epsilon gradually.
10. Repeat for many episodes.
11. Save the trained Q-table.

## 8. Epsilon-Greedy Strategy

At the beginning, the agent explores many actions. As training continues, exploration decreases and the agent increasingly chooses the best-known action.

This balances:
- Exploration: trying new actions.
- Exploitation: using learned knowledge.

## 9. System Flow

```text
Start
  |
  v
Initialize Environment
  |
  v
Initialize Q-Table
  |
  v
Observe State
  |
  v
Choose Action
  |
  v
Perform Action
  |
  v
Receive Reward
  |
  v
Update Q-Table
  |
  v
Episode Finished?
  |             |
 No            Yes
  |             |
  +----<--------+
                |
                v
          Save Trained Model
                |
                v
             Play Game
```

## 10. Expected Result

After training, the agent should learn efficient paths toward the goal and avoid known obstacles. The exact performance depends on the number of training episodes and learning parameters.

## 11. Advantages
- Simple to understand.
- Does not require a labelled dataset.
- Learns from interaction.
- Useful for game AI.
- Easy to visualize.

## 12. Limitations
- Q-tables become large for complex state spaces.
- Performance can depend on reward design.
- The current game has a relatively small state/action space.
- More advanced games require Deep Q-Networks or other RL algorithms.

## 13. Future Enhancements
- Add moving enemies.
- Add levels and increasing difficulty.
- Add score tracking.
- Use Deep Q-Learning with a neural network.
- Add a larger game environment.
- Compare Q-Learning with SARSA.
- Plot training rewards.

## 14. Conclusion
This project demonstrates how Reinforcement Learning can be used to create a game-playing agent. Through repeated interaction with the environment, the Q-Learning agent learns which actions produce better long-term rewards. The project provides a simple foundation for understanding game AI and more advanced Reinforcement Learning methods.

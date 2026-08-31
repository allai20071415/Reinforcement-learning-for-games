from environment import GridGame, ACTIONS
from agent import QLearningAgent

EPISODES = 3000
MODEL_PATH = "model/q_table.pkl"

def train():
    env = GridGame(render=False)
    agent = QLearningAgent(ACTIONS)

    rewards = []

    for episode in range(1, EPISODES + 1):
        state = env.reset()
        total_reward = 0

        while True:
            action = agent.choose_action(state, training=True)
            next_state, reward, done = env.step(action)

            agent.update(state, action, reward, next_state, done)

            state = next_state
            total_reward += reward

            if done:
                break

        agent.decay_exploration()
        rewards.append(total_reward)

        if episode % 100 == 0:
            avg = sum(rewards[-100:]) / 100
            print(
                f"Episode {episode}/{EPISODES} | "
                f"Average reward: {avg:.2f} | "
                f"Epsilon: {agent.epsilon:.3f}"
            )

    agent.save(MODEL_PATH)
    env.close()
    print(f"Training complete. Model saved to {MODEL_PATH}")

if __name__ == "__main__":
    train()

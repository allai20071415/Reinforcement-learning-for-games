import pygame
from environment import GridGame, ACTIONS
from agent import QLearningAgent

MODEL_PATH = "model/q_table.pkl"

def manual_mode(env):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        action = None
        if keys[pygame.K_UP]:
            action = 0
        elif keys[pygame.K_DOWN]:
            action = 1
        elif keys[pygame.K_LEFT]:
            action = 2
        elif keys[pygame.K_RIGHT]:
            action = 3

        if action is not None:
            _, _, done = env.step(action)
            if done:
                env.reset()

        env.draw()

def ai_mode(env, agent):
    state = env.reset()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        action = agent.choose_action(state, training=False)
        state, reward, done = env.step(action)
        env.draw()

        if done:
            pygame.time.wait(600)
            state = env.reset()

    env.close()

def main():
    env = GridGame(render=True)
    agent = QLearningAgent(ACTIONS)
    agent.load(MODEL_PATH)

    print("AI is playing. Close the window to exit.")
    ai_mode(env, agent)

if __name__ == "__main__":
    main()

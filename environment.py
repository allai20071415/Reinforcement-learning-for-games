import random
import pygame

GRID_SIZE = 8
CELL_SIZE = 70
WINDOW_SIZE = GRID_SIZE * CELL_SIZE

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
ACTIONS = [UP, DOWN, LEFT, RIGHT]

class GridGame:
    def __init__(self, render=False):
        self.render_enabled = render
        self.obstacles = {(2, 2), (2, 3), (4, 5), (5, 5), (6, 2)}
        self.goal = (7, 7)
        self.max_steps = 100
        self.steps = 0
        self.screen = None
        self.clock = None

        if self.render_enabled:
            pygame.init()
            self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
            pygame.display.set_caption("Reinforcement Learning Game")
            self.clock = pygame.time.Clock()

        self.reset()

    def reset(self):
        self.agent = (0, 0)
        while self.agent in self.obstacles or self.agent == self.goal:
            self.agent = (random.randrange(GRID_SIZE), random.randrange(GRID_SIZE))
        self.steps = 0
        return self.get_state()

    def get_state(self):
        # State = agent x, agent y, goal x, goal y.
        return (self.agent[0], self.agent[1], self.goal[0], self.goal[1])

    def step(self, action):
        x, y = self.agent
        nx, ny = x, y

        if action == UP:
            ny -= 1
        elif action == DOWN:
            ny += 1
        elif action == LEFT:
            nx -= 1
        elif action == RIGHT:
            nx += 1

        self.steps += 1

        # Boundary penalty
        if nx < 0 or nx >= GRID_SIZE or ny < 0 or ny >= GRID_SIZE:
            reward = -5
            done = self.steps >= self.max_steps
            return self.get_state(), reward, done

        # Obstacle penalty
        if (nx, ny) in self.obstacles:
            reward = -100
            done = True
            return self.get_state(), reward, done

        self.agent = (nx, ny)

        if self.agent == self.goal:
            reward = 100
            done = True
        elif self.steps >= self.max_steps:
            reward = -10
            done = True
        else:
            reward = -1
            done = False

        return self.get_state(), reward, done

    def draw(self):
        if not self.render_enabled:
            return

        self.screen.fill((245, 245, 245))

        # Grid
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, (210, 210, 210), rect, 1)

        # Obstacles
        for x, y in self.obstacles:
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(self.screen, (80, 80, 80), rect)

        # Goal
        gx, gy = self.goal
        goal_rect = pygame.Rect(gx * CELL_SIZE, gy * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(self.screen, (70, 180, 90), goal_rect)

        # Agent
        ax, ay = self.agent
        center = (ax * CELL_SIZE + CELL_SIZE // 2, ay * CELL_SIZE + CELL_SIZE // 2)
        pygame.draw.circle(self.screen, (60, 100, 220), center, CELL_SIZE // 3)

        pygame.display.flip()
        self.clock.tick(12)

    def close(self):
        if self.render_enabled:
            pygame.quit()

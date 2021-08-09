import math
import pygame as pg

class Agent():
    def __init__(self):
        pass

    def get_agent_img(self, agent_size):
        agent_img = pg.image.load("C:/Users/player/Documents/GitHub/Pygame_sim/Obstacle/Jackal.png")# 이미지의 경로는 Agent폴더에 있으며 알맞게 수정바람.
        agent_img = pg.transform.scale(agent_img, (agent_size[0], agent_size[1]))
        return agent_img
import pygame as pg
import random
from Define.Set_Define import *
from pygame.locals import Rect

class Agent():
    # def __init__(self):
    #     super(Agent, self).__init__(Rect(AGENT_XY[0], AGENT_XY[1], AGENT_SIZE_XY[0], AGENT_SIZE_XY[1]))
    #     self.theta = 0
    #     self.lineal = 0
    #     self.agent_img = pg.image.load("./Agent/Jackal_origin.png")
    #
    # def draw(self):
    #     rotated = pg.transform.rotate(self.agent_img, self.theta)
    #     rect = rotated.get_rect()
    #     rect.center = self.rect.center
    def __init__(self):
        self.agent_img = pg.image.load("./Agent/Jackal_origin.png")# 이미지의 경로는 Agent폴더에 있으며 문제가 있다면 수정바람.
        self.agent_img_scale = pg.transform.scale(self.agent_img, (AGENT_SIZE_XY[0], AGENT_SIZE_XY[1]))


        self.theta = 0
        self.agent_update_x = 0
        self.agent_update_y = 0
        self.lineal_vel = LINEAR_SPEED
        self.angle_vel = ROTATE_SPEED

    def agent_key_input(self, key_on_off):
        self.linear_angle_dt = pg.Vector3()# x, y, z
        if key_on_off == True:
            for event in pg.event.get():
                key_event = pg.key.get_pressed()
                if key_event[pg.K_w]:
                    self.linear_angle_dt[0] = self.lineal_vel
                    self.linear_angle_dt[2] = 0
                    return self.linear_angle_dt

                elif key_event[pg.K_s]:
                    self.linear_angle_dt[0] = -self.lineal_vel
                    self.linear_angle_dt[2] = 0
                    return self.linear_angle_dt

                elif key_event[pg.K_a]:
                    self.linear_angle_dt[0] = self.lineal_vel
                    self.linear_angle_dt[2] = self.angle_vel
                    return self.linear_angle_dt

                elif key_event[pg.K_d]:
                    self.linear_angle_dt[0] = self.lineal_vel
                    self.linear_angle_dt[2] = -self.angle_vel

                    return self.linear_angle_dt

            return self.linear_angle_dt


    def agent_move(self, get_axis):
        agent_axis = [AGENT_XY[0] + self.agent_update_x, AGENT_XY[1] + self.agent_update_y, get_axis[2]]

        if INIT_ARENA_XY[0] < agent_axis[0] < END_ARENA_WH[0] and \
            INIT_ARENA_XY[1] < agent_axis[1] < END_ARENA_WH[1]:

            self.agent_update_x += get_axis[0]
            self.agent_update_y += get_axis[1]

        return [agent_axis[0], agent_axis[1], get_axis[2]]


    def draw(self, screen, agent_move): # 미완성.
        self.rotate_img = pg.transform.rotate(self.agent_img_scale, agent_move[2])
        # rect = self.rotate_img.get_rect()

        screen.blit(self.rotate_img, (agent_move[0], agent_move[1]))
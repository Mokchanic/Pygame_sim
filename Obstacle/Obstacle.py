import pygame as pg
from Define.Set_Define import *


class Obstacle():
    def __init__(self):
        self.circle_img = pg.image.load("./Obstacle/black_circle.png")
        self.rectangle_img = pg.image.load("./Obstacle/black_square.png")
        self.circle_size_img = None
        self.rectangle_size_img = None


    # def circle_draw(self, screen, color, axis, radius):
    #     pg.draw.circle(screen, color, axis, radius)
    #
    # def rectangle_draw(self, screen, color, xywh):
    #     pg.draw.rect(screen, color, xywh)

    def circle_draw(self, screen, axis, size):
        self.circle_size_img = pg.transform.scale(self.circle_img, (size[0], size[1]))
        circle_mask = pg.mask.from_surface(self.circle_size_img)
        circle_rect = self.circle_size_img.get_rect()
        cx = MAP_SIZE_XY[0]/2 - circle_rect[0]
        cy = MAP_SIZE_XY[1]/2 - circle_rect[1]
        screen.blit(self.circle_size_img, (axis[0], axis[1]))

    def rectangle_draw(self, screen, axis, size):
        self.rectangle_size_img = pg.transform.scale(self.rectangle_img, (size[0], size[1]))
        screen.blit(self.rectangle_size_img, (axis[0], axis[1]))
        pass

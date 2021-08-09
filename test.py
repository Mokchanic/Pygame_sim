import pygame
import sys
import time
import random

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SPAWN_TIME = 1

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
pygame.display.set_caption("Stars in Space")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


class Star(object):
    def __init__(self):
        self.image = pygame.image.load("./Agent/Jackal.png").convert_alpha()
        self.x = random.randint(0, SCREEN_WIDTH - self.image.get_width())
        self.y = random.randint(0, SCREEN_HEIGHT - self.image.get_height())
        self.head = random.randint(0, 359)
        self.rotated_image = pygame.transform.rotate(self.image, self.head)
        self.rotate_speed = random.randint(1, 3)

    def rotate(self):
        self.head += self.rotate_speed
        self.rotated_image = pygame.transform.rotate(self.image, self.head)

    def draw(self):
        screen.blit(self.rotated_image, (self.x + self.image.get_width() / 2 - self.rotated_image.get_width() / 2,
                                         self.y + self.image.get_height() / 2 - self.rotated_image.get_height() / 2))


def main():
    stars = []

    last_spawn_time = time.time()

    while True:
        clock.tick(60)
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if time.time() - last_spawn_time > SPAWN_TIME:
            stars.append(Star())
            last_spawn_time = time.time()

        for star in stars:
            star.rotate()
            star.draw()

        pygame.display.update()


if __name__ == "__main__":
    main()
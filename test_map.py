import pygame as pg

from Define.Set_Define import *
from Make_Map import Map

def main():
    get_map = Map.Map()
    screen = get_map.make_window(MAP_SIZE_XY)
    done = False

    while not done:
        get_map.frame_rate(MAP_FRAME)
        get_map.end_condition()
        screen.fill(WHITE)



if __name__ == "__main__":
    main()
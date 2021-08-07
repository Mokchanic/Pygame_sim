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
        screen.fill(WHITE) # 바탕화면을 흰색으로

        get_map.arena(screen, BLACK, INIT_ARENA_XY, END_ARENA_WH, ARENA_THICK)
        get_map.grid(screen, GRAY, X_INTERVAL, Y_INTERVAL, GRID_THICK, INIT_ARENA_XY, ARENA_END_AXIS, GRID_ON_OFF)


        pg.display.flip() # 업데이트



if __name__ == "__main__":
    main()
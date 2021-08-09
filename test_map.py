import pygame as pg
import pygame.event

from Define.Set_Define import *
from Make_Map import Map
from Agent import Agent

def main():
    get_map = Map.Map()
    get_agent = Agent.Agent()
    screen = get_map.make_window(MAP_SIZE_XY)


    done = False

    while not done:
        # Map
        get_map.frame_rate(MAP_FRAME)
        #done = get_map.end_condition() # Key_move와 충돌을 일으킴
        screen.fill(WHITE) # 바탕화면을 흰색으로

        get_map.arena(screen, BLACK, INIT_ARENA_XY, END_ARENA_WH, ARENA_THICK)
        get_map.grid(screen, GRAY, X_INTERVAL, Y_INTERVAL, GRID_THICK, INIT_ARENA_XY, ARENA_END_AXIS, GRID_ON_OFF)

        # Agent
        get_move = get_agent.agent_key_input(KEY_ON_OFF)
        get_agent_move = get_agent.agent_move(get_move)
        get_agent.draw(screen, get_agent_move) # Agent그리기


        # Reset()
        # get_map()

        pg.display.flip() # 업데이트


if __name__ == "__main__":
    main()
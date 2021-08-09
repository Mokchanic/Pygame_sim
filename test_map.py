import pygame as pg

from Define.Set_Define import *
from Make_Map import Map
from Agent import Agent

def main():
    get_map = Map.Map()
    get_agent = Agent.Agent()
    screen = get_map.make_window(MAP_SIZE_XY)
    agent = get_agent.get_agent_img(AGENT_SIZE_XY)

    done = False

    while not done:
        # Map
        get_map.frame_rate(MAP_FRAME)
        get_map.end_condition()
        screen.fill(WHITE) # 바탕화면을 흰색으로

        get_map.arena(screen, BLACK, INIT_ARENA_XY, END_ARENA_WH, ARENA_THICK)
        get_map.grid(screen, GRAY, X_INTERVAL, Y_INTERVAL, GRID_THICK, INIT_ARENA_XY, ARENA_END_AXIS, GRID_ON_OFF)

        # Agent
        screen.blit(agent, (AGENT_XY[0], AGENT_XY[1])) # Agent 그리기

        pg.display.flip() # 업데이트




if __name__ == "__main__":
    main()
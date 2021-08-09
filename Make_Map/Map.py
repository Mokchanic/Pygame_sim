import pygame as pg

class Map():
    def __init__(self):
        self.done = False
        self.repeat = 0
        self.x_length = 0
        self.y_length = 0

    def make_window(self, size): # UI창을 만들어줌.
        self.window = pg.display.set_mode(size)
        pg.display.set_caption("RV_Robot_Sim")
        return self.window

    def frame_rate(self, frame):
        self.clock = pg.time.Clock()
        self.clock.tick(frame)
        return self.clock

    def end_condition(self): # 환경 종료 조건
        for event in pg.event.get():
            if event.type == pg.QUIT: #GUI창에서 X를 누르면
                self.done = True
        return self.done

    def arena(self, screen, color, init_xy, end_xy, arena_tick):
        self.draw_arena = pg.draw.rect(screen, color, [init_xy[0], init_xy[1], end_xy[0], end_xy[1]], arena_tick)
        return self.draw_arena

    def grid(self, screen, color, x_interval, y_interval, thickness, init_arena_xy, end_arena_xy, on_off):
        self.x_length = end_arena_xy[0] - init_arena_xy[0]
        self.y_length = end_arena_xy[1] - init_arena_xy[1]
        self.repeat_and_length = int(self.x_length / x_interval)
        self.init_arena_x = init_arena_xy[0]
        self.init_arena_y = init_arena_xy[1]
        if on_off == True:
            for i in range(self.repeat_and_length-1):
                self.init_arena_x += x_interval
                x_init_grid_xy = [self.init_arena_x, init_arena_xy[1]]
                x_end_grid_xy = [self.init_arena_x, end_arena_xy[1]]
                self.line_x = pg.draw.line(screen, color, [x_init_grid_xy[0], x_init_grid_xy[1]], [x_end_grid_xy[0], x_end_grid_xy[1]], thickness)

                self.init_arena_y += y_interval
                y_init_grid_xy = [init_arena_xy[0], self.init_arena_y]
                y_end_grid_xy = [end_arena_xy[0], self.init_arena_y]
                self.line_y = pg.draw.line(screen, color, [y_init_grid_xy[0], y_init_grid_xy[1]], [y_end_grid_xy[0], y_end_grid_xy[1]], thickness)

        else:
            pass


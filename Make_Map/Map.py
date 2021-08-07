import pygame as pg

class Map():
    def __init__(self):
        self.done = False

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


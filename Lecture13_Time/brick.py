from pico2d import *
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
FALL_SPEED_KMPH = 20.0   # km / hour
FALL_SPEED_MPM = (FALL_SPEED_KMPH * 1000.0 / 60.0 )
FALL_SPEED_MPS = (FALL_SPEED_MPM / 60.0)
FALL_SPEED_PPS = (FALL_SPEED_MPS * PIXEL_PER_METER )

class Brick:
    x = 500
    y = 250
    move = 0
    dir = 0
    def __init__(self):
        self.image = load_image('brick180x40.png')
    def update(self):
        if Brick.dir == 0:
            if Brick.x <= 1400:
                Brick.move = FALL_SPEED_PPS * game_framework.frame_time
                Brick.x += Brick.move
            else: Brick.dir = 1
        elif Brick.dir == 1:
            if Brick.x >= 200:
                Brick.move = FALL_SPEED_PPS * game_framework.frame_time
                Brick.x -= Brick.move
            else: Brick.dir = 0

        pass

    def draw(self):
        self.image.draw(Brick.x, Brick.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return Brick.x - 90, Brick.y - 20, Brick.x + 90, Brick.y + 20
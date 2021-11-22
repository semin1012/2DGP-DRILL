from pico2d import *
import random
from brick import Brick

import main_state
import game_framework
import game_world

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
FALL_SPEED_KMPH = 20.0   # km / hour
FALL_SPEED_MPM = (FALL_SPEED_KMPH * 1000.0 / 60.0 )
FALL_SPEED_MPS = (FALL_SPEED_MPM / 60.0)
FALL_SPEED_PPS = (FALL_SPEED_MPS * PIXEL_PER_METER )

class Ball:
    image = None
    drop = 0

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600-1), random.randint(600, 1000), FALL_SPEED_PPS
        self.parent = None
        self.rx, self.ry = 0, 0

    def get_bb(self):
        # fill here
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        if self.parent is None: # 볼은 부모가 없으면
            self.y -= self.fall_speed * game_framework.frame_time
        else:
            self.x, self.y = self.parent.x + self.rx, self.parent.y + self.ry

    def stop(self):
        self.fall_speed = 0
        # self.y = 60

    def brick_stop(self):
        self.fall_speed = 0
        if Brick.dir == 0:
            self.x += Brick.move
        elif Brick.dir == 1:
            self.x -= Brick.move

    def ball_stop(self):
        self.fall_speed = 0

    def set_parent(self, brick):
        self.parent = brick
        self.rx, self.ry = self.x - brick.x, self.y - brick.y # 발판에 대한 상대적인 x, y의 위치




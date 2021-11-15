import game_framework
from pico2d import *
from ball import Ball
import random

import game_world


PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 50.0  # Km / Hour, 새는 한 시간에 50km를 간다고 가정하고 코드를 짰다
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Bird:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 14)
        self.dir = random.randint(0, 1 + 1)
        self.image = load_image('bird100x100x14.png')
        self.velocity = 0
        self.image_num = 0
        self.velocity += RUN_SPEED_PPS
        print(self.velocity)


    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14

        if self.dir == 0:
            if self.x <= 1500:
                self.x += self.velocity * game_framework.frame_time
                self.image_num = 0
            else:
                self.dir = 1

        else:
            if self.x >= 100:
                self.x -= self.velocity * game_framework.frame_time
                self.image_num = 1
            else: self.dir = 0

    def draw(self):
        if self.image_num == 0:
            self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)
        else:
            self.image.clip_composite_draw(int(self.frame) * 100, 0, 100, 100, 3.141592 / 2, '', self.x + 25, self.y - 25, 100, 100)






from pico2d import *
import game_framework
import server
import collision
from ball import Ball

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
FALL_SPEED_KMPH = 20.0   # km / hour
FALL_SPEED_MPM = (FALL_SPEED_KMPH * 1000.0 / 60.0 )
FALL_SPEED_MPS = (FALL_SPEED_MPM / 60.0)
FALL_SPEED_PPS = (FALL_SPEED_MPS * PIXEL_PER_METER )

class Brick:
    move = 0
    dir = 0
    def __init__(self):
        self.image = load_image('brick180x40.png')
        self.x, self.y = 100, 200
        self.speed = 200
        self.child_balls = Ball()

    def update(self):
        if Brick.dir == 0:
            if self.x <= 1400:
                Brick.move = FALL_SPEED_PPS * game_framework.frame_time
                self.x += Brick.move
            else: Brick.dir = 1
        elif Brick.dir == 1:
            if self.x >= 200:
                Brick.move = FALL_SPEED_PPS * game_framework.frame_time
                self.x -= Brick.move
            else: Brick.dir = 0

        for ball in server.balls.copy:
            if collision.collide(self, ball):
                self.attach_ball(ball)
                server.balls.remove(ball)



    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 90, self.y - 20, self.x + 90, self.y + 20

    def attach_ball(self, ball):
        pass
        # self.child_balls.append(ball)
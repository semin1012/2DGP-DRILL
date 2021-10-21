from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.image = load_image('run_animation.png')
        self.frame = random.randint(0, 7)

    def update(self):
        self.x += 5
        self.frame = (self.frame + 1) % 8
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(40, 760), 599
        self.image_rand = random.randint(1, 2 + 1)  # 1이면 small, 2면 big
        self.speed = random.randint(1, 10)
        self.big_image = load_image('ball41x41.png')
        self.small_image = load_image('ball21x21.png')
        print(self.x)

    def update(self):
        if self.image_rand == 1:
            if self.y - self.speed >= 55:
                self.y -= self.speed
            else: self.y = 55
        elif self.image_rand == 2:
            if self.y - self.speed >= 65:
                self.y -= self.speed
            else: self.y = 65

    def draw(self):
        if self.image_rand == 1:
            self.small_image.clip_draw(0, 0, 21, 21, self.x, self.y)
        elif self.image_rand == 2:
            self.big_image.clip_draw(0, 0, 41, 41, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

grass = Grass()
team = [Boy() for i in range(1, 11+1)]
balls = [Ball() for i in range(1, 20+1)]

running = True

# game main loop code
while running:
    handle_events()

    # game logic
    for boy in team:
        boy.update()
    for ball in balls:
        ball.update()
    # game draw
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ball in balls:
        ball.draw()
    update_canvas()

# finalization code
close_canvas()
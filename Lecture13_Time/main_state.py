import random
import json
import os

from pico2d import *
import game_framework
import game_world

from boy import Boy
from grass import Grass
from ball import Ball
from brick import Brick


name = "MainState"

grass = None
boy = None
brick = None
balls = []


def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b - 10: return False
    if right_a < left_b + 10: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b - 30: return False

    return True


def enter():
    global boy
    boy = Boy()

    global grass
    grass = Grass()

    game_world.add_object(grass, 0)
    game_world.add_object(boy, 1)

    global balls
    balls = [Ball() for i in range(70)]
    game_world.add_objects(balls, 1)

    global brick
    brick = Brick()
    game_world.add_object(brick, 1)


def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    # fill here
    for ball in balls:
        if collide(boy, ball):
            balls.remove(ball)
            game_world.remove_object(ball)
            # print("COLLISION")
    for ball in balls:
        for ball2 in balls:
            if collide(ball2, ball):
                ball.ball_stop()
    for ball in balls:
        if collide(grass, ball):
            ball.stop()
    for ball in balls:
        if collide(brick, ball):
            ball.brick_stop()
    # delay(0.1)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()







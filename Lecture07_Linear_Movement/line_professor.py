import turtle
import random
import math
import math

def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()


def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())


def draw_line_basic(p1, p2):
    # fill here
    draw_big_point(p1)
    draw_big_point(p2)

    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    a = (y2 - y1) / (x2 - x1)
    b = y1 - x1 * a
    for x in range(x1, x2+1, 10):
        y = a * x + b
        draw_point((x, y))

    draw_point(p2)
    pass


def draw_line(p1, p2):
    # fill here
    draw_big_point(p1)
    draw_big_point(p2)
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    for i in range(0, 100 + 1, 2):
        t = i / 100
        x = (1 - t) * x1 + t * x2
        y = (1- t)*y1 + t*y2
        draw_point((x, y))

    draw_point(p2)
    pass


# 밑에 교수님 코드 함수
def draw_circle():
    t = 0.0

    # 원 그리기
    r = 200
    # math.pi = 3.141592...... 증가량이 정확하지 않아서 점 찍히는 곳이 바퀴마다 다름
    while t <= 4 * math.pi:  # t <= 4이므로 두 바퀴
        x = r * math.cos(t)
        y = r * math.sin(t)
        t += (math.pi / 10)    # 0.3씩 돌리므로 찍히는 바퀴가 돌아올 때마다 같음
        draw_point((x, y))

def draw_shape():

    # k = 0.5
    a = 100
    b = 200

    # k = 1.7
    a = 340
    b = 200

    # k = 2.5
    a = 500
    b = 200

    # k = 0.25
    a = 50
    b = 200

    t = 0.0

    # math.pi = 3.141592...... 증가량이 정확하지 않아서 점 찍히는 곳이 바퀴마다 다름
    while t <= 8 * math.pi:
        x = (a-b)*math.cos(t) + b*math.cos(t*(a/b-1))
        y = (a-b)*math.sin(t) - b*math.sin(t*(a/b-1))
        t += (math.pi / 40)  # 0.3씩 돌리므로 찍히는 바퀴가 돌아올 때마다 같음
        draw_point((x, y))


prepare_turtle_canvas()

draw_shape()

# draw_line((-0, 50), (100, 50))

turtle.done()
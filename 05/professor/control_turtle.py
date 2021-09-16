import turtle

def run_turtle(deg, dist):
    turtle.setheading(deg)
    turtle.forward(dist)
    turtle.stamp()


def move_up():
    run_turtle(90, 50)
    print('UP')

def move_right():
    run_turtle(0, 50)
    print('RIGHT')

def move_down():
    run_turtle(270, 50)
    print('DOWN')

def move_left():
    run_turtle(180, 50)
    print('LEFT')

def finish():
    turtle.bye()    


turtle.shape('turtle')
turtle.stamp()

turtle.onkey(finish, 'Escape')
turtle.onkey(move_up, 'w')
turtle.onkey(move_right, 'd')
turtle.onkey(move_down, 's')
turtle.onkey(move_left, 'a')

turtle.listen()
turtle.mainloop()
'''루프를 안 하면 엄밀히 따졌을 때 끝날 수 있음'''

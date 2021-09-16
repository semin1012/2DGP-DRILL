import turtle

center_list = [
    (200, 200, 50),
    (-200, -200, 30),
    (100, 100, 50)
]

for x, y, r in center_list:
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(r)
    turtle.write((x,y))


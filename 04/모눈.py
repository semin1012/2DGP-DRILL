import turtle


# draw horizontal lines

x = 0

while x <= 500:
    turtle.penup()
    turtle.goto(x, -100)
    turtle.pendown()
    turtle.goto(x, 400)
    x += 100
    
#가로줄 그리기

y= -100

while y <= 400:
    turtle.penup()
    turtle.goto(0, y)
    turtle.pendown()
    turtle.goto(500, y)
    y += 100


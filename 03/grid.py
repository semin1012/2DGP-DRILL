import turtle

count = 5
count2 = 5
x = -200
y = 200

while ( count > 0 ):
    turtle.penup()
    turtle.goto(x, y)
    while( count2 > 0 ):
        turtle.pendown()
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        count2 -= 1
    y -= 100
    count2 = 5
    count -= 1

turtle.exitonclick()
    

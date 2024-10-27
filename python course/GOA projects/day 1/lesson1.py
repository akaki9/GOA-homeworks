from turtle import *

width(8)
speed(50)
color("green")

#square

forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

#door

forward(70)
color("blue")
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)

penup()
goto(200, 200)
pendown()

color("purple")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#window left

penup()
goto(30, 170)
pendown()
width(6)
color("red")
begin_fill()
left (30)
forward (40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

#window right

penup()
goto(130, 170)
pendown()
width(6)
color("red")
begin_fill()
left (90)
forward (40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()



exitonclick()
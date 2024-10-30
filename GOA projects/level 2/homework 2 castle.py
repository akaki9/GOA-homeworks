from turtle import *

width (8)
speed(100)
penup()
goto(-450, -200)
pendown()

color ("grey")
forward (100)
left(90)
forward(400)
left(90)
forward(100)
left(90)
forward(400)

penup()
goto(-400, -200)
pendown()


left(90)
forward(800)
left(90)
forward(400)
left(90)
forward(100)
left(90)
forward(400)


penup()
goto(-450, 200)
pendown()


#ROOF 1
begin_fill()
left(90)
forward(100)
forward(20)
left(120)
forward(140)
left(120)
forward(140)
left(120)
forward(20)
end_fill()


penup()
goto(300, 200)
pendown()

#ROOF 2
begin_fill()
forward(100)
forward(20)
left(120)
forward(140)
left(120)
forward(140)
left(120)
forward(20)
end_fill()


right(90)
forward(120)
right(90)


forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

right(90)
forward(50)

penup()
goto(-150, 90)
pendown()


right(90)
forward(150)


right(90)

color("salmon")
begin_fill()
forward(250)
right(90)
end_fill()
color("grey")
forward(160)


penup()
goto(100, 240)
pendown()

color("salmon")
begin_fill()
left(90)
forward(20)

penup()
goto(-150, 240)
pendown()

left(180)
forward(20)

right(130)
forward(225)

right(100)
forward(225)
end_fill()

penup()
goto(-110, -200)
pendown()

width(9)
color("sienna")
begin_fill()
left(140)
forward(180)
right(90)
forward(180)
right(90)
forward(180)
end_fill()



exitonclick()
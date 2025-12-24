from turtle import*
hideturtle()
bgcolor("black")
speed("fastest")

# Background
up()
goto(0, -199)
down()
begin_fill()
fillcolor("#442905")
circle(198.5, 360)
end_fill()

# hee
width(2)
color("#EAEA11")
up()
goto(0, -198)
down()
circle(197, 360)

up()
goto(4, -191)
down()

for x in range(36):
    circle(150, 10)
    left(90)
    forward(7)
    left(90)
    forward(7)
    right(90)
    forward(7)
    right(90)
    forward(7)
    left(90)
    forward(7)
    right(90)
    forward(7)
    right(90)
    forward(21)
    left(90)

up()
goto(5, -165)
circle(130, 4.5)
down()

for x in range(36):
    circle(130, 10)
    right(90)
    forward(18.3)
    left(90)
    forward(6)
    left(90)
    forward(6)
    right(90)
    forward(6)
    left(90)
    forward(6)
    left(90)
    forward(6)
    right(90)
    forward(6)
    right(90)

# Tenger
up()
goto(11, -158)
circle(130, -4.5)
down()
begin_fill()
circle(158, 360)
fillcolor("#180985")
end_fill()

# chandmani
width(2)
colors = ["#17AD06", "#1A56C4", "red"]
pos = [(4, 100), (-54, 0), (64, 0)]

for (x, y), col in zip(pos, colors):
    up()
    goto(x, y)
    down()
    begin_fill()
    fillcolor(col)
    right(130)
    forward(48)
    circle(40, 270)
    right(10)
    forward(41)
    right(130)
    end_fill()

colors = ["#4ED72A", "#3286D6", "#FA2C45"]
pos = [(4, 100), (-54, 0), (64, 0)]

for (x, y), col in zip(pos, colors):
    up()
    goto(x, y)
    down()
    begin_fill()
    fillcolor(col)
    right(130)
    forward(36)
    circle(30, 270)
    right(10)
    forward(30)
    right(130)
    end_fill()

colors = ["#3EEB3B", "#6AACDF", "#FD426F"]
pos = [(4, 100), (-54, 0), (64, 0)]

for (x, y), col in zip(pos, colors):
    up()
    goto(x, y)
    down()
    begin_fill()
    fillcolor(col)
    right(130)
    forward(24)
    circle(20, 270)
    right(10)
    forward(18)
    right(130)
    end_fill()

done()

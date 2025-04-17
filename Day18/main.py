from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()

screen.colormode(255)

color_list = [(197, 138, 158), (225, 213, 204), (182, 162, 139), (153, 73, 104), (182, 93, 128), (150, 177, 186)]
timmy.speed("slow")
timmy.hideturtle()
y_position = 0
for i in range(10):
    for j in range(10):
        timmy.dot(13, random.choice(color_list))
        timmy.penup()
        timmy.forward(36)
    y_position += 30
    timmy.teleport(x=0, y=y_position)

screen.exitonclick()


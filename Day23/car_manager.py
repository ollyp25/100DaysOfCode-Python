from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.color(random.choice(COLORS))
        self.speed = STARTING_MOVE_DISTANCE
        y_cor = random.randint(-200, 240)
        x_cor = random.randint(-280, 320)
        self.setposition(x_cor, y_cor)

    def move_car(self):
        x_cor = self.xcor() - self.speed
        self.goto(x_cor, self.ycor())

    def reset(self):
        y_cor = random.randint(-200, 240)
        self.setposition(320, y_cor)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT





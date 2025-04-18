from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setposition(position)

    def go_up(self):
        y_cor = self.ycor() + 20
        self.setposition(self.xcor(), y=y_cor)

    def go_down(self):
        y_cor = self.ycor() - 20
        self.setposition(self.xcor(), y=y_cor)

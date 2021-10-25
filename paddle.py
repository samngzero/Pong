from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.setheading(90)
        self.turtlesize(0.5, 3, 1)
        self.color("white")
        self.penup()
        self.speed(0)

    def set(self, x):
        self.goto(x, 0)

    def up(self):
        self.fd(20)

    def down(self):
        self.back(20)

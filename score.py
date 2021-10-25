from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self,screen_width):
        super().__init__()
        self.screen_width=screen_width
        self.p1=0
        self.p2=0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed(0)

    def draw_line(self):
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed(0)
        self.goto(0,-self.screen_width)
        self.setheading(90)
        self.pensize(5)
        while self.ycor()<240:
            self.pendown()
            self.fd(15)
            self.penup()
            self.fd(12)

    def draw_score(self):
        self.goto(-40,self.screen_width/2-40)
        self.write(f"{self.p1}", False, "center", ("Arial", 30, "normal"))
        self.goto(40, self.screen_width / 2 - 40)
        self.write(f"{self.p2}", False, "center", ("Arial", 30, "normal"))

    def score_p1(self):
        self.p1+=1
        self.clear()
        self.draw_score()

    def score_p2(self):
        self.p2+=1
        self.clear()
        self.draw_score()



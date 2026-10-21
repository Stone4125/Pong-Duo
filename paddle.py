from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position_x):
        super().__init__()
        self.shape("square")
        self.penup()
        self.position_x = position_x
        self.create_paddle(position_x)

    def create_paddle(self, position):
            self.shapesize(5, 1)
            self.color("white")
            self.teleport(position, 0)


    def up(self):
        self.sety(self.ycor() + 20)

    def down(self):
        self.sety(self.ycor() - 20)
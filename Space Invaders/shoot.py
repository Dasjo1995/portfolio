from turtle import Turtle


class Shoot(Turtle):

    def __init__(self):
        super().__init__()
        self.y_move = 1
        self.list = []


    def shots(self):
        self.new_turtle = Turtle()
        self.new_turtle.color("white")
        self.new_turtle.shape("circle")
        self.new_turtle.penup()
        self.new_turtle.hideturtle()
        self.list.append(self.new_turtle)
        print(self.list)



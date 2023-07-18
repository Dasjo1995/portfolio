from turtle import Turtle



class Aliens(Turtle):
    def __init__(self):
        super().__init__()
        self.list = []
        self.hideturtle()
        self.penup()
        self.position_blocks()



    def position_blocks(self):
        x_coord = -345
        for block in range(0, 9):
            new_block = Turtle()
            new_block.shape("square")
            new_block.shapesize(stretch_wid=2, stretch_len=3)
            new_block.penup()
            new_block.color("yellow")
            new_block.goto(x_coord, 230)
            self.list.append((new_block))
            x_coord += 85




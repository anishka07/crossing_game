from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
    
    def move(self):
        self.fd(MOVE_DISTANCE)

    def reach_finish(self):
        if self.ycor() == FINISH_LINE_Y: return True 
        else: return False
    
    def reset_position(self):
        self.goto(STARTING_POSITION)
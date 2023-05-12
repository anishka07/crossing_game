from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_cars(self):
        if random.randint(1,6) == 2:
            new_car = Turtle('square')
            new_car.shape('square')
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            y_cor = random.randint(-250,250)
            new_car.goto(300,y_cor)
            self.all_cars.append(new_car)

    def car_move(self):
        for cars in self.all_cars:
            cars.setheading(180)
            cars.fd(STARTING_MOVE_DISTANCE)
    
    def car_speed(self):
        for cars in self.all_cars:
            cars.setheading(180)
            new_speed = STARTING_MOVE_DISTANCE+MOVE_INCREMENT
            cars.fd(new_speed)
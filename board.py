from sense_hat import SenseHat
import time
import random

class Board():
    def __init__(self):
        self.sense = SenseHat()
        self.walls = self.set_walls()
        self.food = self.set_food()
        self.player = (1,1) #change to player class once created
    
    def set_walls(self):
        walls = set()
        ##set boarder walls
        for x in range(8):
            walls.add((0,x))
            walls.add((7,x))
            walls.add((x, 0))
            walls.add((x, 7))

        #add obstical
        walls.add((3,3))
        walls.add((4,3))
        walls.add((4,4))
        walls.add((4,5))
        
        return walls

    def get_walls(self)
        return self.walls

    def set_food(self):
        food = set()
        for i in range(5):
            pos = (random.randint(0,8), random.randint(0,8))
            if pos not in self.walls:
                food.add(pos)
        return food
    
    def get_food(self):
        return self.food

    def display_walls(self):
        wall_colour = (255, 255, 255)
        for pos in self.walls:
            self.sense.set_pixel(pos[0], pos[1], wall_colour)

    def display_food(self):
        food_colour = (0, 0, 255)
        for pos in self.food:
            self.sense.set_pixel(pos[0], pos[1], food_colour)

    def clear_display(self):
        self.sense.clear()

    def display_board(self):
        self.display_walls()
        self.display_food()


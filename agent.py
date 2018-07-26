from sense_hat import SenseHat

class Agent():
    
    def __init__(self, board, colour, position):
        self.board = board
        self.position = position
        self.colour = colour
        self.sense = SenseHat()       
 
    def get_position(self):
        return self.position

    def get_position_as_list(self):
        return list(self.position)

    def remove_pos(self):
       self.sense.set_pixel(self.position[0], self.position[1], (0, 0, 0)) 
    
    def valid_move(self):
        return False
    
    def get_move(self):
        return None
        

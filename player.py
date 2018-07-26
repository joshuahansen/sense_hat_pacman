from agent import Agent
import time
class Direction():
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'
    MIDDLE = 'middle'
    PRESSED = 'pressed'
    RELEASED = 'released'

    
class Player(Agent):

    def __init__(self, board, colour, position):
        super().__init__(board, colour, position)

    def valid_move(self, pos, new_pos):
        move_error = (255, 0, 0)
        if new_pos in self.board.walls:
            #Flash error colour
            self.sense.set_pixel(pos[0], pos[1], move_error)
            time.sleep(0.1)
            self.sense.set_pixel(pos[0], pos[1], (0, 0, 0))
            time.sleep(0.1)
            return False
        else:
            return True

    def get_move(self):
        for event in self.sense.stick.get_events():
            if event.direction == Direction.MIDDLE and event.action == Direction.PRESSED:
                break
            elif event.direction == Direction.UP and event.action == Direction.PRESSED:
                self.remove_pos()
                pos = self.get_position_as_list()
                new_pos = (pos[0], pos[1]-1)

                if self.valid_move(self.get_position(), new_pos):
                    self.position = new_pos
                break
            elif event.direction == Direction.DOWN and event.action == Direction.PRESSED:
                self.remove_pos()
                pos = self.get_position_as_list()
                new_pos = (pos[0], pos[1]+1)

                if self.valid_move(self.get_position(), new_pos):
                    self.position = new_pos
                break
            elif event.direction == Direction.RIGHT and event.action == Direction.PRESSED:
                self.remove_pos()
                pos = self.get_position_as_list()
                new_pos = (pos[0]+1, pos[1])

                if self.valid_move(self.get_position(), new_pos):
                    self.position = new_pos
                break
            elif event.direction == Direction.LEFT and event.action == Direction.PRESSED:
                self.remove_pos()
                pos = self.get_position_as_list()
                new_pos = (pos[0]-1, pos[1])

                if self.valid_move(self.get_position(), new_pos):
                    self.position = new_pos
                break

    def display_player(self):
        self.sense.set_pixel(self.get_position()[0], self.get_position()[1], self.colour)

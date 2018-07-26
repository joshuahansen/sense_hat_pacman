from agent import Agent
import time

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
            if event.direction == 'middle' and event.action == 'pressed':
                break
            elif event.direction == 'up' and event.action == 'pressed':
                self.remove_pos()
                pos = self.get_position_as_list()
                new_pos = (pos[0], pos[1]-1)

                if self.valid_move(self.get_position(), new_pos):
                    self.position = new_pos
                self.sense.set_pixel(self.get_position()[0], self.get_position()[1], self.colour)
                break
            elif event.direction == 'down' and event.action == 'pressed':
                self.remove_pos()
                pos = self.get_position_as_list()
                new_pos = (pos[0], pos[1]+1)

                if self.valid_move(self.get_position(), new_pos):
                    self.position = new_pos
                self.sense.set_pixel(self.get_position()[0], self.get_position()[1], self.colour)
                break
            elif event.direction == 'right' and event.action == 'pressed':
                self.remove_pos()
                pos = self.get_position_as_list()
                new_pos = (pos[0]+1, pos[1])

                if self.valid_move(self.get_position(), new_pos):
                    self.position = new_pos
                self.sense.set_pixel(self.get_position()[0], self.get_position()[1], self.colour)
                break
            elif event.direction == 'left' and event.action == 'pressed':
                self.remove_pos()
                pos = self.get_position_as_list()
                new_pos = (pos[0]-1, pos[1])

                if self.valid_move(self.get_position(), new_pos):
                    self.position = new_pos
                self.sense.set_pixel(self.get_position()[0], self.get_position()[1], self.colour)
                break

    def display_player(self):
        self.sense.set_pixel(self.get_position()[0], self.get_position()[1], self.colour)

from sense_hat import SenseHat
import time

class Pi_game():

    def __init__(self):
        self.sense = SenseHat()
        self.walls = self.set_walls()
        self.player = (1, 1)
        self.player_colour = (0, 255, 0)

    def set_walls(self):
        walls = set()
        for x in range(8):
            walls.add((0, x))
            walls.add((7, x))

        for x in range(8):
            walls.add((x, 0))
            walls.add((x, 7))

        walls.add((3,3))
        walls.add((4,3))
        walls.add((4,4))
        walls.add((4,5))

        return walls

    def display_walls(self):
        wall_colour = (255, 255, 255)
        for x in self.walls:
            self.sense.set_pixel(x[0], x[1], wall_colour)

    def valid_move(self, pos, new_pos):
        move_error = (255, 0, 0)
        if new_pos in self.walls:
            for i in range(3):
                self.sense.set_pixel(pos[0], pos[1], move_error)
                time.sleep(0.1)
                self.sense.set_pixel(pos[0], pos[1], (0, 0, 0))
                time.sleep(0.1)
            return False
        else:
            return True

    def play(self):
        play_game = True
        
        self.display_walls()

        while play_game:

            self.sense.set_pixel(self.player[0], self.player[1], self.player_colour)

            for event in self.sense.stick.get_events():
                if event.direction == 'middle' and event.action == 'pressed':
                    play_game = False
                    break
                elif event.direction == 'up' and event.action == 'pressed':
                    self.sense.set_pixel(self.player[0], self.player[1], (0,0,0))
                    player_pos = list(self.player)
                    new_pos = (player_pos[0], player_pos[1]-1)
                    
                    if self.valid_move(self.player, new_pos):
                        self.player = new_pos
                    
                    self.sense.set_pixel(self.player[0], self.player[1], self.player_colour)
                    break
                elif event.direction == 'down' and event.action == 'pressed':
                    self.sense.set_pixel(self.player[0], self.player[1], (0,0,0))
                    player_pos = list(self.player)
                    new_pos = (player_pos[0], player_pos[1]+1)
                    
                    if self.valid_move(self.player, new_pos):
                        self.player = new_pos
                    
                    self.sense.set_pixel(self.player[0], self.player[1], self.player_colour)
                    break
                elif event.direction == 'right' and event.action == 'pressed':
                    self.sense.set_pixel(self.player[0], self.player[1], (0,0,0))
                    player_pos = list(self.player)
                    new_pos = (player_pos[0]+1, player_pos[1])
                    
                    if self.valid_move(self.player, new_pos):
                        self.player = new_pos
                    
                    self.sense.set_pixel(self.player[0], self.player[1], self.player_colour)
                    break
                elif event.direction == 'left' and event.action == 'pressed':
                    self.sense.set_pixel(self.player[0], self.player[1], (0,0,0))
                    player_pos = list(self.player)
                    new_pos = (player_pos[0]-1, player_pos[1])

                    if self.valid_move(self.player, new_pos):
                        self.player = new_pos
                    
                    self.sense.set_pixel(self.player[0], self.player[1], self.player_colour)
                    break

        self.sense.clear()

game = Pi_game()
game.play()

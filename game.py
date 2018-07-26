from sense_hat import SenseHat
import time
import random
from board import Board
from player import Player

class Game():
    def __init__(self):
        self.board = Board()
        self.player = Player(self.board, (0, 255, 0), (1, 1))

    def display_score(self):
        sense = SenseHat()
        selse.clear()
        sense.show_message('Score: {self.player.score}') 

    def play(self):
        self.board.display_board()
        self.player.display_player()

        while self.board.has_food():
            self.player.get_move()
            self.player.display_player()
        
        self.display_score()
    
    def reset(self):
        self.board.clear_display()


game = Game()

game.reset()
game.play()

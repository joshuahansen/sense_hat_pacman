from sense_hat import SenseHat
import time
import random
from board import Board
from player import Player

class Game():
    def __init__(self):
        self.board = Board()
        self.player = Player(self.board, (0, 255, 0), (1, 1))

    def play(self):
        self.board.display_board()
        self.player.display_player()

        while True:
            self.player.get_move()

    def reset(self):
        self.board.clear_display()

game = Game()

game.reset()
game.play()

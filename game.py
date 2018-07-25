from sense_hat import SenseHat
import time
import random
import Board
import Player

class Game():
    def __init__(self):
        self.board = Board()
        self.player = Player((0, 255, 0), (1, 1))

    def play():
        self.board.display_board()
        self.player.display_player()

        while True:
            self.player.get_move

game = Game()

game.play()

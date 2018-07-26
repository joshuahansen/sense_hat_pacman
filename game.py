from sense_hat import SenseHat
import Board
import Player

class Game():
    def __init__(self):
        self.board = Board()
        self.player = Player((0, 255, 0), (1, 1))

    def display_score(self):
        sense = SenseHat()
        sense.show_message('Score: {self.player.score}') 

    def play():
        self.board.display_board()
        self.player.display_player()

        while self.board.has_food():
            self.player.get_move

        self.display_score()

game = Game()

game.play()

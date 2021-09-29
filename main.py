import Player
import Board
import Game

"""
This is a game of TicTacToe
"""

my_board = Board.Board()
my_player = Player.Player()
my_game = Game.Game()
my_game.play(my_board, my_player)


from Player import Player
from Player import my_board
from Player import win_combinations
from Player import the_board
from Player import X
from Player import O

"""
This is a game of TicTacToe
"""


my_player = Player()

while True:
    my_board.display_board()
    my_player.enter_input()
    list_numbers_with_character = my_board.winning_positions(X)
    if my_board.winner(win_combinations, list_numbers_with_character, X):
        my_board.display_board()
        break
    flat = [i for sublist in the_board for i in sublist]
    if set(flat) == {X, O}:
        print("The game is finished")
        break
    my_player.opponents_move()
    list_numbers_with_character = my_board.winning_positions(O)
    if my_board.winner(win_combinations, list_numbers_with_character, O):
        break

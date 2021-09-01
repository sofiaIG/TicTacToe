import Board
import Player

"""
This is a game of TicTacToe
"""

the_board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 4], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
X = "X"
O = "⬤"


my_board = Board.Board(the_board)
my_player = Player()
while True:
    my_board.display_board()
    my_player.Player.enter_input()
    if my_board.win_game(X) or my_board.winning_diagonally(X):
        my_board.display_board()
        break
    flat = [i for sublist in the_board for i in sublist]
    if set(flat) == {X, O}:
        print("The game is finished")
        break
    my_player.Player.opponents_move()
    list_numbers_with_character = my_board.winning_positions(O)
    if my_board.winner(win_combinations, list_numbers_with_character, O):
        break

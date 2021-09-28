import Player
import Board

"""
This is a game of TicTacToe
"""


my_player = Player.Player()
my_board = Board.Board()

while True:
    my_board.display_board()
    my_player.enter_input(my_board)
    list_numbers_with_character = my_board.winning_positions(my_board.X)
    if my_board.winner(my_board.X):
        my_board.display_board()
        break
    flat = [i for sublist in my_board.board for i in sublist]
    if set(flat) == {my_board.X, my_board.O}:
        print("The game is finished")
        break
    my_player.opponents_move(my_board)
    list_numbers_with_character = my_board.winning_positions(my_board.O)
    if my_board.winner(my_board.O):
        break

"""
This is a game of TicTacToe
"""

import Board
import random

X = "X"
O = "⬤"
the_board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0,3,4],[1,4,7], [2,5,8],[0,4,8],[2,4,6]]

# my_board = Board(the_board) Not sure why but I am not deleting this line just yet
my_board = Board.Board(the_board)


def enter_input():
    """This function is used to get players decision and place it on the board"""
    board_user = my_board.remove_squares_with_x()
    flat_board_user = [i for sublist in board_user for i in sublist]
    users_choice = int(input("\n Please add a number from 0 to 8: "))
    my_board.value = users_choice
    while users_choice not in flat_board_user:
        users_choice = int(input(
            "\nPlease only enter numbers from 0-8 that has not been selected already):"))
    my_board.adding_decision_into_board(users_choice, X)


def opponents_move():
    """This function is used to get the user's move and add it into the board"""
    board_without_x_o = my_board.remove_squares_with_x()
    flat_board = [x for sublist in board_without_x_o for x in sublist]
    number_selected = random.choice(flat_board)
    my_board.value = number_selected
    print("\nThe opponent has selected: ")
    my_board.adding_decision_into_board(number_selected, O)


while True:
    my_board.display_board()
    enter_input()
    if my_board.win_game(X) or my_board.winning_diagonally(X):
        my_board.display_board()
        break
    flat = [i for sublist in the_board for i in sublist]
    if set(flat) == {X, O}:
        print("The game is finished")
        break
    opponents_move()
    if my_board.win_game(O) or my_board.winning_diagonally(O):
        my_board.display_board()
        break
    my_board.win_game(O)

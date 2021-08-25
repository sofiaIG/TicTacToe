"""
This is a game of TicTacToe
"""

import random

X = "X"
O = "O"


def display_board(board):
    """
    This function in printing the board with its current values
    """
    for i in range(0, 3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|   {}   |   {}   |   {}   |".format(board[i][0], board[i][1], board[i][2]))
    print("+-------+-------+-------+")


def remove_squares_with_x(board):
    "This is a function will create a board that only has squares that are not selected by X and O"
    board_decision_removed = [[i for i in j if isinstance(i, int)] for j in board]
    return board_decision_removed


def enter_input(board):
    "This function is used to get players decision and place it on the board"
    board_user = remove_squares_with_x(board)
    flat_board_user = [i for sublist in board_user for i in sublist]
    users_choice = int(input("\n Please add a number from 0 to 8: "))
    while users_choice not in flat_board_user:
        users_choice = int(input(
            "\nPlease only enter numbers from 0-8 that has not been selected already):"))
    adding_decision_into_board(users_choice, board, X)


def opponents_move(board):
    """This function is used to get the user's move and add it into the board"""
    board_without_x_o = remove_squares_with_x(board)
    if len(board_without_x_o) == 0:
        print("You have finished the game")
    else:
        flat_board = [x for sublist in board_without_x_o for x in sublist]
        number_selected = random.choice(flat_board)
        print("\nThe opponent has selected: ")
        adding_decision_into_board(number_selected, board, O)


def win_game(board, character):
    """
    This function in used to decide who is winning. The functionality
    of it is limited to vertical and horizontal winning
    """
    position_j = -1
    list_vertically = []
    list_diagonally = []
    for i in board:
        if set(i) == {character}:
            print(f"{character} has won!")
            return True
        for j in enumerate(i):
            if j[-1] == character:
                if position_j == -1:
                    position_j = j[0]
                elif position_j == j[0]:
                    list_vertically.append(j[-1])
    if len(list_diagonally) == 2 or len(list_vertically) == 2:
        print(f"{character} wins")
        return True
    else:
        return False


def winning_diagonally(board, character):
    """
    This function in used to decide who is winning. The functionality
    of it is limited to diagonal winning
    """
    number = 0
    list_for_1st_loop = []
    list_for_2st_loop = []
    for i in board:
        for _ in i:
            if i[number] == character:
                list_for_1st_loop.append(1)
                if number <= 2:
                    number += 1
                    break
    if len(list_for_1st_loop) == 3:
        print(f"{character} wins")
        return True
    else:
        number_1 = 2
        for i in board:
            for _ in i:
                if i[number_1] == character:
                    list_for_2st_loop.append(1)
                if number_1 >= 0:
                    number_1 -= 1
                    break
    if len(list_for_2st_loop) == 3:
        print(f"{character} wins")
        return True


def adding_decision_into_board(value, board, character):
    """
    Add a player's decision to the board and return the updated board
    """
    number = -1  # Creating number as I can not use i for index so I am replacing it with number
    for i in board:
        number += 1
        for j in i:
            index = i.index(j)
            if board[number][index] == value:
                board[number][index] = character
                break
    return board


the_board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
while True:
    display_board(the_board)
    enter_input(the_board)
    if win_game(the_board, X) or winning_diagonally(the_board, X):
        display_board(the_board)
        break
    flat = [i for sublist in the_board for i in sublist]
    if set(flat) == {X, O}:
        print("The game is finished")
        break
    opponents_move(the_board)
    if win_game(the_board, O) or winning_diagonally(the_board, O):
        display_board(the_board)
        break
    win_game(the_board, O)

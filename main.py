"""
This is a game of TicTacToe
"""

import random

X = "X"
O = "⬤"
the_board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]


class Board:
    def __init__(self, board):
        self.board = board
        self.value = None

    def display_board(self):
        """
        This function in printing the board with its current values
        """
        for i in range(0, 3):
            print("+-------+-------+-------+")
            print("|       |       |       |")
            print("|   {}   |   {}   |   {}   |".format(self.board[i][0], self.board[i][1], self.board[i][2]))
        print("+-------+-------+-------+")

    def remove_squares_with_x(self):
        """This is a function will create a board that only has squares that are not selected by X and O"""
        board_decision_removed = [[i for i in j if isinstance(i, int)] for j in self.board]
        return board_decision_removed

    def adding_decision_into_board(self, value, character):
        """
        Add a player's decision to the board and return the updated board
        """
        number = -1  # Creating number as I can not use i for index so I am replacing it with number
        for i in self.board:
            number += 1
            for j in i:
                index = i.index(j)
                if self.board[number][index] == self.value:
                    self.board[number][index] = character
                    break
        return self.board

    def win_game(self, character):
        """
        This function in used to decide who is winning. The functionality
        of it is limited to vertical and horizontal winning
        """
        position_j = -1
        list_vertically = []
        list_diagonally = []
        for i in self.board:
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

    def winning_diagonally(self, character):
        """
        This function in used to decide who is winning. The functionality
        of it is limited to diagonal winning
        """
        number = 0
        list_for_1st_loop = []
        list_for_2st_loop = []
        for i in self.board:
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
            for i in self.board:
                for _ in i:
                    if i[number_1] == character:
                        list_for_2st_loop.append(1)
                    if number_1 >= 0:
                        number_1 -= 1
                        break
        if len(list_for_2st_loop) == 3:
            print(f"{character} wins")
            return True


my_board = Board(the_board)


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

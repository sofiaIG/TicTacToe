from Board import Board
import random

the_board = [["X", "X", "⬤"], ["⬤", 4, 5], [6, 7, 8]]
win_combinations = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 4}, {1, 4, 7}, {2, 5, 8}, {0, 4, 8}, {2, 4, 6}]
X = "X"
O = "⬤"
my_board = Board(the_board, win_combinations)

class Player:


    def opponents_move(self):
        """This function is used to get the user's move and add it into the board"""
        number_selected = 0
        statement = True
        positions = my_board.winning_positions(X)
        for i in win_combinations:
            z = i.difference(set(positions))
            if len(z) == 1 and O not in i:
                number_selected = next(iter(z))
                statement = False
                break
        if statement is True:
            flat_board = [x for sublist in the_board for x in sublist]
            flat_board_without_decision = [x for x in flat_board if type(x) is int]
            number_selected = random.choice(flat_board_without_decision)
        my_board.adding_decision_into_board(number_selected, O)


    def enter_input(self):
        """This function is used to get players decision and place it on the board"""
        board_user = my_board.remove_squares_with_x()
        flat_board_user = [i for sublist in board_user for i in sublist]
        # users_choice = int(input("\n Please add a number from 0 to 8: "))
        users_choice = 4
        my_board.value = users_choice
        while users_choice not in flat_board_user:
            users_choice = int(input(
                "\nPlease only enter numbers from 0-8 that has not been selected already):"))
        my_board.adding_decision_into_board(users_choice, X)





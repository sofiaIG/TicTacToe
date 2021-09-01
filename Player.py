import Board

X = "X"
O = "⬤"
the_board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 4],[1, 4, 7], [2, 5, 8],[0, 4, 8],[2, 4, 6]]
my_board = Board.Board(the_board)

class Player:

    def enter_input(self):
        """This function is used to get players decision and place it on the board"""
        board_user = my_board.remove_squares_with_x()
        flat_board_user = [i for sublist in board_user for i in sublist]
        users_choice = int(input("\n Please add a number from 0 to 8: "))
        my_board.value = users_choice
        while users_choice not in flat_board_user:
            users_choice = int(input(
                "\nPlease only enter numbers from 0-8 that has not been selected already):"))
        my_board.adding_decision_into_board(users_choice, X)

    def opponents_move(self):
        """This function is used to get the user's move and add it into the board"""
        my_board.winning_positions()
        for i in win_combinations:
            z = i.difference(set(my_board))
            if len(z) == 1:
                number_selected = next(iter(z))
        my_board.adding_decision_into_board(number_selected, O)

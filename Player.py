import random


class Player:

    def opponents_move(self, board):
        """This function is used to get the user's move and add it into the board"""
        positions_x = board.character_positions(board.X)
        positions_y = board.character_positions(board.O)
        number_selected = -1
        flat_list = [item for items in board.board for item in items]
        # FIXME: This line below "knows" too much about the implementation of the board
        flat_board_without_decision = [i for i in flat_list if type(i) == int]

        for row in board.board:  # If in a win combo there are already 2 O. The set would be completed instead of blocking
            # move.
            set_row = set(row)
            if len(set_row) == 2 and board.O in set_row:
                for col in set_row:
                    if type(col) == int:
                        number_selected = col

        if number_selected == -1:  # If there are not already 2XO in win combo O should aim to complete the combo
            # instead
            for i in board.win_combinations:  # Blocking X
                intersection = i.intersection(positions_x)
                difference = i.difference(positions_x)
                try:
                    number_difference = next(iter(difference))
                except StopIteration:
                    print(f'{board.O} wins')

                if len(intersection) == 2 and number_difference not in positions_y:
                    if number_difference in flat_board_without_decision:
                        number_selected = number_difference
                        break
        if number_selected == -1:
            number_selected = random.choice(flat_board_without_decision)

        board.adding_decision_into_board(number_selected, board.O)

    def enter_input(self, board):
        """This function is used to get players decision and place it on the board"""
        board_user = board.remove_squares_with_x()
        flat_board_user = [i for sublist in board_user for i in sublist]
        users_choice = int(input("\n Please add a number from 0 to 8: "))
        board.value = users_choice
        while users_choice not in flat_board_user:
            users_choice = int(input(
                "\nPlease only enter numbers from 0-8 that has not been selected already):"))
        board.adding_decision_into_board(users_choice, board.X)

class Board:
    def __init__(self, board, winning_combo_set):
        self.board = board
        self.value = None
        self.winning_combo_set = winning_combo_set

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

    def winning_positions(self, character):
        loop_number = -1
        count = -1
        list_of_selected_squares = 0
        for i in self.board:
            loop_number += 1
            for j in i:
                count += 1
                if j == character:
                    list_of_selected_squares.append(count)
        return list_of_selected_squares

    def winner(self, winning_combo_set, list_squares, character):
        self.list_squares = self.winning_positions(character)
        if set(list_squares) in winning_combo_set:
            print(f"{character} wins")
            return True
        else:
            return False


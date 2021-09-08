class Board:
    def __init__(self, board, winning_combo_set):
        self.board = board
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
        number_i = -1  #This has been amended. If bugs occur, refer back to github for history.
        for i in self.board:
            number_i += 1#This is to count rows
            count = -1#This is to count colums
            for _ in i:
                count += 1
                if _ == value:
                    self.board[number_i][count] = character
        return self.board



    def winning_positions(self, character):#This function is created to return a set that contains the indices of the character.
        loop_number = -1
        count = -1
        set_of_selected_squares = set()
        for i in self.board:
            loop_number += 1
            for j in i:
                count += 1
                if j == character:
                    set_of_selected_squares.add(count)
        return set_of_selected_squares

    def winner(self, winning_combo_set, set_squares, character):
        self.set_squares = self.winning_positions(character)
        if set_squares in winning_combo_set:
            print(f"{character} wins")
            return True
        else:
            return False


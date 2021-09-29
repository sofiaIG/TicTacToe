class Board:

    X = "X"
    O = "⬤"
    blank_board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    win_combinations = ({0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, {0, 4, 8}, {2, 4, 6})

    def __init__(self, board=blank_board):
        self.board = board

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


    def character_positions(self, character):
        """
        This function is created to return a set that contains the indices of the character.
        """
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

    def winner(self, character):
        set_squares = self.character_positions(character)
        for i in Board.win_combinations:
            i_intersection_set_sq = i.intersection(set_squares)
            if len(i_intersection_set_sq) == 3:
                print(f"{character} wins")
                return True




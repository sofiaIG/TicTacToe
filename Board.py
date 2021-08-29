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

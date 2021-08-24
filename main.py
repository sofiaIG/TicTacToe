import random

x = "X"
o = "O"
board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]


def display_board(board: list):
    "This function in printing the board with its current values"
    print("+-------+-------+-------+\n" "|       |       |       |\n"
          "|   {}   |   {}   |   {}   |\n"
          "|       |       |       |\n".format(board[0][0], board[0][1], board[0][2]), end="")
    print("+-------+-------+-------+\n" "|       |       |       |\n"
          "|   {}   |   {}   |   {}   |\n"
          "|       |       |       |\n".format(board[1][0], board[1][1], board[1][2]), end="")
    print("+-------+-------+-------+\n" "|       |       |       |\n"
          "|   {}   |   {}   |   {}   |\n""|       |       |       |\n"
          "+-------+-------+-------+".format(board[2][0], board[2][1], board[2][2]), end="")


def remove_squares_with_x(board):
    "This is a function will create a board that only has squares that are not selected by X and O"
    board_decision_removed = [[i for i in j if type(i) == int]for j in board]
    return board_decision_removed


def enter_input():
    "This function is used to get players decision and place it on the board"
    board_user = remove_squares_with_x(board)
    flat_board_user = [i for sublist in board_user for i in sublist]
    users_choice = int(input("\n Please add a number from 0 to 8: "))
    while users_choice not in flat_board_user:
        users_choice = int(input(
            "\nPlease only enter numbers from 0-8 that has not been selected already):"))
    adding_decision_into_board(users_choice, board, x)


def opponents_move():
    "This function is used to get the user's move and add it into the board"
    board_without_x_o = remove_squares_with_x(board)
    if len(board_without_x_o) == 0:
        "You have finished the game"
    else:
        flat = [x for sublist in board_without_x_o for x in sublist]
        number_selected = random.choice(flat)
        print("\nThe opponent has selected: ")
        adding_decision_into_board(number_selected, board, o)


def win_game(board, character):
    "This function in used to decide who is winning. The functionality of it is limited to vertical and horizontal winning "
    position_j = -1
    list_vertically = []
    list_diagonally = []
    number = 0
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
    number = 0
    list_for_1st_loop = []
    list_for_2st_loop = []
    for i in board:
        for j in i:
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
            for j in i:
                if i[number_1] == character:
                    list_for_2st_loop.append(1)
                if number_1 >= 0:
                    number_1 -= 1
                    break
    if len(list_for_2st_loop) == 3:
        print(f"{character} wins")
        return True


def adding_decision_into_board(value, board, character):
    number = -1  # Creating number as I can not use i for index so I am replacing it with number
    for i in board:
        number += 1
        for j in i:
            index = i.index(j)
            if board[number][index] == value:
                board[number][index] = character
                break
    return board


while True:
    display_board(board)
    enter_input()
    if win_game(board, x) == True or winning_diagonally(board, x) == True:
        display_board(board)
        break
    flat = [i for sublist in board for i in sublist]  # This is not working
    if set(flat) == {x, o}:
        print("The game is finished")
        break
    opponents_move()
    if win_game(board, o) == True or winning_diagonally(board, o) == True:
        display_board(board)
        break
    win_game(board, o)

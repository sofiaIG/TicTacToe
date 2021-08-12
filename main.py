values = [x for x in range(1,10)]
board =[]
x = "X"

for i in range(3):
    row = [x for x in range(3)]
    board.append(row)


def display_board(values):
    print("+-------+-------+-------+\n" "|       |       |       |\n""|   {}   |   {}   |   {}   |\n""|       |       |       |\n".format(values[0], values[1], values[2]), end = "")
    print("+-------+-------+-------+\n" "|       |       |       |\n""|   {}   |   {}   |   {}   |\n""|       |       |       |\n".format(values[3], values[4], values[5]), end = "")
    print("+-------+-------+-------+\n" "|       |       |       |\n""|   {}   |   {}   |   {}   |\n""|       |       |       |\n""+-------+-------+-------+".format(values[6], values[7], values[8]), end = "")


def enter_input():
    users_choice = int(input("\nPlease select a number: "))
    if users_choice == 1:
        board[0][0]=1
        values[0] = x
    elif users_choice == 2:
        board[0][1] = 2
        values[1] = x
    elif users_choice ==3:
        board[0][2] = 3
        values[2] = x
    elif users_choice ==4:
        board[1][0] = 4
        values[3] = x
    elif users_choice == 5:
        board[1][1] = 5
        values[4] = x
    elif users_choice == 6:
        board[1][2] = 6
        values[5] = x
    elif users_choice == 7:
        board[2][0] = 7
        values[6] = x
    elif users_choice == 8:
        board[2][1] = 8
        values[7] = x
    elif users_choice == 9:
        values[8] = x


display_board(values)
enter_input()
display_board(values)


def win():
    win_combinations = [{1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{1,5,9},{3,5,7}]
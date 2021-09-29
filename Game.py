class Game:


    def play(self, board, player):
        while True:
            board.display_board()
            player.enter_input(board)
            if board.winner(board.X):
                board.display_board()
                break
            flat = [i for sublist in board.board for i in sublist]
            if set(flat) == {board.X, board.O}:
                board.display_board()
                print("The game is finished")
                break
            player.opponents_move(board)
            if board.winner(board.O):
                board.display_board()
                break

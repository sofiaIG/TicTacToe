class Game:


    def play(self, board, player):
        while True:
            board.display_board()
            player.enter_input(board)
            if board.winner(board.X):
                board.display_board()
                break
            if board.finished_game() is True:
                board.display_board()
                break
            player.opponents_move(board)
            if board.winner(board.O):
                board.display_board()
                break
            if board.finished_game() is True:
                board.display_board()
                break

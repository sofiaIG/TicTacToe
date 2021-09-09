import unittest
import Board

class TestBoard(unittest.TestCase):


    win_combinations = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 4}, {1, 4, 7}, {2, 5, 8}, {0, 4, 8}, {2, 4, 6}]

    def test_win_x(self):
        """
        Test a few known board layouts to confirm winning calculation
        does the right thing
        """
        X = Board.Board().X
        O = Board.Board().O

        test_boards = (
                ((X, X, O),
                 (O, 4, 5),
                 (6, 7, 8), False),
                ((X, X, O),
                 (O, O, 5),
                 (X, 7, 8), False),
                ((X, X, O),
                 (X, O, O),
                 (X, 7, 8), True),
                ((X, X, X),
                 (O, 4, 5),
                 (6, 7, 8), True)
                )
        for i in range(len(test_boards)):
            the_board = Board.Board(test_boards[i][0:2])
            self.assertEqual(the_board.winner(X), test_boards[i][3])

if __name__ == '__main__':
    unittest.main()

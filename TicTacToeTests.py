import TicTacToe
import unittest


class DefaultBoardTests(unittest.TestCase):
    def setUp(self):
        self.board = TicTacToe.TTTBoard()

    def tearDown(self):
        self.board = None

    def test_default_num_rows(self):
        assert self.board.numRows == 3

    def test_default_num_cols(self):
        assert self.board.numCols == 3

    def test_default_values_are_none(self):
        for row in range(3):
            for col in range(3):
                assert self.board.getGridValue(row, col) == ' '

    def test_ability_to_set_grid_values(self):
        for row in range(3):
            for col in range(3):
                cantorPairingValue = .5 * (row + col) * (row + col) * (row + col + 1) + col
                self.board.setGridValue(row, col, cantorPairingValue)

        for row in range(3):
            for col in range(3):
                cantorPairingValue = .5 * (row + col) * (row + col) * (row + col + 1) + col
                assert self.board.getGridValue(row, col) == cantorPairingValue

    def test_print_blank_board(self):
        assert str(self.board) == "| | | |\n| | | |\n| | | |"

    def test_print_board_with_values(self):
        self.board.setGridValue(0, 0, 'x')
        self.board.setGridValue(0, 1, 'o')
        self.board.setGridValue(1, 1, 'o')
        self.board.setGridValue(1, 2, 'x')
        self.board.setGridValue(2, 0, 'x')
        self.board.setGridValue(2, 2, 'o')
        assert str(self.board) == "|x|o| |\n| |o|x|\n|x| |o|"


class DefaultGameTests(unittest.TestCase):
    def setUp(self):
        self.board = TicTacToe.TTTBoard()
        self.game = TicTacToe.TTTGame(self.board)

    def tearDown(self):
        self.board = None
        self.game = None

    def test_no_move_game(self):
        self.game.simulateGame([])
        assert self.game.winner == self.board.emptyCellValue
        assert self.game.isGameOver() == False

    def test_row_zero_win(self):
        moves = [0, 3, 1, 4, 2]
        self.game.simulateGame(self.game.unpackMoves(moves))
        assert self.game.isGameOver()
        assert self.game.winner == self.game.xPiece

    def test_row_one_win(self):
        moves = [8, 3, 2, 4, 1, 5]
        self.game.simulateGame(self.game.unpackMoves(moves))
        assert self.game.isGameOver()
        assert self.game.winner == self.game.oPiece

    def test_row_two_win(self):
        moves = [6, 2, 7, 1, 8]
        self.game.simulateGame(self.game.unpackMoves(moves))
        assert self.game.isGameOver()
        assert self.game.winner == self.game.xPiece

    def test_col_zero_win(self):
        moves = [1, 0, 2, 3, 8, 6]
        self.game.simulateGame(self.game.unpackMoves(moves))
        assert self.game.isGameOver()
        assert self.game.winner == self.game.oPiece

    def test_col_one_win(self):
        moves = [1, 0, 4, 2, 7]
        self.game.simulateGame(self.game.unpackMoves(moves))
        assert self.game.isGameOver()
        assert self.game.winner == self.game.xPiece

    def test_col_two_win(self):
        moves = [1, 2, 0, 5, 7, 8]
        self.game.simulateGame(self.game.unpackMoves(moves))
        assert self.game.isGameOver()
        assert self.game.winner == self.game.oPiece

    def test_diag_zero_win(self):
        moves = [0, 2, 4, 5, 8]
        self.game.simulateGame(self.game.unpackMoves(moves))
        assert self.game.isGameOver()
        assert self.game.winner == self.game.xPiece

    def test_diag_one_win(self):
        moves = [0, 2, 3, 4, 8, 6]
        self.game.simulateGame(self.game.unpackMoves(moves))
        assert self.game.isGameOver()
        assert self.game.winner == self.game.oPiece

    def test_draw_complete_game(self):
        moves = [0, 1, 2, 4, 3, 5, 7, 6, 8]
        self.game.simulateGame(self.game.unpackMoves(moves))
        assert self.game.isGameOver()
        assert self.game.winner == self.board.emptyCellValue

    def test_draw_incomplete_game(self):
        moves = [0, 1, 2, 4, 3, 5, 7, 6]
        self.game.simulateGame(self.game.unpackMoves(moves))
        assert not self.game.isGameOver()
        assert self.game.winner == self.board.emptyCellValue



unittest.main()

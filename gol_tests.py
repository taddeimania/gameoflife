import unittest
import gol
from gol import LifeNode
import mock

class LifeNodeTest(unittest.TestCase):

    def test_init_can_make_alive_or_dead_node(self):
        lifestates = [0,1]
        node = gol.LifeNode()
        self.assertIn(node.lifestate, lifestates)

    def test_life_node_returns_blank_space_if_dead(self):
        node = gol.LifeNode()
        node.lifestate = 0
        self.assertEqual(" ", str(node))

    def test_life_node_returns_X_if_alive(self):
        node = gol.LifeNode()
        node.lifestate = 1
        self.assertEqual("X", str(node))

class CreateBoardTest(unittest.TestCase):

    def setUp(self):
        self.board = gol.CreateBoard(3)
        self.copy_patch = mock.patch('copy.deepcopy')
        self.copy = self.copy_patch.start()

    def tearDown(self):
        self.copy_patch.stop()

    def test_generate_board_fills_board_with_life_nodes(self):
        self.board.generate_board()
        for idx, row in enumerate(self.board.BOARD):
            for idxx, cell in enumerate(row):
                self.assertIsInstance(self.board.BOARD[idx][idxx], LifeNode)

    @mock.patch('gol.CreateBoard.copy_board')
    def test_iterate_board_calls_copy_board_twice(self, copy_board):
        new_board = gol.CreateBoard(3)
        new_board.iterate_board()
        self.assertEqual(2, copy_board.call_count)

    @unittest.skip(True)
    @mock.patch('gol.CreateBoard.check_neighbors')
    def test_iterate_board_calls_check_neighbors(self, check_neighbors):
        pass

    @unittest.skip(True)
    @mock.patch('gol.CreateBoard.count_neighbors')
    def test_check_neighbors_calls_count_neighbors(self, count_neighbors):
        new_board = gol.CreateBoard(3)
        new_board.check_neighbors()

    def test_copy_board_calls_deep_copy(self):
        new_board = gol.CreateBoard(3)
        newer_board = new_board.copy_board(self.board.BOARD)
        self.copy.assert_called_once_with(self.board.BOARD)
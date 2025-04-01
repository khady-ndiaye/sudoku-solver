import unittest
from itertools import product
from script import SudokuGrid

class TestSudokuGrid(unittest.TestCase):

    def setUp(self):
        # Create an instance of SudokuGrid for each test
        self.sudoku = SudokuGrid()

    def test_is_valid(self):
        # Tests the validity of the `is_valid` method
        self.sudoku.grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        
        # Test with a valid number
        self.assertTrue(self.sudoku.is_valid(0, 2, 4))  # The box (0, 2) can take the 4
        # Test with an invalid number (already present on the same line)
        self.assertFalse(self.sudoku.is_valid(0, 2, 5))  # The box (0, 2) cannot take the 5

    def test_resolve_backtracking(self):
        # Tests whether the backtracking solution method correctly solves a given grid
        self.sudoku.grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        
        solved = self.sudoku.resolve_backtracking()  # Resolution with backtracking
        self.assertTrue(solved)  # Should return True if the Sudoku is solved
        self.assertEqual(self.sudoku.grid[0][2], 4)  # Check if box (0, 2) is filled with a 4

    def test_solve_brute_force(self):
        # Tests whether the brute force method correctly solves a given grid
        self.sudoku.grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        
        solved = self.sudoku.solve_brute_force()  # Solving with brute force
        self.assertTrue(solved)  # Should return True if the Sudoku is solved
        self.assertEqual(self.sudoku.grid[0][2], 4)  # Check if box (0, 2) is filled with a 4

if __name__ == "__main__":
    unittest.main()

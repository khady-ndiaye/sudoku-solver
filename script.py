# Class representing the Sudoku grid
class SudokuGrid:
    def __init__(self):
        # The Sudoku grid is initialized as a 9x9 matrix
        self.grid = [[0] * 9 for _ in range(9)]

    # Method to import and parse a grid from a file
    def import_grid(self, filename):
        with open(filename, "r") as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                self.grid[i] = [int(c) if c != "_" else 0 for c in line.strip()]

    # Method to display grid in terminal
    def show_grid(self):
        for row in self.grid:
            print(" ".join(str(num) if num != 0 else "_" for num in row))

    # Method to check if a digit is valid in a given position
    def is_valid(self, row, col, num):
        # Check line
        if num in self.grid[row]:
            return False
        # Check column
        for i in range(9):
            if self.grid[i][col] == num:
                return False
        # Check the 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.grid[i][j] == num:
                    return False
        return True


    # Method for solving the grid with the backtracking algorithm
    def resolve_backtracking(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:  
                    for num in range(1, 10):
                        if self.is_valid(row, col, num):
                            self.grid[row][col] = num
                            if self.resolve_backtracking():
                                return True
                            self.grid[row][col] = 0  
                    return False
        return True
    
    def resolve_backtracking(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0: 
                    for num in range(1, 10):
                        if self.is_valid(row, col, num):
                            self.grid[row][col] = num
                            print(f"Attempt from {num} to ({row}, {col})")  
                            self.show_grid()  
                            if self.resolve_backtracking():
                                return True
                            self.grid[row][col] = 0  
                            print(f"Go back to ({row}, {col})")
                    return False
        return True


    # Method to solve the grid with brute force
    def solve_brute_force(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0: 
                    for num in range(1, 10):
                        self.grid[row][col] = num
                        if self.solve_brute_force():
                            return True
                        self.grid[row][col] = 0  
                    return False
        return True

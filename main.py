import time
from script import SudokuGrid
from pygame_window import SudokuPygame

# Main function to run the program
def main():
    sudoku = SudokuGrid()
    
    # Import grid from text file
    sudoku.import_grid("sudoku4.txt")  
    
    # Display the initial grid in the terminal
    print("Initial grid:")
    sudoku.show_grid()
    
    # Solving Sudoku with the Backtracking Method
    print("\nResolution with backtracking:")
    start_time = time.time()
    if sudoku.resolve_backtracking():
        print("Solution found:")
        sudoku.show_grid()
    else:
        print("No solutions found.")
    print(f"Backtracking Execution Time : {time.time() - start_time:.5f} seconds")
    
    # Display the solved grid with Pygame
    # Creates an instance of SudokuDisplay
    sudoku_pygame = SudokuPygame(sudoku)
    # Display the grid with Pygame  
    sudoku_pygame.start_display()
     
    
    # Solving Sudoku with the Brute Force Method
    print("\nSolving Sudoku with the Brute Force Method:")
    sudoku.import_grid("sudoku4.txt")  
    start_time = time.time()
    if sudoku.solve_brute_force():
        print("Solution found:")
        sudoku.show_grid()
    else:
        print("No solutions found.")
    print(f"Brute Force Execution Time : {time.time() - start_time:.5f} seconds")
    
    # Display the solved grid with Pygame
    SudokuPygame(sudoku)
    

if __name__ == "__main__":
    main()
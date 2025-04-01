import time
from script import SudokuGrid
from pygame_window import SudokuPygame

# Menu in terminal for loading the sudoku grid 
def menu_terminal():
    print("\n--- Choosing a Sudoku grid ---")
    print("1. Grid 1")
    print("2. Grid 2")
    print("3. Grid 3")
    print("4. Grid 4")
    print("5. Grid 5")
    print("6. Quitter")
    
    grid_choice = input("Please choose a grid : ")

    return grid_choice

# Menu in the terminal to choose the resolution method.
def menu_terminal_resolution():
    print("\n--- Choose a resolution method ---")
    print("1. Backtracking Resolution")
    print("2. Brute Force Resolution")
    
    method_choice = input("Please choose the resolution method: ")

    return method_choice

# Main function to run the program
def main():
    """sudoku_pygame = SudokuPygame()   #####
    sudoku = SudokuGrid(sudoku_pygame) ###"""
    sudoku = SudokuGrid()
    
    #sudoku_pygame = SudokuPygame(sudoku) 
    # Menu in terminal to choose a grid
    print("Please choose a grid  :")
    grid_choice = menu_terminal()

    if grid_choice == '1':
        sudoku.import_grid("sudoku.txt")
    elif grid_choice == '2':
        sudoku.import_grid("sudoku2.txt")
    elif grid_choice == '3':
        sudoku.import_grid("sudoku3.txt")
    elif grid_choice == '4':
        sudoku.import_grid("sudoku4.txt")
    elif grid_choice == '5':
        sudoku.import_grid("evilsudoku.txt")
    elif grid_choice == '6':
        print("Thank you for using the Sudoku solver!")
        return
    else:
        print("Invalid choice!")
        return
    
    # Display the initial grid in the terminal
    print("Initial grid:")
    sudoku.show_grid()
    # Display the solved grid with Pygame
    """sudoku_pygame = SudokuPygame(sudoku)"""
    #sudoku_pygame.start_display()

    # Menu in terminal to choose a method
    method_choice = menu_terminal_resolution()
    if method_choice == '1':
        # Solving Sudoku with the Backtracking Method
        print("\nResolution with backtracking:")
        start_time = time.time()
        if sudoku.resolve_backtracking():
            print("Solution found:")
            sudoku.show_grid()
        else:
            print("No solutions found.")
        print(f"Backtracking Execution Time : {time.time() - start_time:.5f} seconds")
        method_choice = menu_terminal_resolution()
        if method_choice == '2':
            
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

    elif method_choice == '2':
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
    sudoku_pygame = SudokuPygame(sudoku)
    sudoku_pygame.start_display()

if __name__ == "__main__":
    main()
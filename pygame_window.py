import pygame
from config import *

# Function to display the Sudoku grid with Pygame
def display_grid_pygame(sudoku_grid):
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.SysFont('Arial', 40)
    
    
    
    while True:
        screen.fill((WHITE))

        # Draw the grid boxes
        for row in range(9):
            for col in range(9):
                x, y = col * cell_size, row * cell_size
                pygame.draw.rect(screen, (BLACK), (x, y, cell_size, cell_size), 2)
                if sudoku_grid.grid[row][col] != 0:
                    if sudoku_grid.initial_grid[row][col] == 0:
                        color = RED
                    else:
                        color = BLACK  
                    text = font.render(str(sudoku_grid.grid[row][col]), True, (color))
                    screen.blit(text, (x + 20, y + 10))
                
        # Draw the additional grid lines
        for i in range(1, 9):
            if i % 3 == 0:
                pygame.draw.line(screen, (BLACK), (0, i * cell_size), (540, i * cell_size), 4)  
                pygame.draw.line(screen, (BLACK), (i * cell_size, 0), (i * cell_size, 540), 4)  

                
            
        # Update the display
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
       

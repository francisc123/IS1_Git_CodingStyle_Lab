import pygame
import random

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
GRID_ROWS = 10
GRID_COLS = 10
CELL_SIZE = 50

def generate_random_grid():
    return [[(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 
             for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Procedural Color Grid (Press SPACE to Regenerate)")

    grid_colors = generate_random_grid()
    running = True

    while running:
        screen.fill((0, 0, 0))

        for row in range(GRID_ROWS):
            for col in range(GRID_COLS):
                rect_dimensions = (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, grid_colors[row][col], rect_dimensions)
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    grid_colors = generate_random_grid()

    pygame.quit()

if __name__ == "__main__":
    main()
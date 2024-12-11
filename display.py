import pygame
import numpy as np
import colorsys

# Constants
GRID_SIZE = 16  # 16x16 grid
CELL_SIZE = 40  # Size of each cell in pixels
SCREEN_SIZE = GRID_SIZE * CELL_SIZE
FPS = 30

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("16x16 LED Array Simulator")
clock = pygame.time.Clock()

# Function to generate a rainbow color
# Hue moves cyclically in HSV space, converted to RGB
def rainbow_color(step, total_steps):
    hue = (step / total_steps) % 1.0
    r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    return int(r * 255), int(g * 255), int(b * 255)

# Function to calculate the distance from the center of the grid
def distance_from_center(x, y):
    center_x, center_y = GRID_SIZE // 2, GRID_SIZE // 2
    return np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)


# Function to draw the grid with the pattern
def draw_grid_stripes(frame):
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            # Calculate color based on the frame and position
            color = rainbow_color((frame + y) % GRID_SIZE, GRID_SIZE)
            # Draw the cell
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect)
            # Draw the grid line
            pygame.draw.rect(screen, (0, 0, 0), rect, 6)

            # Function to draw the grid with the pattern
def draw_grid_circle(frame):
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            # Calculate distance from the center
            dist = distance_from_center(x, y)
            # Calculate color based on the distance and frame
            color = rainbow_color((frame + int(dist)) % GRID_SIZE, GRID_SIZE)
            # Draw the cell
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect)
            # Draw the grid line (black and thicker)
            pygame.draw.rect(screen, (0, 0, 0), rect, 6)

# Main loop
running = True
frame = 0  # Animation frame counter

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the grid with the current pattern
    draw_grid_circle(frame)

    # Update the display
    pygame.display.flip()

    # Increment the frame counter
    frame += 1

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()


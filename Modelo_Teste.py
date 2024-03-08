import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 1920, 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Protocolo Teste Mouse")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)

# Function to draw a circle
def draw_circle(surface, color, center, radius):
    pygame.draw.circle(surface, color, center, radius)

# Function to check if a point is inside a circle
def point_inside_circle(point, center, radius):
    return math.sqrt((point[0] - center[0]) ** 2 + (point[1] - center[1]) ** 2) <= radius

# Draw the central circle and surrounding circles
central_x, central_y = screen_width // 2, screen_height // 2
central_radius = 50
circle_radius = 20
circles = {}
angle_increment = 360 / 10  # Split the circle into 10 equal parts
for i in range(10):
    angle = math.radians(i * angle_increment)
    x = central_x + 400 * math.cos(angle)
    y = central_y + 400 * math.sin(angle)
    circles[i] = {"center": (int(x), int(y)), "color": RED}

# Variables to store mouse positions
mouse_positions = []

# Main loop
running = True
current_circle = None

with open("mouse_movements3.txt", "w") as file:
    while running:
        screen.fill(WHITE)
        # Draw the central circle
        draw_circle(screen, BLUE, (central_x, central_y), central_radius)
        # Draw surrounding circles
        for key, circle in circles.items():
            draw_circle(screen, circle["color"], circle["center"], circle_radius)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    running = False  # End the program when left mouse button is clicked

        # Get mouse position
        x, y = pygame.mouse.get_pos()
        mouse_positions.append((x, y))

        pygame.display.flip()
        clock.tick(60)

        # Save mouse positions to a text file
        for x, y in mouse_positions:
            file.write(f"{x}, {y}\n")

# Quit Pygame
pygame.quit()

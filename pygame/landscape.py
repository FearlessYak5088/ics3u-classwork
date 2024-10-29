# # # Landscape Assignment

import pygame
import sys

# Initialize pygame
pygame.init()

# Set display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Landscape by Fan")

# colours
blue = (0, 0, 139)
green = (1, 70, 42)
gray = (51, 51, 51)
orange = (200, 100, 0)
brown = (92, 64, 51)
white = (144, 144, 144)

circle_x = 120
circle_y = 200

# loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # sky
    screen.fill(blue)

    # ground
    pygame.draw.rect(screen, green, (0, 400, width, height - 400))

    # house body
    pygame.draw.rect(screen, brown, (300, 300, 300, 200))

    # roof
    pygame.draw.polygon(screen, orange, [(300, 300), (450, 175), (600, 300)])

    # door
    pygame.draw.rect(screen, gray, (380, 380, 70, 120))

    # moon
    pygame.draw.circle(screen, white, (circle_x, circle_y), 60)

    # move the moon across the sky
    if circle_x <= width // 2:
        circle_x += 0.035
        circle_y -= 0.015
    elif circle_x >= width // 2:
        circle_x += 0.035
        circle_y += 0.015

    # update the display
    pygame.display.flip()


# # # Landscape

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
blue2 = (135, 206, 250)
green = (1, 70, 42)
gray = (51, 51, 51)
gray2 = (75, 75, 75)
orange = (200, 100, 0)
brown = (92, 64, 51)
white = (144, 144, 144)
white2 = (200, 200, 200)
black = (0, 0, 0)
orange2 = (255,140,0)
yellow = (204, 204, 0)

window_colour = white2
moon_x = 0
moon_y = 155
sun_x = 0
sun_y = 125
day = True

# loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # sky
    if day:
        screen.fill(blue2)

        # draw the sun
        pygame.draw.circle(screen, orange2, (sun_x, sun_y), 60)
        
        # make a parabola that the sun follows
        parabola = ((sun_x - 400) ** 2) / 500

        # move the sun up
        sun_x += 0.075
        sun_y = parabola

        if sun_x > width + 65:
            day = False
    else:
        screen.fill(blue)

        # draw the moon
        pygame.draw.circle(screen, white, (moon_x, moon_y), 60)

        # moon texture
        pygame.draw.circle(screen, gray2, (moon_x - 20, moon_y + 20), 20)
        pygame.draw.circle(screen, gray2, (moon_x - 10, moon_y - 20), 12)

        # change window colour (light turns on in house)
        window_colour = yellow 

        # change the parabola to affect the moon
        parabola = ((moon_x - 400) ** 2) / 500

        # move the moon  
        moon_x += 0.075
        moon_y = parabola

    # ground
    pygame.draw.rect(screen, green, (0, 400, width, height - 400))

    # house body
    pygame.draw.rect(screen, brown, (300, 300, 300, 200))

    # roof
    pygame.draw.polygon(screen, orange, [(300, 300), (450, 175), (600, 300)])

    # door
    pygame.draw.rect(screen, gray, (380, 380, 70, 120))

    # door handle
    pygame.draw.circle(screen, white, (395, 450), 8)

    # window
    pygame.draw.ellipse(screen, window_colour, (485, 380, 80, 80))
    pygame.draw.line(screen, black, (525, 380), (525, 460), 2)
    pygame.draw.line(screen, black, (485, 420), (565, 420), 2)
            

    # update the display
    pygame.display.flip()


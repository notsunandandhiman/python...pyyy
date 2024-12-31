import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sprite Color Change Example")

# Define colors
WHITE = (255, 255, 255)

# Sprite class
class MySprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def change_color(self):
        # Change the sprite's color to a random color
        self.image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

# Create two sprites
sprite1 = MySprite((255, 0, 0), 50, 50)  # Red sprite
sprite2 = MySprite((0, 0, 255), 50, 50)  # Blue sprite

# Set initial positions
sprite1.rect.x = 100
sprite1.rect.y = 100
sprite2.rect.x = 300
sprite2.rect.y = 100

# Create a sprite group
all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1)
all_sprites.add(sprite2)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Change color on space key press
                sprite1.change_color()
                sprite2.change_color()

    # Fill the background
    screen.fill(WHITE)

    # Draw all sprites
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dice Simulator")

# Load dice images
dice_images = [
    pygame.image.load('C:/Users/ANKIT ROY/Downloads/faceone.png'),
    pygame.image.load('C:/Users/ANKIT ROY/Downloads/facetwo.png'),
    pygame.image.load('C:/Users/ANKIT ROY/Downloads/facethree.png'),
    pygame.image.load('C:/Users/ANKIT ROY/Downloads/facefour.png'),
    pygame.image.load('C:/Users/ANKIT ROY/Downloads/facefive.png'),
    pygame.image.load('C:/Users/ANKIT ROY/Downloads/facesix.png')
]

# Function to draw a dice
def draw_dice(face):
    win.fill((255, 255, 255))  # Fill the background with white
    dice_img = dice_images[face - 1]
    dice_rect = dice_img.get_rect(center=(width // 2, height // 2))
    win.blit(dice_img, dice_rect)
    pygame.display.update()

# Main loop
running = True
current_face = random.randint(1, 6)
draw_dice(current_face)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                current_face = random.randint(1, 6)
                draw_dice(current_face)

pygame.quit()

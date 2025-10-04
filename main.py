
# pingpong game using pygame
import pygame
pygame.init()

# dimensions
width = 800
height = 600

# screen initialization
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("pong game")

# player initialization
player = pygame.Rect(0, 0, 20, 70)
player.centery = height/2
player.x = 10

# player initialization
cpu = pygame.Rect(0, 0, 20, 70)
cpu.centery = height/2
cpu.x = width - 30

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # line divider for the pong table
    pygame.draw.aaline(
        screen, color="green", start_pos=(width/2, 0), end_pos=(width/2, height)
    )

    # players paddle
    pygame.draw.rect(
        surface=screen,
        color="red",
        rect=player
    )
    # cpu paddle
    pygame.draw.rect(
        surface=screen,
        color="red",
        rect=cpu
    )


    pygame.display.update()

pygame.quit()

# pingpong game using pygame
import pygame
import random

pygame.init()

# dimensions
width = 800
height = 600

# clock
clock = pygame.time.Clock()

#........
font = pygame.font.Font(None, 40)

# screen initialization
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("pong game")

# player initialization and movement
player = pygame.Rect(0, 0, 20, 70)
player.centery = height/2
player.x = 10
player_speed = 5
player_score = 0


# cpu initialization and movement
cpu = pygame.Rect(0, 0, 20, 70)
cpu.centery = height/2
cpu.x = width - 30
cpu_speed = 5
cpu_score = 0

# ball initialization and movement
ball = pygame.Rect(0, 0, 30, 30)
ball.center = (width/2, height/2)
ball_speed_x = 5
ball_speed_y = 5

# ball movement
def move_ball():
    global ball_speed_y, ball_speed_x, cpu_score, player_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1

    if ball.left <= 0:
        cpu_score += 1
        reset_ball()
    if ball.right >= width:
        player_score += 1
        reset_ball()

    if ball.colliderect(player):
        ball.left = player.right
        ball_speed_x *= -1
    if ball.colliderect(cpu):
        ball.right = cpu.left
        ball_speed_x *= -1

# player movement
def move_player():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player.top >= 0:
        player.y -= player_speed
    if keys[pygame.K_DOWN] and player.bottom <= height:
        player.y += player_speed

# player movement
def move_cpu():
    if ball.centery > cpu.centery and player.bottom <= height:
        cpu.y += cpu_speed
    if ball.centery < cpu.centery and player.top >= 0:
        cpu.y -= cpu_speed

# resetting the ball after missing
def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.center = (width/2, height/2)
    ball_speed_x *= random.choice([1, -1])
    ball_speed_y *= random.choice([1, -1])

# while loop for continuos running
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("black")

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
    # cpu move
    move_cpu()

    # pingpong ball
    pygame.draw.ellipse(
        surface=screen,
        color="orange",
        rect=ball
    )

    player_speed_surface = font.render(
        str(player_score),
        False,
        (255, 255, 255)
    )
    cpu_speed_surface = font.render(
        str(cpu_score),
        False,
        (255, 255, 255)
    )

    screen.blit(
        player_speed_surface, (width * 0.25, 10)
    )
    screen.blit(
        cpu_speed_surface, (width * 0.75, 10)
    )


    
    # move ball
    move_ball()
    # move player
    move_player()
    # cpu move
    move_cpu()
    
    clock.tick(60)
    pygame.display.update()

pygame.quit()
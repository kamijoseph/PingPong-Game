
# pingpong game using pygame
import pygame
pygame.init()

# dimensions
width = 800
height = 600

# clock
clock = pygame.time.Clock()

# screen initialization
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("pong game")

# player initialization and movement
player = pygame.Rect(0, 0, 20, 70)
player.centery = height/2
player.x = 10
player_speed = 5


# cpu initialization and movement
cpu = pygame.Rect(0, 0, 20, 70)
cpu.centery = height/2
cpu.x = width - 30

# ball initialization and movement
ball = pygame.Rect(0, 0, 30, 30)
ball.center = (width/2, height/2)
ball_speed_x = 5
ball_speed_y = 5

# ball movement
def move_ball():
    global ball_speed_y, ball_speed_x
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= width:
        ball_speed_x *= -1



# while loop for continuos running
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player.top >= 0:
        player.y -= player_speed
    if keys[pygame.K_DOWN] and player.bottom <= height:
        player.y += player_speed
    
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

    # pingpong ball
    pygame.draw.ellipse(
        surface=screen,
        color="orange",
        rect=ball
    )
    move_ball()
    
    clock.tick(60)
    pygame.display.update()

pygame.quit()
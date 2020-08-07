import random
from paddle import Paddle
from ball import Ball
import time
import pygame

pygame.init()

# Initialize the screen, the caption, the background color
win = width, height = 800, 600
screen = pygame.display.set_mode(win)
caption = pygame.display.set_caption("Pong")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Score
score_value1, score_value2 = 0, 0
font = pygame.font.Font('freesansbold.ttf', 16)
textX = 10
textY = 10
def show_score(x, y, score_value, player):
    score = font.render(f"Player {player} score: {str(score_value)}", True, (255, 255, 255))
    screen.blit(score, (x, y))

# Paddle 1
paddle1 = Paddle(WHITE, 10, 100)
paddle1.rect.x = 20
paddle1.rect.y = 210

# Paddle 1
paddle2 = Paddle(WHITE, 10, 100)
paddle2.rect.x = 770
paddle2.rect.y = 210

# Ball
ball = Ball(WHITE, 10, 10)
ball.rect.x = 400
ball.rect.y = 300

# List of sprites
all_sprites_list = pygame.sprite.Group()

# Add paddles to the list of sprites
all_sprites_list.add(paddle1)
all_sprites_list.add(paddle2)
all_sprites_list.add(ball)

# Winner
screen_center = 150, 300
finish_font = pygame.font.Font('freesansbold.ttf', 64)
def win():
    global score_value1
    global score_value2
    if score_value1 > 6:
        end_statement = finish_font.render(f"Player 1 Wins", True, (255, 255, 255))
        screen.blit(end_statement, screen_center)
        time.sleep(3)
        running = False
    if score_value2 > 6:
        end_statement = finish_font.render(f"Player 1 Wins", True, (255, 255, 255))
        screen.blit(end_statement, screen_center)
        time.sleep(3)
        running = False

# Clock to measure fps
clock = pygame.time.Clock()

# Game Loop
running = True
while running:
    # Drawing the game area
    screen.fill(BLACK)
    # Drawing the net
    pygame.draw.line(screen, WHITE, (400, 0), (400, 600))
    # Drawing all the sprites
    all_sprites_list.draw(screen)
    # Showing score
    show_score(textX, textY, score_value1, 1)
    show_score(650, textY, score_value2, 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keypress = pygame.key.get_pressed()
    if keypress[pygame.K_w]:
        paddle1.moveUp(5)
    if keypress[pygame.K_s]:
        paddle1.moveDown(5)
    if keypress[pygame.K_UP]:
        paddle2.moveUp(5)
    if keypress[pygame.K_DOWN]:
        paddle2.moveDown(5)

    # Game logic
    all_sprites_list.update()

    # Ball bouncing off walls
    if ball.rect.x > 800:
        score_value1 += 1
        ball.rect.x = 400
        ball.rect.y = 300
        time.sleep(3)
        ball.new()
    if ball.rect.x < 0:
        score_value2 += 1
        ball.rect.x = 400
        ball.rect.y = 300
        time.sleep(3)
        ball.new()
    if ball.rect.y > 600:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    # Collision detection
    if pygame.sprite.collide_mask(paddle1, ball) or pygame.sprite.collide_mask(paddle2, ball):
        ball.bounce()
        effect = pygame.mixer.Sound('/Users/rishit/desktop/gamedev/pong/pong.wav')
        effect.play()

    win() # Check who has won
    pygame.display.update() # Can also use flip() however, through update you can add arguements. If no arguments its basically flip()

    # Number of frames per second (fps)
    clock.tick(60)

pygame.quit()

import pygame
from random import randint

WHITE = (255, 255, 255)
BLACK = (0,0,0)

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Drawing the ball
        pygame.draw.rect(self.image, WHITE, [0, 0, width, height])

        # Velocity of the ball
        self.velocity = [randint(3, 7), randint(-7, 7)]

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)

    def new(self):
        self.velocity = [randint(3, 7), randint(-3, 3)]

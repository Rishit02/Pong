import pygame
WHITE = (255, 255, 255)
BLACK = (0,0,0)

class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        # Call the parent class
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the paddle
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    # To move the paddle up the screen
    def moveUp(self, pixels):
        self.rect.y -= pixels
        # Make sure the paddles do not go above the screen
        if self.rect.y <0:
            self.rect.y = 0

    # To move the paddle down the screen
    def moveDown(self, pixels):
        self.rect.y += pixels
        # Make sure the paddles do not go below the screen
        if self.rect.y > 500:
            self.rect.y = 500

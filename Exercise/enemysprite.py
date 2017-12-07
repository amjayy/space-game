import pygame
from pygame.sprite import Sprite

class Enemysprite(Sprite):
    """ A class to represent enemy sprite."""

def __init__(self, ai_settings, screen):
    """ Initialize the enemy sprite and set its starting position."""
    super(enemysprite, self).__init__()
    self.screen = screen
    self.ai_settings = ai_settings

    self.image = pygame.image.load("images/enemy.jpg")
    self.rect = self.image.get_rect()

    self.rect.x = self.rect.width
    self.rect.y = self.rect.height

    self.x = float(self.rect.x)

    def blitme(self):
        """ Draw enemy at its current location."""
        self.screen.blit(self.image, self.rect)

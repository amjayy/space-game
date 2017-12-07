import pygame

class Alienlady():
    def __init__(self, screen):
        """ Initialize the alienlady and set its starting point. """
        self.screen = screen

        self.image = pygame.image.load("images/alienlady.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """ Draw the alienlady at its location."""
        self.screen.blit(self.image, self.rect)

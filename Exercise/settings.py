import pygame
class Settings():
 """ A class to store all the settings for this game."""

 def __init__(self):
        """ Initialize the game's settings. """
        # Screen settings
        self.screen_width =900
        self.screen_height= 600
        self.background_image = pygame.image.load("images/spacebridge.jpg")
        

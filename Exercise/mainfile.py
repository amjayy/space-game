import pygame
from settings import Settings
from alienlady import Alienlady


pygame.init()
pygame.mixer.init()
ai_settings=Settings()
screen =  pygame.display.set_mode(
    (ai_settings.screen_width, ai_settings.screen_height))
pygame.display.set_caption( "Space Queen Showdown")
pygame.mixer.music.load("music/Aaliyah.mp3")
pygame.mixer.music.play(0)

alienlady= Alienlady(screen)

running = False
clock = pygame.time.Clock()
surface_position = [0, 0]

surface= (ai_settings.surface)



while not running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True
            
    screen.blit(surface, surface_position)
    alienlady.blitme()

    pygame.display.flip()

    clock.tick(60)

    

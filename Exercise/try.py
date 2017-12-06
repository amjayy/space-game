import pygame
from settings import Settings

pygame.init()
pygame.mixer.init()
ai_settings=Settings()
screen =  pygame.display.set_mode(
    (ai_settings.screen_width, ai_settings.screen_height))
pygame.display.set_caption( "Xena Vs. Shanti: Space Lady Showdown")
pygame.mixer.music.load("music/Aaliyah.mp3")
pygame.mixer.music.play(0)
done = False
clock = pygame.time.Clock()
background_position = [0, 0]
background_image = pygame.image.load("images/spacebridge.jpg")
player = pygame.image.load("images/alienlady.jpg")

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(background_image, background_position)

    pygame.display.flip()

    clock.tick(60)

    

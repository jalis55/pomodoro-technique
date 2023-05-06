import pygame
import time

#pygame.init()

def imshow(filename):
    #pygame.init()
    img = pygame.image.load(filename)
    size = img.get_rect().size
    pygame.display.set_caption('GeeksforGeeks')
    screen = pygame.display.set_mode(size)
    screen.blit(img, (0, 0))
    pygame.display.flip()
    #pygame.event.clear()

def imclose():
    #pygame.quit()
    pygame.display.quit()

imshow('start.jpg')
time.sleep(3)
imclose()

imshow('rest.jpg')
time.sleep(3)
imclose()
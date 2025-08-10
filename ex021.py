import pygame

pygame.init()
pygame.mixer.music.load('gorilaroxo.mp3')
pygame.mixer.music.play()
import time
while pygame.mixer.music.get_busy():
    time.sleep(1)
pygame.quit()
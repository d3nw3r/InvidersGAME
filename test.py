import pygame
import sys
bg_color = (0,0,255)

def run_gm():
    pygame.init()
    pygame.display.set_mode((800,600))
    pygame.display.set_caption('TEST')
    pygame.fill(bg_color)
    pygame.display.flip()

run_gm()
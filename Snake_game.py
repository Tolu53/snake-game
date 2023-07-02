import pygame
import random


pygame.init()
class snakeGame:
    def __init__(self , w = 640, h =480):
        self.w = w
        self.h = h

        # init display

    def play_step(self):
       pass
        
if __name__== '__main__':
    game = snakeGame()

    while True:
        game.play_step()

    
    pygame.quit()
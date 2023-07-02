import pygame
import random
from enum import Enum
from collections import namedtuple


pygame.init()

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('point', 'x, y')
class snakeGame:
    def __init__(self , w = 640, h =480):
        self.w = w
        self.h = h

        # init display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Snake is Love , Snake is Life')
        self.clock = pygame.time.Clock()

        # init game state
        self.direction = Direction.RIGHT
        self.head =  Point (self.w/2, self.h/2)
        self.snake = [self.head, Point(self.head.x - 20, self.head.y), Point(self.head.x - 40, self.head.y)]

    def play_step(self):
       pass
        
if __name__== '__main__':
    game = snakeGame()

    while True:
        game.play_step()

    
    pygame.quit()
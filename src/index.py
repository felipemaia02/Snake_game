import pygame
from Game_snake import Game_snake
from Config import *

def main():
    display = pygame.display.set_mode((
        Config['game']['width'], 
        Config['game']['height']
    ))
    pygame.display.set_caption(Config['game']['caption'])

    game = Game_snake(display)
    game.loop()

if __name__ == '__main__':
    main()
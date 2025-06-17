import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Game_Over import GameOver
from code.Level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            # CREATE LEVEL
            level = Level(self.window)
            level_return = level.run()
            # TODO:
            game_over = GameOver(self.window, level_return)
            stop = game_over.show() # usa esc para fechar

        quit()

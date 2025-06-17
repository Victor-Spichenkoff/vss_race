import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Game_Over import GameOver
from code.Helper import reset_global, clear_keys
from code.Level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.num = 0
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            # CREATE LEVEL
            level = Level(self.window)
            points = level.run()

            clear_keys() # without this, it might skip game_over_screen,
            game_over = GameOver(self.window, points)
            game_over.show() # usa esc para fechar
            reset_global()
        quit()

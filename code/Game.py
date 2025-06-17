import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
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
            # if level_return:
            #     stop = get_final_screen() # usa esc para fechar
            #     if stop:
            #         break

        quit()

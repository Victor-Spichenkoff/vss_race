import pygame

import code.Const as Const
import code.Global as Global

def update_difficult():
    if Const.DIFFICULT > 4:
        return True

    Const.DIFFICULT += 1
    Const.SPAW_TIME = int(2000 / Const.DIFFICULT + 250)
    Const.ENTITY_SPEED['bg'] = 6 * Const.DIFFICULT / 1.75
    if Const.DIFFICULT == 3:
        Const.ENTITY_SPEED["player"] *= 1.4
        return True
    return False


def reset_global():
    Const.DIFFICULT = 1
    Const.SPAW_TIME = 2200
    Global.POINTS = 0


def clear_keys():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # fechou, executo mesmo
            pygame.quit()
            quit()

    return False
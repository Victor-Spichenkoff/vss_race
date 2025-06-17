import code.Const as Const

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
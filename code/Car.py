import code.Const as Const

from code.Const import WIN_HEIGHT, ENTITY_SPEED, WIN_WIDTH, ROAD_LIMIT_Y, ROAD_LIMIT_RIGHT, ROAD_LIMIT_LEFT
from code.Entity import Entity


class Car(Entity):
    def __init__(self, name, position: tuple):
        super().__init__(name, position)

    def move(self):
        speed_changer = Const.DIFFICULT / 1.2 if Const.DIFFICULT / 1.2 >= 1 else 1
        self.rect.centery += ENTITY_SPEED[self.name] * speed_changer


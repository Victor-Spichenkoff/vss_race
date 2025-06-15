from code.Const import WIN_HEIGHT, ENTITY_SPEED
from code.Entity import Entity

class Background(Entity):
    """
    - name deve ser com base nos assets
    """
    def __init__(self, name, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centery += ENTITY_SPEED[self.name]
        if self.rect.top >= WIN_HEIGHT:
            self.rect.bottom = 0
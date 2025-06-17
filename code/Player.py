import pygame

from code.Const import WIN_HEIGHT, ENTITY_SPEED, WIN_WIDTH, ROAD_LIMIT_Y, ROAD_LIMIT_RIGHT, ROAD_LIMIT_LEFT, \
    FINAL_POSITION_RIGHT, FINAL_POSITION_LEFT
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name, position: tuple):
        super().__init__(name, position)
        self.going_to = "none"

    def move(self):
        pressed_key = pygame.key.get_pressed()  # quando segura, não é so apertar

        if pressed_key[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name] * 1.2
        if pressed_key[pygame.K_LEFT] and self.rect.left > ROAD_LIMIT_LEFT:
            if self.rect.centerx > FINAL_POSITION_LEFT:
                self.going_to = "left"
        if pressed_key[pygame.K_RIGHT] and self.rect.right < ROAD_LIMIT_RIGHT:
            if self.rect.centerx < FINAL_POSITION_RIGHT:
                self.going_to = "right"

        # handle special move
        if self.going_to == "right":
            self.rect.centerx += ENTITY_SPEED[self.name]
            if self.rect.centerx >= FINAL_POSITION_RIGHT:
                self.going_to = "none"

        if self.going_to == "left":
            self.rect.centerx -= ENTITY_SPEED[self.name]
            if self.rect.centerx <= FINAL_POSITION_LEFT:
                self.going_to = "none"

        # FOR DEBUG AND POSITION COLLETION:
        # if pressed_key[pygame.K_LEFT] and self.rect.left > ROAD_LIMIT_LEFT:
        #     self.rect.centerx -= ENTITY_SPEED[self.name]
        #     print(self.rect.centerx)
        # if pressed_key[pygame.K_RIGHT] and self.rect.right < ROAD_LIMIT_RIGHT:
        #     self.rect.centerx += ENTITY_SPEED[self.name]
        #     print(self.rect.centerx)


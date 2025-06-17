import pygame

from code.Car import Car
from code.Entity import Entity
from code.Const import WIN_HEIGHT
from code.Player import Player


class EntityMediator:
    # __ -> privado
    @staticmethod
    def __verify_collision_window_and_remove(ent: Entity, entity_list: list[Entity]):
        if isinstance(ent, Car):
            if ent.rect.top > WIN_HEIGHT:
                entity_list.remove(ent)

    @staticmethod
    def __verify_collision_entity(player: Entity, car: Entity):
        # if not isinstance(player, (Car, Player)) or not isinstance(car, (Car, Player)) :
        #     return False

        collision_margin_x = 30
        collision_margin_y = 5
        p = player.rect.inflate(-collision_margin_x, -collision_margin_y)
        c = car.rect.inflate(-collision_margin_x, -collision_margin_y)
        return (
                p.right >= c.left and
                p.left <= c.right and
                p.bottom >= c.top and
                p.top <= c.bottom
        )

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for ent in entity_list:
            if isinstance(ent, Player):
                player = ent
                break

        for ent in entity_list:
            if isinstance(ent, Car):
                EntityMediator.__verify_collision_window_and_remove(ent, entity_list)
                has_collision = EntityMediator.__verify_collision_entity(player, ent)
                if has_collision:
                    return True

        return False
    # FIM MEU =======================

    # def verify_collision(entity_list: list[Entity]):
    #     for i in range(len(entity_list) - 1):
    #         entity1 = entity_list[i]
    #         EntityMediator.__verify_collision_window_and_remove(entity1, entity_list)
    #
    #         # colisão entre
    #         for j in range(i + 1, len(entity_list)):
    #             entity2 = entity_list[j]
    #             has_collision = EntityMediator.__verify_collision_entity(entity1, entity2)
    #             if has_collision:
    #                 return True
    #     return False




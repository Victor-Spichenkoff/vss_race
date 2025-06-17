from code.Car import Car
from code.Entity import Entity
from code.Const import WIN_HEIGHT
from code.Player import Player


class EntityMediator:
    # __ -> privado
    @staticmethod
    def __verify_collision_window(ent: Entity, entity_list: list[Entity]):
        if isinstance(ent, Car):
            if ent.rect.top > WIN_HEIGHT:
                entity_list.remove(ent)

    @staticmethod
    def __verify_collision_entity(player: Entity, car: Entity):
        return (player.rect.right >= car.rect.left and
            player.rect.left <= car.rect.right and
            player.rect.bottom >= car.rect.top and
            player.rect.top <= car.rect.bottom)



    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for ent in entity_list:
            if isinstance(ent, Player):
                player = ent
                break

        for ent in entity_list:
            if isinstance(ent, Car):
                EntityMediator.__verify_collision_window(ent, entity_list)
                has_collision = EntityMediator.__verify_collision_entity(player, ent)
                if has_collision:
                    return True

        return False

    # def verify_collision(entity_list: list[Entity]):
    #     for i in range(len(entity_list)):
    #
    #         entity1 = entity_list[i]
    #         EntityMediator.__verify_collision_window(entity1)
    #
    #         # colisão entre
    #         for j in range(i + 1, len(entity_list)):
    #
    #             entity2 = entity_list[j]
    #             user_collided = EntityMediator.__verify_collision_entity(player, entity2)



    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)

import random

from code.Background import Background
from code.Const import WIN_HEIGHT, WIN_WIDTH, PLAYER_WIDTH, PLAYER_HEIGHT, ROAD_LIMIT_RIGHT, ROAD_LIMIT_LANE_2, \
    ROAD_LIMIT_LANE_1, ROAD_LIMIT_LEFT, BOT_WIDTH, FINAL_POSITION_RIGHT, FINAL_POSITION_LEFT
from code.Player import Player
from code.Car import Car

"""
- bg
- player
- car1
- car2
"""
class EntityFactory:
    @staticmethod
    def get_entity(entity_name, position: tuple = (0, 0)):
        match entity_name:
            case "bg":
                list_bg = []
                for i in range(2):
                    list_bg.append(Background('bg', (0, -WIN_HEIGHT)))
                    list_bg.append(Background('bg', (0, 0)))
                return list_bg
            case "player":
                return Player("player", (WIN_WIDTH / 2 - PLAYER_WIDTH / 2, WIN_HEIGHT - PLAYER_HEIGHT - 30))
            case "car1":
                return Car("car1", (get_car_position(), 0))
            # case "car1":
            #     return Enemy("Enemy1", (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT -40)))

        return None


"""
Position at X axis for the car (between road limits and lanes)
"""
def get_random_car_position():
    padding = 4

    if True:
    # if is_left:
        return random.randint(int(ROAD_LIMIT_RIGHT) - BOT_WIDTH - padding, ROAD_LIMIT_LANE_2 + padding)

    return random.randint(int(ROAD_LIMIT_LEFT) + padding, ROAD_LIMIT_LANE_1 - BOT_WIDTH - padding)


def get_car_position():
    is_left = random.randint(0, 1)
    if is_left:
        return FINAL_POSITION_LEFT - BOT_WIDTH / 2

    return FINAL_POSITION_RIGHT - BOT_WIDTH / 2
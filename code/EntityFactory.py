
"""
- bg
- player
- car1
- car2
"""
from code.Background import Background
from code.Const import WIN_HEIGHT


class EntityFactory:
    @staticmethod
    def get_entity(entity_name, position: tuple = (0, 0)):
        match entity_name:
            case "bg":
                list_bg = []
                for i in range(2):
                    list_bg.append(Background('bg', (0, -WIN_HEIGHT + 60)))
                    # list_bg.append(Background('bg', (0, -WIN_HEIGHT)))
                    list_bg.append(Background('bg', (0, 70)))
                return list_bg
            # case "Player":
            #     return Player("Player1", (10, WIN_HEIGHT / 2))
            # case "car1":
            #     return Player("Player2", (10, WIN_HEIGHT / 2 - 60))
            # case "car1":
            #     return Enemy("Enemy1", (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT -40)))

        return None
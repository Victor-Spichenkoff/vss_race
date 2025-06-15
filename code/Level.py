import random

import pygame

from code.Const import WIN_HEIGHT, WIN_HEIGHT
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window):
        self.window = window
        self.entity_list: list[Entity] = []
        # self.player_score = player_score
        self.entity_list.extend(EntityFactory.get_entity('bg'))

        # self.entity_list.append(EntityFactory.get_entity("Player1"))
        # player = EntityFactory.get_entity("Player1")
        # player.score = player_score[0]
        # self.entity_list.append(player)

        # pygame.time.set_timer(EVENT_ENEMY, SPAW_TIME)
        # pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)


    def run(self):
        # TODO:SOUND
        # pygame.mixer_music.load(f'./assets/{self.name}.mp3')
        # pygame.mixer_music.set_volume(0.3)
        # TODO: DECOMMENT
        # pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()  # manter taxa de atualização constante
        while True:
            clock.tick(60)  # FPS

            # EVENT
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                # ent.move()
                # HUD
                # if ent.name =="player":
                    # self.level_text(14, f'Player1 - Health: {ent.health} | score : {ent.score}', COLOR_GREEN, (10, 25))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # fechou, executo mesmo
                    pygame.quit()
                    quit()  # acabar com o pygame (init)
                # if event.type == EVENT_ENEMY:
                #     choice = random.choice(("Enemy1", "Enemy1", "Enemy2"))
                #     self.entity_list.append(EntityFactory.get_entity(choice))
                # if event.type == EVENT_TIMEOUT:
                #     self.timeout -= 100
                #     if self.timeout <= 0:
                #         for ent in self.entity_list:
                #             if isinstance(ent, Player) and ent.name == "Player1":
                #                 player_score[0] = ent.score
                #             if isinstance(ent, Player) and ent.name == "Player2":
                #                 player_score[1] = ent.score
                #         return True


            # TODO: TEXTS DEBUG, HELP
            # self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            # self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            # self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))

            pygame.display.flip()

            # COLLISIONS
            # EntityMediator.verify_collision(self.entity_list)
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

import random

import pygame
import code.Global as Global
from code.Const import WIN_HEIGHT, WIN_HEIGHT, COLOR_WHITE, COLOR_BLACK, EVENT_ENEMY, SPAW_TIME, EVENT_DIFFICULT_UP
import code.Const as Const
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Helper import update_difficult


class Level:
    def __init__(self, window):
        self.window = window
        self.entity_list: list[Entity] = []
        # self.player_score = player_score
        self.entity_list.extend(EntityFactory.get_entity('bg'))
        # self.difficulty = 1
        self.entity_list.append(EntityFactory.get_entity("player"))
        self.entity_list.append(EntityFactory.get_entity(random.choice(("car1", "car3"))))
        # player = EntityFactory.get_entity("Player1")
        # player.score = player_score[0]
        # self.entity_list.append(player)
        self.points = 0

        pygame.time.set_timer(EVENT_ENEMY, Const.SPAW_TIME)
        pygame.time.set_timer(EVENT_DIFFICULT_UP, 1000, loops=4)


    def run(self):
        # TODO: DECOMMENT SOUND
        music_choice = random.randint(1, 2)
        pygame.mixer_music.load(f'./assets/music_{music_choice}.mp3')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1) # -1 === infinito
        clock = pygame.time.Clock()  # manter taxa de atualização constante
        while True:
            clock.tick(60)  # FPS

            # EVENT
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                # HUD
                # if ent.name =="player":
                    # self.level_text(14, f'Player1 - Health: {ent.health} | score : {ent.score}', COLOR_GREEN, (10, 25))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # fechou, executo mesmo
                    pygame.quit()
                    quit()  # acabar com o pygame (init)
                #     TODO:
                if event.type == EVENT_ENEMY:
                    choice = random.choice(("car1", "car3"))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_DIFFICULT_UP:
                    is_max = update_difficult()
                    if is_max:
                        print(Const.SPAW_TIME)
                        pygame.time.set_timer(EVENT_ENEMY, Const.SPAW_TIME)



            self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_BLACK, (10, WIN_HEIGHT - 50))
            self.level_text(45, f'{Global.POINTS}', COLOR_BLACK, (20, 20))
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_BLACK, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'DIFICULDADE: {Const.DIFFICULT}', COLOR_BLACK, (10, WIN_HEIGHT - 20))
            self.level_text(14, f'DIFICULDADE: {Const.SPAW_TIME}', COLOR_BLACK, (10, WIN_HEIGHT - 70))
            pygame.display.flip()

            # COLLISIONS
            has_collision = EntityMediator.verify_collision(self.entity_list)
            if has_collision:
                return self.points


    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

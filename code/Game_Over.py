import pygame
from pygame import K_BACKSPACE, K_RETURN, K_ESCAPE

from code.Const import WIN_WIDTH, WIN_HEIGHT, COLOR_WHITE, COLOR_BLUE, COLOR_GREEN, COLOR_RED, SONG_DELAY


class GameOver:
    def __init__(self, window, points):
        self.window = window
        self.points = points

        self.surf = pygame.image.load("./assets/game_over.png").convert_alpha()
        self.rect = self.surf.get_rect(topleft=(0, 0))
        self.window.blit(source=self.surf, dest=self.rect)


    def get_action(self):
        self.score_text(30, "Press any key to restart (ESC)", COLOR_RED, (WIN_WIDTH / 2, 300))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # fechou, executo mesmo
                pygame.quit()
                quit()
             # SALVAR O NOME (TYPING)
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                else:
                    return True
        return False


    def show(self):
        # TODO: DECOMMENT SOUND
        pygame.mixer_music.load(f'./assets/game_over.mp3')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(start=SONG_DELAY) # -1 === infinito
        while True:
            self.score_text(50, "GAME OVER", COLOR_RED, (WIN_WIDTH / 2, 200))
            self.score_text(35, f"POINTS: {self.points}", COLOR_WHITE, (WIN_WIDTH / 2, 250))
            stop = self.get_action()
            pygame.display.flip()
            if stop:
                return stop


    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

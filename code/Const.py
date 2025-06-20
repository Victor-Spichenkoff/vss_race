import pygame
import code.Global as Global

# C
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (64, 128, 255)
COLOR_RED = (255, 32, 32)
COLOR_GREEN = (32, 255, 64)

# SPACE
WIN_WIDTH = 400
WIN_HEIGHT = 600

ROAD_LIMIT_RIGHT = (WIN_WIDTH / 4) * 3 + 4
ROAD_LIMIT_LEFT = WIN_WIDTH / 4 + 2
ROAD_LIMIT_Y = 600
ROAD_LIMIT_LANE_1 = 172
ROAD_LIMIT_LANE_2 = 232

PLAYER_WIDTH = 45
PLAYER_HEIGHT = 104
BOT_WIDTH = 100


FINAL_POSITION_LEFT = 152
FINAL_POSITION_RIGHT = 256


# E
ENTITY_SPEED = {
    'bg': 6,
    'player': 4,
    'car1': 2,
    'car3': 2.75
}

EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_DIFFICULT_UP = pygame.USEREVENT + 2

# P
PLAYER_KEY_UP = pygame.K_UP
PLAYER_KEY_DOWN = pygame.K_DOWN

PLAYER_KEY_LEFT = pygame.K_LEFT

PLAYER_KEY_RIGHT = pygame.K_RIGHT

PLAYER_KEY_SHOOT = pygame.K_RCTRL


# GAME LOGIC
DIFFICULT = 1
SPAW_TIME = 3000
SONG_DELAY = 2.2

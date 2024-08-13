WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 1000

PLAY_WINDOW_WIDTH = WINDOW_WIDTH/2
PLAY_WINDOW_HEIGHT = PLAY_WINDOW_WIDTH

INFO_BAR_y = 100

BOTTOM_BAR_y = INFO_BAR_y + PLAY_WINDOW_HEIGHT

PIECE_WINDOW_x = WINDOW_WIDTH - PLAY_WINDOW_WIDTH
PIECE_WINDOW_y = INFO_BAR_y

SQUARE_WIDTH = PLAY_WINDOW_WIDTH/7
SQUARE_HEIGHT = PLAY_WINDOW_HEIGHT/7

COLOR_WHITE = (255,255,255) 

COLOR_BLACK = (0,0,0) 
  
COLOR_LIGHT_GREY = (170,170,170) 
  
COLOR_DARK_GREY = (100,100,100)

COLOR_RED = (210, 43, 43)
COLOR_DARK_RED = (136, 8, 8)

COLOR_YELLOW = (255, 255, 0)

COLOR_BACKGROUND = (60,25,60)


POSSIBLE_DICE_VALUES = [
    [(0, 0), (2, 0), (3, 0), (3, 1), (4, 1), (5, 2)],
    [(0, 1), (1, 1), (2, 1), (0, 2), (1, 0), (1, 2)],
    [(2, 2), (3, 2), (4, 2), (1, 3), (2, 3), (3, 3)],
    [(4, 0), (5, 1), (5, 1), (1, 5), (0, 4), (0, 4)],
    [(0, 3), (1, 4), (2, 5), (2, 4), (3, 5), (5, 5)],
    [(4, 3), (5, 3), (4, 4), (5, 4), (3, 4), (4, 5)],
    [(5, 0), (5, 0), (5, 0), (0, 5), (0, 5), (0, 5)],
]

DICE_LABEL = {
    (0, 0): 'A1', (0, 1): 'B1', (0, 2): 'C1', (0, 3): 'D1', (0, 4): 'E1', (0, 5): 'F1',
    (1, 0): 'A2', (1, 1): 'B2', (1, 2): 'C2', (1, 3): 'D2', (1, 4): 'E2', (1, 5): 'F2',
    (2, 0): 'A3', (2, 1): 'B3', (2, 2): 'C3', (2, 3): 'D3', (2, 4): 'E3', (2, 5): 'F3',
    (3, 0): 'A4', (3, 1): 'B4', (3, 2): 'C4', (3, 3): 'D4', (3, 4): 'E4', (3, 5): 'F4',
    (4, 0): 'A5', (4, 1): 'B5', (4, 2): 'C5', (4, 3): 'D5', (4, 4): 'E5', (4, 5): 'F5',
    (5, 0): 'A6', (5, 1): 'B6', (5, 2): 'C6', (5, 3): 'D6', (5, 4): 'E6', (5, 5): 'F6'
}

TABLE_INIT_STATE = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]

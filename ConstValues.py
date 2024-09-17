WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 900

PLAY_WINDOW_WIDTH = WINDOW_WIDTH/2
PLAY_WINDOW_HEIGHT = PLAY_WINDOW_WIDTH

INFO_BAR_y = 100

BOTTOM_BAR_y = INFO_BAR_y + PLAY_WINDOW_HEIGHT

PIECE_WINDOW_x = WINDOW_WIDTH - PLAY_WINDOW_WIDTH
PIECE_WINDOW_y = INFO_BAR_y

SQUARE_WIDTH = PLAY_WINDOW_WIDTH//7
SQUARE_HEIGHT = PLAY_WINDOW_HEIGHT//7

MENU_BUTTON_WIDTH = WINDOW_WIDTH*5/6
MENU_BUTTON_HEIGHT = 40

FIRST_MENU_BUTTON_X = WINDOW_WIDTH*1/12
FIRST_MENU_BUTTON_Y = WINDOW_HEIGHT*3/8

SECOND_MENU_BUTTON_X = WINDOW_WIDTH*1/12
SECOND_MENU_BUTTON_Y = WINDOW_HEIGHT*5/8

THIRD_MENU_BUTTON_X = WINDOW_WIDTH*1/12
THIRD_MENU_BUTTON_Y = WINDOW_HEIGHT*7/8


FIRST_DIFF_BUTTON_X = WINDOW_WIDTH*1/12 
FIRST_DIFF_BUTTON_Y = WINDOW_HEIGHT*1/2 

SECOND_DIFF_BUTTON_X = WINDOW_WIDTH*1/12 
SECOND_DIFF_BUTTON_Y = WINDOW_HEIGHT*3/4 



COLOR_WHITE = (255,255,255) 

COLOR_BLACK = (0,0,0) 

COLOR_BEIGE = ( 227, 188, 154)
  
COLOR_LIGHT_GREY = (170,170,170) 
  
COLOR_DARK_GREY = (50,50,50)

COLOR_RED = (210, 43, 43)
COLOR_DARK_RED = (136, 8, 8)

COLOR_YELLOW = (255, 255, 0)

COLOR_BLUE = (0, 0, 255)        
COLOR_BROWN = (150, 75, 0)         
COLOR_ORANGE = (255, 165, 0)        
COLOR_PURPLE = (160, 32, 240)       
COLOR_CYAN = (0, 255, 255)          
COLOR_GREEN = (0, 255, 0)   

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
    (0, 0): 'A1', (0, 1): 'A2', (0, 2): 'A3', (0, 3): 'A4', (0, 4): 'A5', (0, 5): 'A6',
    (1, 0): 'B1', (1, 1): 'B2', (1, 2): 'B3', (1, 3): 'B4', (1, 4): 'B5', (1, 5): 'B6',
    (2, 0): 'C1', (2, 1): 'C2', (2, 2): 'C3', (2, 3): 'C4', (2, 4): 'C5', (2, 5): 'C6',
    (3, 0): 'D1', (3, 1): 'D2', (3, 2): 'D3', (3, 3): 'D4', (3, 4): 'D5', (3, 5): 'D6',
    (4, 0): 'E1', (4, 1): 'E2', (4, 2): 'E3', (4, 3): 'E4', (4, 4): 'E5', (4, 5): 'E6',
    (5, 0): 'F1', (5, 1): 'F2', (5, 2): 'F3', (5, 3): 'F4', (5, 4): 'F5', (5, 5): 'F6'
}


TABLE_INIT_STATE = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]

 
PIECE_1 = [
    [(0, 0)]
]
PIECE_2 = [
    [
        (0, 0), 
        (1, 0)
    ],
    [
        (0, 0), (0, 1)
    ]
]
PIECE_3 = [
    [
    (0, 0), 
    (1, 0), 
    (2, 0)
    ],
    [
    (0, 0), (0, 1), (0, 2)
    ]
]
PIECE_4 = [
    [
            (0, 1), 
    (1, 0), (1, 1)
    ],
    [
    (0, 0), 
    (1, 0), (1, 1)
    ],
    [
    (0, 0), (0, 1), 
    (1, 0)
    ],
    [
    (0, 0), (0, 1), 
            (1, 1)
    ]
]
PIECE_5 = [
    [
    (0, 0), (0, 1), (0, 2), (0, 3)
    ],
    [
    (0, 0), 
    (1, 0), 
    (2, 0), 
    (3, 0)
    ]
]
PIECE_6 = [
    [
    (0, 0), (0, 1), 
            (1, 1), (1, 2)
    ],
    [
            (0, 1), 
    (1, 0), (1, 1), 
    (2, 0)
    ],
    [
            (0, 1), (0, 2), 
    (1, 0), (1, 1)
    ],
    [
    (0, 0), 
    (1, 0), (1, 1), 
            (2, 1)
    ]
]
PIECE_7 = [
    [
    (0, 0), 
    (1, 0), (1, 1),
    (2, 0)
    ],
    [
    (0, 0), (0, 1), (0, 2), 
             (1, 1)
    ],
    [
            (0, 1), 
    (1, 0), (1, 1) ,
            (2, 1)
    ],
    [
            (0, 1), 
    (1, 0), (1, 1), (1, 2)
    ]
]
   
PIECE_8 = [
    [
        (0, 0), (0, 1), (0, 2), 
                        (1, 2)
    ],
    [
                (0, 1), 
                (1, 1), 
        (2, 0), (2, 1),
    ],  
    [
        (0, 0),
        (1, 0), (1, 1), (1, 2),
    ],
    [
        (0, 0), (0, 1),
        (1, 0), 
        (2, 0)
    ],
    [
                        (-1, 2),
        (0, 0), (0, 1), (0, 2),
    ],
    [
        (0, 0), 
        (1, 0), 
        (2, 0), (2, 1)
    ], 
    [
        (0, 0), (0, 1), (0, 2), 
        (1, 0)
    ] ,
    [
        (0, 0), (0, 1),
                (1, 1), 
                (2, 1)
    ]
]
PIECE_9 = [
    [
        (0, 0), (0, 1), 
        (1, 0), (1, 1)
    ]
]
PIECE_COLORS = [
    COLOR_BLACK,       
    COLOR_BLUE,        
    COLOR_BROWN,       
    COLOR_ORANGE,      
    COLOR_PURPLE,     
    COLOR_DARK_GREY,   
    COLOR_RED,         
    COLOR_YELLOW,      
    COLOR_CYAN,        
    COLOR_GREEN
]       

PIECES = [
    PIECE_1,
    PIECE_2,
    PIECE_3,
    PIECE_4,
    PIECE_5,
    PIECE_6,
    PIECE_7,
    PIECE_8,
    PIECE_9
]

PIECE_START_OFFSET = {
    1: (2, 2),
    2: (2, 4),
    3: (0, 0),
    4: (2, 2),
    5: (5, 0),
    6: (0, 2),
    7: (0, 1),
    8: (4, 2),
    9: (3, 0),
}
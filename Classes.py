import pygame
from ConstValues import *


class PiecePart():
    __rect = None

    def __init__(self, x, y, width, height):
        self.__rect = pygame.Rect(x, y, width, height)

class Piece():
    __type = 0
    __orientation_index = 0
    __orientation = []
    __rect_list = []
    __selected_piece = False
    __selected_rect = None
    __selected_rect_index = 0

    def __init__(self, type):
        self.__selected_piece = False
        self.__type = type
        self.__orientation_index = 0
        self.__orientation = (PIECES[type - 1])[self.__orientation_index]
        self.__rect_list = []
        self.__selected_rect = None
        self.__selected_rect_index = 0
        for tuple in self.__orientation:
            x_coord = PIECE_WINDOW_x + 2 + tuple[1]*SQUARE_WIDTH + (PIECE_START_OFFSET[self.__type])[1]*SQUARE_WIDTH 
            y_coord =  PIECE_WINDOW_y+ 2 +  tuple[0]*SQUARE_HEIGHT + (PIECE_START_OFFSET[self.__type])[0]*SQUARE_HEIGHT
            self.__rect_list.append(pygame.Rect(x_coord, y_coord, SQUARE_WIDTH, SQUARE_HEIGHT))
        
    def get_type(self):
        return self.__type
    
    def rotate(self):
        self.__orientation_index = (self.__orientation_index + 1) % len(PIECES[self.__type - 1])
        self.__orientation = (PIECES[self.__type - 1])[self.__orientation_index]
        self.__rect_list.clear()
        for tuple in self.__orientation:
            x_coord = PIECE_WINDOW_x + 2 + tuple[1]*SQUARE_WIDTH + (PIECE_START_OFFSET[self.__type])[1]*SQUARE_WIDTH 
            y_coord =  PIECE_WINDOW_y+ 2 +  tuple[0]*SQUARE_HEIGHT + (PIECE_START_OFFSET[self.__type])[0]*SQUARE_HEIGHT
            self.__rect_list.append(pygame.Rect(x_coord, y_coord, SQUARE_WIDTH, SQUARE_HEIGHT))

    def draw(self, screen):
        for rect in self.__rect_list:
            pygame.draw.rect(screen, PIECE_COLORS[-self.__type], rect)
            if(self.__selected_piece):
                pygame.draw.rect(screen, COLOR_WHITE, rect, width = 2)
            else:
                pygame.draw.rect(screen, COLOR_BLACK, rect, width = 2)

    def select_piece(self):
        self.__selected_piece = True
    def unselect_piece(self):
        self.__selected_piece = False

    def hovered_over(self, pos):
        for index, rect in enumerate(self.__rect_list):
            if (rect.collidepoint(pos)):
                self.__selected_rect = rect
                self.__selected_rect_index = index
                return True
        return False
    
    def hovered_over_rect_coord(self, pos):
        for rect in self.__rect_list:
            if (rect.collidepoint(pos)):
                return (rect.x, rect.y)
        return False
    
    def move(self,pos, x, y):
        for index, rect in enumerate(self.__rect_list):
            if(index == self.__selected_rect_index):
                rect.x = x
                rect.y = y
            else:
                relative_rect_coord = ((self.__orientation[index])[0] - (self.__orientation[self.__selected_rect_index])[0], 
                                        (self.__orientation[index])[1] - (self.__orientation[self.__selected_rect_index])[1])
                rect.x = x + relative_rect_coord[1] * SQUARE_WIDTH
                rect.y = y + relative_rect_coord[0] * SQUARE_HEIGHT


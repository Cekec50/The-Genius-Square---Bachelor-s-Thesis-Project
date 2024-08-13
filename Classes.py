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

    def __init__(self, type):
        self.__selected_piece = False
        self.__type = type
        self.__orientation_index = 0
        self.__orientation = (PIECES[-type])[self.__orientation_index]
        self.__rect_list = []
        for tuple in self.__orientation:
            x_coord = PIECE_WINDOW_x + 2 + tuple[1]*SQUARE_WIDTH + (PIECE_START_OFFSET[self.__type])[1]*SQUARE_WIDTH 
            y_coord =  PIECE_WINDOW_y+ 2 +  tuple[0]*SQUARE_HEIGHT + (PIECE_START_OFFSET[self.__type])[0]*SQUARE_HEIGHT
            self.__rect_list.append(pygame.Rect(x_coord, y_coord, SQUARE_WIDTH, SQUARE_HEIGHT))
        

    def rotate(self):
        self.__orientation_index = (self.__orientation_index + 1) % len(PIECES[-self.__type])
        self.__orientation = (PIECES[-self.__type])[self.__orientation_index]
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
        for rect in self.__rect_list:
            if (rect.collidepoint(pos)):
                return True
        return False
    
    # def hovered_over_rect_coord(self, pos):
    #     for rect in self.__rect_list:
    #         if (rect.collidepoint(pos)):
    #             return (rect.x, rect.y)
    #     return False
    
    # def move(self,pos, x, y):
    #     for rect in self.__rect_list:
    #         rect.x = x
    #         rect.y = y

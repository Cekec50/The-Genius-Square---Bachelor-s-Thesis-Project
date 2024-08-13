import pygame


class PiecePart():
    __rect = None

    def __init__(self, x, y, width, height):
        self.__rect = pygame.Rect(x, y, width, height)

class Piece():
    __parts = None

    def __init__(self):
        self.__parts = []

    def add(self, part: PiecePart):
        self.__parts.append(part)

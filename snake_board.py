import os
import random
import cherrypy
from enum import Enum


class SnakeBoard(object):
    def __int__(self, x, y, players):
        self.board = [['' for i in range(x)] for j in range(y)]
        self.snakes = players
        self.num_snakes = len(self.snakes)
        print(self.board)
        print(self.snakes)


class Tile(Enum):
    HEAD = 1
    BODY = 2
    TAIL = 3
    FOOD = 4


if __name__ == '__main__':
    board = SnakeBoard()

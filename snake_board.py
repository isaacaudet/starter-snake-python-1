import os
import random
import cherrypy
from enum import Enum


class SnakeBoard(object):
    def __init__(self, x, y, players):
        self.board = [['' for i in range(x)] for _ in range(y)]
        self.snakes = players
        self.num_snakes = len(self.snakes)
        for i in range(self.num_snakes):
            self.board[self.snakes[i]['body'][0]['y']][self.snakes[i]['body'][0]['x']] = Tile.HEAD

    # def update_board(self, moves):


class Tile(Enum):
    HEAD = 1
    BODY = 2
    TAIL = 3
    FOOD = 4

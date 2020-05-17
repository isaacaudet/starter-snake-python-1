import os
import random
import cherrypy
from enum import Enum


class SnakeBoard(object):
    def __init__(self, x, y, players, you):
        self.board = [['' for i in range(x)] for _ in range(y)]
        self.snakes = players
        self.num_snakes = len(self.snakes)
        self.you = you


class Tile(Enum):
    HEAD = 1
    BODY = 2
    TAIL = 3
    FOOD = 4

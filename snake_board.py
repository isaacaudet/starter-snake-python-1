import os
import random
import cherrypy
import numpy as np
from enum import Enum


class SnakeBoard(object):
    def __init__(self, x, y, players):
        self.board = np.zeros((x, y))
        self.snakes = list()
        self.num_snakes = len(players)
        print(self.num_snakes)
        for i in range(self.num_snakes):
            self.snakes.append(Snake(players[i]['id'], players[i]['head']))
        for i in self.snakes:
            self.board[i.coords[0][0], i.coords[0][1]] = Tile.HEAD.value


    # def update_board(self, moves):


class Snake(object):
    def __init__(self, id_, coords):
        self.id = id_
        self.coords = [[coords['x'], coords['y']]]
        self.whole_snake = {Tile.HEAD: self.coords[0], Tile.BODY: self.coords[0], Tile.TAIL: self.coords[0]}


class Tile(Enum):
    HEAD = 1
    BODY = 2
    TAIL = 3
    FOOD = 4


test = [{'id': 'gs_66HcWHXbQcQ8bjQkKMmKqw7Q', 'name': 'ethans big snake', 'health': 100,
         'body': [{'x': 1, 'y': 5}, {'x': 1, 'y': 5}, {'x': 1, 'y': 5}], 'head': {'x': 1, 'y': 5},
         'tail': {'x': 1, 'y': 5}, 'length': 3, 'shout': ''},
        {'id': 'gs_FwTwbRpcrDbyKtGWkkRMGG8D', 'name': 'snek', 'health': 100,
         'body': [{'x': 5, 'y': 9}, {'x': 5, 'y': 9}, {'x': 5, 'y': 9}], 'head': {'x': 5, 'y': 9},
         'tail': {'x': 5, 'y': 9}, 'length': 3, 'shout': ''}]


def main():
    snakes = list()
    num_snakes = len(test)
    print(num_snakes)
    for i in range(num_snakes):
        snakes.append(Snake(test[i]['id'], test[i]['head']))
    for i in snakes:
        print(i.id)
        print(i.coords)
        print(i.whole_snake)


if __name__ == '__main__':
    main()

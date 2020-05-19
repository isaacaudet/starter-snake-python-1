import os
import random
import cherrypy
import numpy as np
from enum import Enum


class SnakeBoard(object):
    def __init__(self):
        self.board = None
        self.snakes = list()
        self.num_snakes = None

    def start_board(self, x, y, players):
        self.board = np.zeros((x, y))
        self.snakes = list()
        self.num_snakes = len(players)

        for i in range(self.num_snakes):
            self.snakes.append(Snake(players[i]['id'], players[i]['head']))
        for i in self.snakes:
            self.board[i.coords[0][1], i.coords[0][0]] = Tile.HEAD.value

    def update_board(self, snake_moves, food):
        if len(self.num_snakes) > len(snake_moves):
            self.num_snakes = len(snake_moves)
            ids = [i for i in snake_moves[i]['id']]
            for i in self.snakes:
                if i.id not in ids:
                    self.snakes.remove(i)

        self.snakes.update_snake(snake_moves)


class Snake(SnakeBoard):
    def __init__(self, snake_id, coords):
        super().__init__()
        self.id = snake_id
        self.coords = [[coords['x'], coords['y']]]
        self.body = [{Tile.HEAD: self.coords[0]}, {Tile.BODY: self.coords[0]}, {Tile.TAIL: self.coords[0]}]
        self.health = 100
        self.length = 3

    def update_snake(self, snake_moves):
        for i in range(super().num_snakes):
            super().snakes[i]['health'] = snake_moves[i]['health']
            super().snakes[i]['body'] = snake_moves[i]['body']


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

#
# def main():
#     snakes = list()
#     num_snakes = len(test)
#     print(num_snakes)
#     for i in range(num_snakes):
#         snakes.append(Snake(test[i]['id'], test[i]['head']))
#     for i in snakes:
#         print(i.id)
#         print(i.coords)
#         print(i.whole_snake)
#
#
# if __name__ == '__main__':
#     main()

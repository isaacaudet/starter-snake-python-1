import os
import random
import cherrypy
import numpy as np
from enum import Enum


class SnakeBoard(object):

    def __init__(self):
        self.board = None
        self.snakes = list()
        self.num_snakes = int()
        self.food = list()

    def start_board(self, x, y, snakes):
        self.board = np.zeros((x, y))
        self.num_snakes = int(len(snakes))

        for i in range(self.num_snakes):
            self.snakes.append(Snake(snakes[i]))
        for i in self.snakes:
            self.board[i.coords[0][1], i.coords[0][0]] = Tile.HEAD.value

    def update_board(self, snakes, food):
        # update snakes lsit if num_snakes != len(snakes)
        print(self.num_snakes)
        if self.num_snakes > len(snakes):
            self.num_snakes = len(snakes)
            ids = [snakes[i]['id'] for i in range(self.num_snakes)]
            for i in self.snakes:
                if i.id not in ids:
                    self.snakes.remove(i)
        # update snake body
        print('self.snakes:')
        print(self.snakes)
        for i in self.snakes:
            print(i)

        # update board pos
        for snake in self.snakes:
            for i in snake.body:
                self.board[i['y'], i['x']] = Tile.BODY.value
            self.board[snake.head['y'], snake.head['x']] = Tile.HEAD.value
            self.board[snake.tail['y'], snake.tail['x']] = Tile.TAIL.value

        # update food pos
        for i in food:
            self.board[i['y'], i['x']] = Tile.FOOD.value


class Snake(SnakeBoard):
    def __init__(self, snake):
        super().__init__()
        self.id = snake['id']
        self.body = snake['body']
        self.head = snake['head']
        self.tail = snake['tail']
        self.health = 100
        self.length = 3

    def update_snake(self, snake):
        self.health = snake['health']
        self.body = snake['body']
        self.head = snake['head']
        self.tail = snake['tail']
        self.length = snake['length']


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

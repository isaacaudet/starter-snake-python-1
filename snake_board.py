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
        # Create numpy array for board representation. Loads snake and good positions on the board.
        self.board = np.zeros((x, y))
        self.num_snakes = int(len(snakes))

        for i in range(self.num_snakes):
            self.snakes.append(Snake(snakes[i]))
        for i in self.snakes:
            self.board[i.head['y'], i.head['x']] = Tile.HEAD.value

    def update_board(self, snakes, food):
        # update snakes list if num_snakes != len(snakes)
        print(self.num_snakes)
        if self.num_snakes > len(snakes):
            self.num_snakes = len(snakes)
            ids = [snakes[i]['id'] for i in range(self.num_snakes)]
            for i in self.snakes:
                if i.id not in ids:
                    self.snakes.remove(i)

        # update snake body

        print('before snakes:')
        for i in self.snakes:
            print(i.id)
            print(i.body)
            print(i.tail)
            print(i.length)
            print(i.health)
            print()
        for i in range(self.num_snakes):
            self.snakes[i].update_snake(snakes[i])

        print('self.snakes:')
        for i in self.snakes:
            print(i.id)
            print(i.body)
            print(i.tail)
            print(i.length)
            print(i.health)
            print()

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
        self.tail = self.body.pop()
        self.health = 100
        self.length = 3

    def update_snake(self, snake):
        self.health = snake['health']
        self.body = snake['body']
        self.head = snake['head']
        self.tail = self.body.pop()
        self.length = snake['length']


class Tile(Enum):
    HEAD = 1
    BODY = 2
    TAIL = 3
    FOOD = 4

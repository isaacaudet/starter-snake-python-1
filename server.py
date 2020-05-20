import os
import random
import cherrypy
from snake_board import SnakeBoard
import numpy as np

"""
This is a simple Battlesnake server written in Python.
For instructions see https://github.com/BattlesnakeOfficial/starter-snake-python/README.md
"""


class Battlesnake(object):
    def __init__(self):
        self.board = SnakeBoard()
        self.turn = 0

    @cherrypy.expose
    def index(self):
        return "Your Battlesnake is alive!"

    @cherrypy.expose
    def ping(self):
        return "pong"

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def start(self):

        data = cherrypy.request.json
        board_x = data['board']['width']
        board_y = data['board']['height']
        snakes = data['board']['snakes']

        self.board.start_board(board_x, board_y, snakes)
        self.turn += 1
        return {"color": "#03befc", "headType": "shac-caffeine", "tailType": "regular"}

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def move(self):
        self.turn += 1
        print(self.turn)
        data = cherrypy.request.json
        self.board.update_board(data['board']['snakes'], data['board']['food'])
        for i in self.board.board:
            print(i)

        possible_moves = ["up", "down", "left", "right"]
        move = random.choice(possible_moves)

        print(f"MOVE: {move}")
        return {"move": move}

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def end(self):
        data = cherrypy.request.json
        print("END")
        return "ok"


if __name__ == "__main__":
    server = Battlesnake()
    cherrypy.config.update({"server.socket_host": "0.0.0.0"})
    cherrypy.config.update(
        {"server.socket_port": int(os.environ.get("PORT", "8080"))})
    print("Starting Battlesnake Server...")
    cherrypy.quickstart(server)

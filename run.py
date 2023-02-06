"""
Imports random int for placement of ships.
"""
import random


class Game:
    """
    Contains main part of game logic.
    """
    def __init__(self):
        self.board = []
        self.ships = []
        self.guesses = []

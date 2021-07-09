"""
We’ll focus on the following set of requirements while designing the game of chess:
The system should support two online players to play a game of chess.
All rules of international chess will be followed.
Each player will be randomly assigned a side, black or white.
Both players will play their moves one after the other. The white side plays the first move.
Players can’t cancel or roll back their moves.
The system should maintain a log of all moves by both players.
Each side will start with 8 pawns, 2 rooks, 2 bishops, 2 knights, 1 queen, and 1 king.
The game can finish either in a checkmate from one side, forfeit or stalemate (a draw), or resignation.
"""
from enum import Enum
from abc import ABC, abstractmethod
from typing import Tuple


class Side(Enum):
    white = 1
    black = 2


class Piece(ABC):
    def __init__(self, init_position: str):
        row, col = self.parse_position(init_position)
        self.current_position = (row, col)
        self.isKilled = False

    @abstractmethod
    def is_valid_move(self, position: str):
        pass

    @staticmethod
    def parse_position(position: str) -> Tuple[int, int]:
        assert (len(position) == 2) # eg. "A1"
        assert (position[0] in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
        assert (int(position[1]) in range(1, 9))
        row = int(position[1])-1
        column = ord(position[0])-ord('A')
        return row, column

    @property
    def position(self):
        return "{}{}".format(chr(self.current_position[1]+ord('A')), self.current_position[0]+1)

    @position.setter
    def position(self, pos: str):
        self.current_position = self.parse_position(pos)


class Rook(Piece):
    def __init__(self, init_position: str):
        super().__init__(init_position)

    def is_valid_move(self, position: str):
        row, col = self.parse_position(position)
        curr_row, curr_col = self.current_position

        return (row == curr_row and col != curr_col) or (row != curr_row and col == curr_col)


class Pawn(Piece):
    def __init__(self):
        super().__init__()

    def is_valid_move(self):
        pass


class King(Piece):
    def __init__(self):
        super().__init__()

    def is_valid_move(self):
        pass


class Queen(Piece):
    def __init__(self):
        super().__init__()

    def is_valid_move(self):
        pass


class Bishop(Piece):
    def __init__(self):
        super().__init__()

    def is_valid_move(self):
        pass


class Knight(Piece):
    def __init__(self):
        super().__init__()

    def is_valid_move(self):
        pass


class Player:
    def __init__(self, side: Side):
        self.side = side
        self.score = 0

    def update_score(self, add_points: int) -> None:
        self.score += add_points


class Board:
    def __init__(self):
        self.board = [[None for i in range(8)] for j in range(8)]
        self.finished = False

    def init_board(self):
        """
        Method to give initial positions to all the pieces, can be also used to reset the board.
        :return:
        """
        pass

    def can_move(self, player: Side, from_position: str, to_position: str) -> bool:
        pass

    def make_move(self, from_position: str, to_position: str) -> None:
        pass

class Logger:
    def __init__(self):
        pass


class ChessGame:
    def __init__(self):
        self.player1 = Player(Side.white)
        self.player2 = Player(Side.black)
        self.board = Board()
        self.logger = Logger()
        self.active_player = Side.white
        self.winner = None

    def run_game(self):
        self.board.init_board()
        while not self.board.finished:
            if self.board.can_move(self.active_player, from_pos, to_pos):
                self.board.make_move(from_pos, to_pos)



if __name__ == "__main__":




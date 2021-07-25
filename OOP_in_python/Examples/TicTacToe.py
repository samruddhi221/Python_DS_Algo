class Player:
    def __init__(self, id: int, symbol: str):
        self.id = id
        self.symbol = symbol




class Board:
    def __init__(self):
        self.grid = [[None for i in range(3)] for j in range(3)]


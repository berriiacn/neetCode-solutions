import enum

class GridPosition(enum.Enum):
    EMPTY = 0
    YELLOW = 1
    RED = 2

class Grid:
    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.grid = None
        self.initGrid()

    def initGrid(self):
        self.grid = [[GridPosition.EMPTY for _ in range(self.columns)] for _ in range(self.rows)]

    def getGrid(self):
        return self.grid
    
    def getColumnCount(self):
        return self.columns
    
    def getRowCount(self):
        return self.rows

    def placePiece(self, column, piece):
        if column < 0 or column >= self.columns:
            raise ValueError('Invalid column')
        if piece == GridPosition.EMPTY:
            raise ValueError('Invalid piece')
        for row in range(self.rows-1, -1, -1):
            if self.grid[row][column] == GridPosition.EMPTY:
                self.grid[row][column] = piece
                return row
    
    def checkWin(self, row, column, piece, connectN):
        # Check horizontal
        count = 0
        for c in range(self.columns):
            if self.grid[row][c] == piece:
                count += 1
            else:
                count = 0
            if count == connectN:
                return True
        
        # Check vertical
        count = 0
        for r in range(self.rows):
            if self.grid[r][column] == piece:
                count += 1
            else:
                count = 0
            if count == connectN:
                return True
        
        # Check diagonal
        count = 0
        for r in range(self.rows):
            c = column + row - r
            if c >= 0 and c < self.columns and self.grid[r][c] == piece:
                count += 1
            else:
                count = 0
            if count == connectN:
                return True

        # Check anti-diagonal
        count = 0
        for r in range(self.rows):
            c = column - row + r
            if c >= 0 and c < self.columns and self.grid[r][c] == piece:
                count += 1
            else:
                count = 0
            if count == connectN:
                return True

        return False

class Player:
    def __init__(self, name, pieceColor):
        self.name = name
        self.pieceColor = pieceColor

    def getName(self):
        return self.name

    def getPieceColor(self):
        return self.pieceColor
    
class Game:
    def __init__(self, grid, connectN, targetScore)

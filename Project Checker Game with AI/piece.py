"""

Jin Young Park
CS5001 Fall 2021
piece.py
A class for identifying a piece state.

"""


class Piece:
    '''
        Class -- Piece
            Identifies a piece state. Mainly checks where the chosen
            piece from CheckerGame can go to. Also checks available
            moves for all of player's pieces.
        Attributes:
            row -- the row that the piece is on
            col -- the col that the piece is on
            squares -- the current state of the board
        Methods:
            is_on_board -- checks if the piece is on the board
            get_color -- returns the color of the piece
            get_foe -- returns the foe of the piece
            is_king -- checks if the piece is king
    '''
    def __init__(self, row, col, squares):
        '''
            Constructor -- creates a new instance of GameState
            Parameters:
                self -- the current GameState object
        '''
        self.row = row
        self.col = col
        self.squares = squares
        self.TOP = 7  # top row number
        self.BOTTOM = 0  # bottom row number

    def is_on_board(self):
        '''
            Method -- is_on_board
                Checks if the given row and column is on the board
                This is for row and column where the chosen piece
                can go to. Not the location where the chosen piece is.
            Parameter:
                self -- The current Piece object
            Returns:
                Returns True if it is on the board, otherwise return False.
        '''
        if self.row <= self.TOP and self.row >= self.BOTTOM and \
           self.col <= self.TOP and self.col >= self.BOTTOM:
            return True
        return False

    def get_color(self):
        '''
            Method -- get_color
                Gets the color of the piece
            Parameter:
                self -- The current Piece object
            Returns:
                Returns the color of the piece
        '''
        return str(self.squares[self.row][self.col])

    def get_foe(self):
        '''
            Method -- get_foe
                Gets the foe of the piece
            Parameter:
                self -- The current Piece object
            Returns:
                Returns the foe of the piece. "black" if the piece is "red",
                "red" if the piece is "black".
        '''
        if self.get_color() == "black" or self.get_color() == "black_king":
            return "red"
        elif self.get_color() == "red" or self.get_color() == "red_king":
            return "black"

    def is_king(self):
        '''
            Method -- is_king
                Checks if the piece is king
            Parameter:
                self -- The current Piece object
            Returns:
                Returns True if the piece is king, otherwise return False.
        '''
        if self.squares[self.row][self.col] == "black_king" or \
           self.squares[self.row][self.col] == "red_king":
            return True
        return False

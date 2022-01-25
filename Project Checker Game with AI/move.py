"""

Jin Young Park
CS5001 Fall 2021
move.py
A class identifying available moves of each turn.

"""
from piece import Piece


class Move:
    '''
        Class -- Move
            Identifies avaliable moves of each player.
        Attributes:
            squares -- the current state of the board
            turn -- the current turn
        Methods:
            is_on_board -- checks if the piece is on the board
            get_color -- returns the color of the piece
            get_foe -- returns the foe of the piece
            is_king -- checks if the piece is king
    '''
    def __init__(self, squares, turn):
        self.squares = squares
        self.turn = turn
        self.LEN = 8  # The length of the board
        self.nc_move = {}  # dictionary for non-capture moves
        self.c_move = {}  # dictionary for capture moves
        self.after_c = {}  # dictionary for moves after the capture
        self.non_capture_move = []  # list for non-capture moves
        self.capture_move = []  # list for capture moves
        self.after_capture_move = []  # list for moves after the capture

    def get_move(self, row, col, king, color):
        '''
            Method -- get_move
                Leads to helper function depending on piece's color
            Parameter:
                self -- The current Move object
                row -- row of a piece
                col -- col of a piece
                king -- True if king, False if not
                color -- color of a piece
            Returns:
                Nothing. Leads to the helper functions with matching colors.
                If the color of a piece is black, then leads to black_move,
                if the color of a piece is red, then leads to red_move,
                if the piece is king, then leads to king_move.
        '''
        if king:
            self.king_move(row, col)
        else:
            if color == "black":
                self.black_move(row, col)
            elif color == "red":
                self.red_move(row, col)

    def black_move(self, row, col):
        '''
            Method -- black_move
                Get available moves using helper function for black piece.
            Parameter:
                self -- The current Move object
                row -- row of a piece
                col -- col of a piece
            Returns:
                Nothing. Leads to matching helper function
                with specific parameters.
        '''
        self.get_available_moves(row+1, col-1, row+2, col-2)
        self.get_available_moves(row+1, col+1, row+2, col+2)

    def red_move(self, row, col):
        '''
            Method -- red_move
                Get available moves using helper function for red piece.
            Parameter:
                self -- The current Move object
                row -- row of a piece
                col -- col of a piece
            Returns:
                Nothing. Leads to matching helper function
                with specific parameters.
        '''
        self.get_available_moves(row-1, col-1, row-2, col-2)
        self.get_available_moves(row-1, col+1, row-2, col+2)

    def king_move(self, row, col):
        '''
            Method -- king_move
                Get available moves using helper function for king piece.
            Parameter:
                self -- The current Move object
                row -- row of a piece
                col -- col of a piece
            Returns:
                Nothing. Calls helper functions with specific parameters.
                Since king can move in four directions, it calls black_move
                and red_move functions.
        '''
        self.black_move(row, col)
        self.red_move(row, col)

    def get_available_moves(self, row, col, row_cap, col_cap):
        '''
            Method -- get_available_moves
                Calculates available non-capture moves, capture moves,
                and moves after capture for an individual piece.
            Parameter:
                self -- The current Move object
                row -- row to check if available
                col -- col to check if available
                row_cap -- row to check if move after capture is available
                col_cap -- col to check if move after capture is available
            Returns:
                Nothing. Fills can_go, can_capture, capture_and_go lists with
                corresponding available moves.
        '''
        self.loc = row, col
        self.loc_cap = row_cap, col_cap
        nc = Piece(row, col, self.squares)
        if nc.is_on_board() and nc.get_color() == "empty":
            self.non_capture_move.append(self.loc)
        elif nc.is_on_board() and (nc.get_color() == self.foe or
                                   nc.get_color() == self.foe + "_king"):
            self.desired_move = Piece(row_cap, col_cap, self.squares)
            if self.desired_move.is_on_board() and \
               self.desired_move.get_color() == "empty":
                self.capture_move.append(self.loc)
                self.after_capture_move.append(self.loc_cap)

    def piece_state(self):
        '''
            Method -- piece_state
                Get available moves for the whole pieces of this turn's player
                on the board. It is like a collection of available moves
                from available_moves function.
            Parameter:
                self -- The current GameState object
            Returns:
                Nothing. Fills nc_moves, c_moves, after_c with moveable pieces
                as keys and available moves as values for each corresponding
                dictionaries.
        '''
        for row in range(self.LEN):
            for col in range(self.LEN):
                if self.squares[row][col] == self.turn or \
                   self.squares[row][col] == self.turn + "_king":
                    self.piece = Piece(row, col, self.squares)
                    self.king = self.piece.is_king()
                    self.color = self.piece.get_color()
                    self.foe = self.piece.get_foe()
                    self.get_move(row, col, self.king, self.color)
                    self.nc_keys = row, col
                    if len(self.non_capture_move) > 0:
                        self.nc_move[self.nc_keys] = self.non_capture_move
                    if len(self.capture_move) > 0:
                        self.c_move[self.nc_keys] = self.capture_move
                    if len(self.after_capture_move) > 0:
                        self.after_c[self.nc_keys] = self.after_capture_move
                    self.non_capture_move = []
                    self.capture_move = []
                    self.after_capture_move = []

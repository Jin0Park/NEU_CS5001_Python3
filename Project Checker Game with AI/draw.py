"""

Jin Young Park
CS5001 Fall 2021
draw.py
A class for drawing for the game.

"""


import turtle
from piece import Piece


class DrawingFoundation:
    '''
        Class -- DrawingFoundation
            Represents drawing board and pieces of the game.
        Attributes:
            pen -- a turtle function that draws.
            square_size -- the size of a square of the board
            num_squares -- the number of squares of the board
            corner_position -- the location where the turtle starts its drawing
        Methods:
            draw_square -- draws a square of a given size
            draw_circle -- draws a circle of a given size
            draw_king_crown -- draws a crown on a king piece
            create_board -- creates a window for the game
            draw_board -- draws board of given sizes
            draw_pieces -- draws pieces on the board
    '''

    def __init__(self, turtle, square_size, num_squares, corner_position):
        self.pen = turtle
        self.square_size = square_size
        self.num_squares = num_squares
        self.corner_position = corner_position

    def draw_square(self):
        '''
            Function -- draw_square
                Draw a square of a given size.
            Parameters:
                self -- the current DrawingFoundation object
            Returns:
                Nothing. Draws a square in the graphics window.
        '''
        RIGHT_ANGLE = 90
        self.pen.begin_fill()
        self.pen.pendown()
        for i in range(4):
            self.pen.forward(self.square_size)
            self.pen.left(RIGHT_ANGLE)
        self.pen.end_fill()
        self.pen.penup()

    def draw_circle(self):
        '''
            Function -- draw_circle
                Draw a circle of a given size.
            Parameters:
                self -- the current DrawingFoundation object
            Returns:
                Nothing. Draws a circle in the graphics window.
        '''
        self.pen.begin_fill()
        self.pen.pendown()
        self.pen.circle(self.square_size / 2)
        self.pen.end_fill()
        self.pen.penup()

    def draw_king_crown(self):
        '''
            Function -- draw_king_crown
                Draw a king's crown on a king piece.
            Parameters:
                self -- the current DrawingFoundation object
            Returns:
                Nothing. Draws a white circle on a king piece.
        '''
        self.pen.pendown()
        self.pen.circle(self.square_size / 3)
        self.pen.penup()

    def create_board(self):
        '''
            Function -- create_board
                Draw a board of a given size.
            Parameters:
                self -- the current DrawingFoundation object
            Returns:
                Nothing. Create a graphics window.
        '''
        board_size = self.num_squares * self.square_size
        # Create the UI window. This should be the width of the board plus a
        # little margin
        window_size = board_size + self.square_size
        # The extra + SQUARE is the margin
        turtle.setup(window_size, window_size)

        # Set the drawing canvas size. The should be actual board size
        turtle.screensize(board_size, board_size)
        turtle.bgcolor("white")  # The window's background color
        turtle.tracer(0, 0)  # makes the drawing appear immediately

    def draw_board(self):
        '''
            Function -- draw_board
                Draw a board of a given size.
            Parameters:
                self -- the current DrawingFoundation object
            Returns:
                Nothing. Draws a board in the graphics window.
        '''
        for row in range(self.num_squares):
            for col in range(self.num_squares):
                self.pen.color("black", "white")

                x = self.corner_position + col * self.square_size
                y = self.corner_position + row * self.square_size

                if col % 2 != row % 2:
                    self.pen.fillcolor("gray")
                else:
                    self.pen.fillcolor("white")

                self.pen.setposition(x, y)
                self.draw_square()

    def draw_pieces(self, piece_location):
        '''
            Function -- draw_pieces
                Draw a board using draw_circle function.
            Parameters:
                self -- the current DrawingFoundation object
                piece_location -- the nested list of location of each piece
            Returns:
                Nothing. Draws pieces on the board in the graphics window.
        '''
        for row in range(len(piece_location)):
            for col in range(len(piece_location)):
                this_piece = Piece(row, col, piece_location)
                this_color = this_piece.get_color()
                this_king = this_piece.is_king()
                if "black" in this_color:
                    self.pen.color("black", "black")
                elif "red" in this_color:
                    self.pen.color("red4", "red4")
                elif this_color == "empty":
                    continue

                x = self.corner_position + col * self.square_size
                y = self.corner_position + row * self.square_size
                self.pen.setposition(x + self.square_size / 2, y)
                self.draw_circle()

                if this_king:
                    self.pen.color("white")
                    x = self.corner_position + col * self.square_size
                    y = self.corner_position + row * self.square_size
                    self.pen.setposition(x + self.square_size / 2,
                                         y + self.square_size / 6)
                    self.draw_king_crown()

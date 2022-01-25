"""

Jin Young Park
CS5001 Fall 2021
checker game.py
A class where a game is performed by clicking each
piece on the board with helper classes and helper functions.

"""
import random
import turtle
from game_state import GameState
from draw import DrawingFoundation
from move import Move
from piece import Piece


class CheckerGame:
    '''
        Class -- CheckerGame
            Performs game.
        Attributes:
            NUM_SQUARES -- number of squares in each row
            SQUARE -- size of each square on the board
            CORNER -- location of lower left corner of the board
            BOUNDARY -- boundary of the board
            TOP -- the highest row number
            BOTTOM -- the lowest row number
            pen -- turtle used for this game
            squares -- nested list of pieces location on the board
            turn -- current player of the game
            game_state -- variable for calling GameState class
            drawing -- variable for calling DrawingFoundation class
            picked_piece -- the location where  user clicked for first click
            picked_to_go -- the location where user clicked for second click
            if_captured -- Boolean. Whether the player made capture in his turn
            first_click -- Boolean. Whether it is the user's first click
            ai_capture_move -- list for computer's capture moves
            ai_non_capture_move -- list for computer's non-capture moves
            ai_after_and_go -- list for computer's moves after capture
        Methods:
            select_and_move -- leads to helper functions to proceed game.
            user_first_click -- checks if the clicked piece is valid.
            user_second_click -- makes a move for a black piece. Wheter to
                                 non-capture, capture.
            ai_turn -- computer makes move for red pieces
            after_round_updates -- updates game state and UI after each round.
            see_available_moves -- shows available moves for each turn.
    '''
    def __init__(self):
        self.NUM_SQUARES = 8  # The number of squares on each row.
        self.SQUARE = 50  # The size of each square in the checkerboard.
        self.CORNER = -(self.SQUARE * self.NUM_SQUARES) / 2 - 1
        self.BOUNDARY = self.NUM_SQUARES * self.SQUARE / 2
        self.TOP = 7
        self.BOTTOM = 0

        self.pen = turtle.Turtle()
        self.pen.penup()  # This allows the pen to be moved.
        self.pen.hideturtle()  # This gets rid of the triangle cursor.
        self.pen.speed(1)

        # Call the GameState class
        self.game_state = GameState()
        self.squares = self.game_state.non_cap_update(None, None)
        self.turn = self.game_state.current_player
        print("Turn:", self.turn)

        # check available moves
        self.see_available_moves()

        # draw board and pieces
        self.drawing = DrawingFoundation(self.pen, self.SQUARE,
                                         self.NUM_SQUARES, self.CORNER)
        self.drawing.create_board()
        self.drawing.draw_board()
        self.drawing.draw_pieces(self.squares)
        self.picked_piece = []
        self.picked_to_go = []
        self.if_captured = False
        self.first_click = True
        self.ai_capture_move = []  # available capture moves for AI
        self.ai_non_capture_move = []  # available non-capture moves for AI
        self.ai_capture_and_go = []  # available moves after capture for AI

        self.screen = turtle.Screen()
        self.screen.onclick(self.select_and_move)
        turtle.done()  # Stops the window from closing.

    def select_and_move(self, x, y):
        '''
            Function -- select_and_move
                Select a piece by clicking it and move it by making another
                click on a square where it can move to.
            Parameters:
                x -- X coordinate of the click.
                     Automatically provided by Turtle.
                y -- Y coordinate of the click.
                     Automatically provided by Turtle.
            Returns:
                Nothing. Checks if the click is on the board. Then,
                If it's user's first click, calls user_first_click function.
                If it's user's second click, calls user_second_click function.
                If it is computer's turn, calls ai_turn funciton.
        '''
        if x < -(self.BOUNDARY) or x > self.BOUNDARY or \
           y < -(self.BOUNDARY) or y > self.BOUNDARY:
            print("Not on the board")
        else:
            # FIRST CLICK
            if self.first_click:
                self.user_first_click(x, y)
            # SECOND CLICK
            else:
                self.user_second_click(x, y)
            # AI's turn
            if self.turn == "red":
                self.ai_turn()

    def user_first_click(self, x, y):
        '''
            Function -- user_first_click
                Called when the user made a first click for his turn.
            Parameters:
                self -- the current CheckerGame object
            Returns:
                Nothing. Checks if the clicked piece is a valid piece.
                Compares the clicked piece with dictionary lists of
                available moves from Move class.
        '''
        row = int((y - self.CORNER) // self.SQUARE)
        col = int((x - self.CORNER) // self.SQUARE)
        self.picked_piece = row, col
        self.this_piece = Piece(row, col, self.squares)
        self.color = self.this_piece.get_color()
        self.is_king = self.this_piece.is_king()
        self.foe = self.this_piece.get_foe()
        if self.turn in self.color:
            # If a piece can capture, player must choose the piece
            if len(self.pieces.c_move) > 0:
                if self.picked_piece in self.pieces.c_move.keys():
                    self.first_click = False
                else:
                    print("You must pick the piece that can capture.")
                    return
            else:  # if the piece is not moveable
                if self.picked_piece in self.pieces.nc_move.keys():
                    self.first_click = False
                else:
                    print("Pick a piece that can move. Pick again")
                    return
        else:  # If player did not choose his color
            print("Pick the piece with right color")
            return

    def user_second_click(self, x, y):
        '''
            Function -- user_second_click
                Called when the user made a second click for his turn.
            Parameters:
                self -- the current CheckerGame object
            Returns:
                Nothing. Checks if the click is valid pick
                where the piece that the user chose in his first click
                can move to. Compares the click with dictionary lists
                of available moves from Move class. And at the end,
                it updates the game by after_round_updates function.
        '''
        row = int((y - self.CORNER) // self.SQUARE)
        col = int((x - self.CORNER) // self.SQUARE)
        self.picked_to_go = row, col
        # if a piece that can capture were not chosen
        if len(self.pieces.c_move) > 0 and \
           self.picked_piece not in self.pieces.c_move.keys():
            print("You must capture if you can")
            self.first_click = True
            return
        # capture move
        if self.picked_piece in self.pieces.after_c.keys():
            self.value = self.pieces.after_c[self.picked_piece]
            # if picked a piece that can capture, but did not capture
            if self.picked_to_go not in self.value:
                print("You must capture. Pick again")
                self.first_click = True
                return
            if self.picked_to_go == self.value[0]:
                captured_one = self.pieces.c_move[self.picked_piece][0]
            elif self.picked_to_go == self.value[1]:
                captured_one = self.pieces.c_move[self.picked_piece][1]
            self.squares = \
                self.game_state.cap_update(self.picked_to_go,
                                           captured_one,
                                           self.picked_piece)
            self.if_captured = True
        # non-capture move
        elif self.picked_piece in self.pieces.nc_move.keys():
            self.value = self.pieces.nc_move[self.picked_piece]
            if self.picked_to_go in self.value:
                self.squares = \
                    self.game_state.non_cap_update(self.picked_to_go,
                                                   self.picked_piece)
                self.if_captured = False
            else:
                print("Choose a right move. Pick again")
                self.first_click = True
                return
        # if neither capture move nor non-capture move
        else:
            print("Not able to move")
            self.first_click = True
            return
        self.after_round_updates()

    def after_round_updates(self):
        '''
            Function -- after_round_updates
                Call helper functions from GameState, Move, Drawing classes.
            Parameters:
                self -- the current CheckerGame object
            Returns:
                Nothing. Update the king piece if there is one, switch the
                player if meets the condition, check available moves for
                the next player, check if the game is over, and redraw the
                board and pieces.
        '''
        # updates the board and pieces and state of the game
        self.game_state.king_update()
        self.turn = self.game_state.switch_player(self.if_captured)
        self.first_click = True
        self.see_available_moves()
        if self.game_state.check_game_over(self.pieces.nc_move,
                                           self.pieces.c_move):
            quit()
        self.drawing.draw_board()
        self.drawing.draw_pieces(self.squares)

    def ai_turn(self):
        '''
            Function -- ai_turn
                Computer moves the piece according to the dictionary lists
                of available moves
            Parameters:
                self -- the current CheckerGame object
            Returns:
                Nothing. Computer (AI) moves red pieces. The moves chosen from
                the dictionary lists are random.
        '''
        ai_turn = True
        while ai_turn:
            if len(self.pieces.c_move) > 0:  # ai capture a piece
                rand_int = random.randint(0, len(self.pieces.c_move)-1)
                keys_list = list(self.pieces.c_move)
                random_piece = keys_list[rand_int]
                # if ai's selected piece can capture multiple pieces
                if len(self.pieces.c_move[random_piece]) > 1:
                    new_rand_int = random.randint(0, len(self.pieces.c_move
                                                         [random_piece])-1)
                    ai_capture = self.pieces.c_move[random_piece][new_rand_int]
                    ai_capture_and_go = \
                        self.pieces.after_c[random_piece][new_rand_int]
                # if ai's selected piece can capture only one piece
                else:
                    ai_capture = self.pieces.c_move[random_piece][0]
                    ai_capture_and_go = self.pieces.after_c[random_piece][0]
                # update squares as ai captures
                self.squares = \
                    self.game_state.cap_update(ai_capture_and_go, ai_capture,
                                               random_piece)
                self.if_captured = True
            else:  # if there is no piece that ai can capture
                ran_int = random.randint(0, len(self.pieces.nc_move)-1)
                keys_list = list(self.pieces.nc_move)
                random_piece = keys_list[ran_int]
                # if ai's selected piece can move to multiple locations
                if len(self.pieces.nc_move[random_piece]) > 1:
                    new_rand_int = random.randint(0, len(self.pieces.nc_move
                                                         [random_piece])-1)
                    ai_non_capture = \
                        self.pieces.nc_move[random_piece][new_rand_int]
                # if ai's selected piece can move to one location
                else:
                    ai_non_capture = self.pieces.nc_move[random_piece][0]
                # update the square as ai moves a piece
                self.squares = self.game_state.non_cap_update(ai_non_capture,
                                                              random_piece)
                self.if_captured = False
            self.after_round_updates()
            if self.turn == "black":
                ai_turn = False

    def see_available_moves(self):
        '''
            Function -- see_avaliable_moves
                Shows available non-capture, capture, after-capture moves
            Parameters:
                self -- the current CheckerGame object
            Returns:
                Nothing. Shows non-capture, capture, after-capture moves.
        '''
        self.pieces = Move(self.squares, self.turn)
        self.pieces.piece_state()
        self.pieces.nc_move
        print("Pieces can move to:")
        print(self.pieces.nc_move)
        print("Pieces can capture:")
        print(self.pieces.c_move)
        print("After capture moves are:")
        print(self.pieces.after_c)
        print()

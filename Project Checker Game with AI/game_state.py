"""

Jin Young Park
CS5001 Fall 2021
game_state.py
A class representing state of the game.

"""


class GameState:
    '''
        Class -- GameState
            Represents state of the game.
        Attributes:
            current_player -- current player of each turn of the game.
            squaures -- the location of pieces on the board
        Methods:
            switch_player -- switch the current_player for each turn
            non_cap_squares -- convert squares as the player makes
                               a non capturing move
            cap_squares -- convert squres as the player makes a
                           capturing move.
            king_update -- converts a piece to a king piece.
    '''
    def __init__(self):
        '''
            Constructor -- creates a new instance of GameState
            Parameters:
                self -- the current GameState object
        '''
        self.BOARD_LEN = 8
        self.TOP = 7
        self.BOTTOM = 0
        self.current_player = "black"
        self.squares = [
            ["empty", "black", "empty", "black", "empty", "black", "empty",
             "black"],
            ["black", "empty", "black", "empty", "black", "empty", "black",
             "empty"],
            ["empty", "black", "empty", "black", "empty", "black", "empty",
             "black"],
            ["empty", "empty", "empty", "empty", "empty", "empty", "empty",
             "empty"],
            ["empty", "empty", "empty", "empty", "empty", "empty", "empty",
             "empty"],
            ["red", "empty", "red", "empty", "red", "empty", "red", "empty"],
            ["empty", "red", "empty", "red", "empty", "red", "empty", "red"],
            ["red", "empty", "red", "empty", "red", "empty", "red", "empty"]
        ]

    def switch_player(self, captured):
        '''
            Method -- switch_player
                Switch player as the round is over
            Parameter:
                self -- The current GameState object
            Returns:
                Returns "red" if the current player was "black",
                otherwise, return "black"
        '''
        if captured is False:
            if self.current_player == "black":
                self.current_player = "red"
            elif self.current_player == "red":
                self.current_player = "black"
        return self.current_player

    def non_cap_update(self, new_loc, old_loc):
        '''
            Method -- non_cap_update
                Changes the squares list as the user makes a non-capture move
            Parameter:
                self -- The current GameState object
                new_loc -- The location where the piece moves to
                old_loc -- The location where the piece was
            Returns:
                Returns new squares list after changing as demanded
        '''
        if new_loc is None or old_loc is None:
            return self.squares
        # moving the selected piece to where the user wants to move
        else:
            self.squares[new_loc[0]][new_loc[1]] = \
                self.squares[old_loc[0]][old_loc[1]]
            # removing the piece from its old position
            self.squares[old_loc[0]][old_loc[1]] = "empty"
            return self.squares

    def cap_update(self, new_loc, captured_loc, old_loc):
        '''
            Method -- cap_update
                Changes the squares list as the user makes a capture move
            Parameter:
                self -- The current GameState object
                new_loc -- The location where the piece moves to after capture
                captured_loc -- The location where the captured piece was
                old_loc -- The location where the capturing piece was
            Returns:
                Returns new squares list after changing as demanded
        '''
        self.squares[new_loc[0]][new_loc[1]] = \
            self.squares[old_loc[0]][old_loc[1]]
        # removing the piece from its old position
        self.squares[old_loc[0]][old_loc[1]] = "empty"
        self.squares[captured_loc[0]][captured_loc[1]] = "empty"
        return self.squares

    def king_update(self):
        '''
            Method -- king_update
                Changes the squares list as pieces convert to king
            Parameter:
                self -- The current GameState object
                king_loc -- The location where the king piece is
            Returns:
                Returns new squares list after changing as demanded
        '''
        for col in range(self.BOARD_LEN):
            if self.squares[self.TOP][col] == "black":
                self.squares[self.TOP][col] = "black_king"
            if self.squares[self.BOTTOM][col] == "red":
                self.squares[self.BOTTOM][col] = "red_king"
        return self.squares

    def check_game_over(self, nc_move, c_move):
        '''
            Function -- check_game_over
                Checks if the game is over by checking two conditions
            Parameters:
                self -- the current CheckerGame object
            Returns:
                Nothing.
                Declare the winner if the game is over and quit the game.
        '''
        # count red and black pieces to see if game is over
        red_count = 0
        black_count = 0
        no_move = len(nc_move) == 0 and \
            len(c_move) == 0
        for row in range(len(self.squares)):
            for col in range(len(self.squares)):
                if "red" in self.squares[row][col]:
                    red_count += 1
                elif "black" in self.squares[row][col]:
                    black_count += 1
        if red_count == 0 or (no_move and self.current_player == "red"):
            print("GAME OVER! YOU WIN!")
            return True
        if black_count == 0 or (no_move and self.current_player == "black"):
            print("GAME OVER! YOU LOSE!")
            return True

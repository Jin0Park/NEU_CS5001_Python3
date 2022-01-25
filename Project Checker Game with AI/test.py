"""

Jin Young Park
CS5001 Fall 2021
game_state.py
A test file where tests functions in GameState and Piece class.
Functions in Drawing class cannot be tested since it has turtle functions.
Functinos in CheckerGame and Move classes cannot be tested since
the functions do not return anything. But all classes' contructors are tested.
* GAME STARTS WHEN TEST IS RUN. PLEASE CLOSE THE GAME TO PROCEED TEST.

"""

import turtle
from game_state import GameState
from piece import Piece
from draw import DrawingFoundation
from checker_game import CheckerGame
from move import Move


squares = [
    ["empty", "black", "empty", "black", "empty", "black", "empty", "black"],
    ["black", "empty", "black_king", "empty", "black", "empty", "black",
        "empty"],
    ["empty", "black", "empty", "black", "empty", "black", "empty", "black"],
    ["empty", "empty", "red", "empty", "red", "empty", "empty", "empty"],
    ["empty", "empty", "empty", "red", "empty", "empty", "empty", "empty"],
    ["red", "empty", "red_king", "empty", "red", "empty", "red", "empty"],
    ["empty", "red", "empty", "red", "empty", "red", "empty", "red"],
    ["red", "empty", "red", "empty", "red", "empty", "red", "empty"]
]


# Piece class
def test_piece_constructor():
    piece = Piece(1, 5, squares)
    assert(piece.row == 1)
    assert(piece.col == 5)
    assert(piece.squares == squares)


def test_is_on_board():
    piece1 = Piece(0, 8, squares)
    assert(piece1.is_on_board() is False)
    piece2 = Piece(0, 0, squares)
    assert(piece2.is_on_board() is True)
    piece3 = Piece(7, 7, squares)
    assert(piece3.is_on_board() is True)
    piece4 = Piece(8, 0, squares)
    assert(piece4.is_on_board() is False)


def test_get_color():
    piece1 = Piece(0, 1, squares)
    assert(piece1.get_color() == "black")
    piece2 = Piece(7, 0, squares)
    assert(piece2.get_color() == "red")
    piece3 = Piece(3, 5, squares)
    assert(piece3.get_color() == "empty")


def test_get_foe():
    piece1 = Piece(0, 1, squares)
    assert(piece1.get_foe() == "red")
    piece2 = Piece(7, 0, squares)
    assert(piece2.get_foe() == "black")
    piece3 = Piece(3, 5, squares)
    assert(piece3.get_foe() is None)


def test_is_king():
    piece1 = Piece(1, 2, squares)
    assert(piece1.is_king() is True)
    piece2 = Piece(5, 2, squares)
    assert(piece2.is_king() is True)
    piece3 = Piece(3, 5, squares)
    assert(piece3.is_king() is False)


# GameState class
def test_gamestate_constructor():
    state = GameState()
    assert(state.current_player == "black")
    assert(state.squares == [
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
        ])


def test_switch_player():
    # player in the beginning of the game is set to "black"
    state1 = GameState()
    # if the player did not capture
    assert(state1.switch_player(False) == "red")
    # if the player did capture
    state2 = GameState()
    assert(state2.switch_player(True) == "black")


def test_king_update():
    state1 = GameState()
    state1.squares = [
      ["empty", "red", "empty", "black", "empty", "black", "empty", "black"],
      ["empty", "empty", "empty", "black", "empty", "empty", "empty", "empty"],
      ["empty", "black", "empty", "empty", "empty", "black", "empty", "empty"],
      ["empty", "empty", "black", "empty", "red", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["red", "empty", "empty", "empty", "empty", "empty", "red", "empty"],
      ["empty", "red", "empty", "red", "empty", "red", "empty", "red"],
      ["empty", "empty", "empty", "empty", "red", "empty", "black", "empty"]
    ]
    # piece at row 0 col 1 is changed to "red_king" and
    # piece at row 7 col 6 is changed to "black_king"
    assert(state1.king_update() == [
      ["empty", "red_king", "empty", "black", "empty", "black", "empty",
       "black"],
      ["empty", "empty", "empty", "black", "empty", "empty", "empty", "empty"],
      ["empty", "black", "empty", "empty", "empty", "black", "empty", "empty"],
      ["empty", "empty", "black", "empty", "red", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["red", "empty", "empty", "empty", "empty", "empty", "red", "empty"],
      ["empty", "red", "empty", "red", "empty", "red", "empty", "red"],
      ["empty", "empty", "empty", "empty", "red", "empty", "black_king",
       "empty"]
    ])


def test_check_game_over():
    # no red pieces are on the board
    state1 = GameState()
    state1.squares = [
      ["empty", "empty", "empty", "black", "empty", "black", "empty", "black"],
      ["empty", "empty", "empty", "black", "empty", "empty", "empty", "empty"],
      ["empty", "black", "empty", "empty", "empty", "black", "empty", "empty"],
      ["empty", "empty", "black", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "black", "empty"]
    ]
    assert(state1.check_game_over({}, {}) is True)

    # no black pieces are on the board
    state2 = GameState()
    state2.squares = [
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "red", "empty", "empty", "empty", "empty"],
      ["empty", "red", "empty", "empty", "empty", "red", "empty", "empty"],
      ["empty", "empty", "red", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["red", "empty", "empty", "empty", "empty", "empty", "red", "empty"],
      ["empty", "red", "empty", "red", "empty", "red", "empty", "red"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "red", "empty"]
    ]
    assert(state2.check_game_over({}, {}) is True)
    # there is a red piece but it has no available move
    state3 = GameState()
    state3.squares = [
      ["empty", "empty", "empty", "black", "empty", "black", "empty", "black"],
      ["empty", "empty", "empty", "black", "empty", "empty", "empty", "empty"],
      ["empty", "black", "empty", "empty", "empty", "black", "empty", "empty"],
      ["empty", "empty", "black", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "black", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "black", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "red"]
    ]
    assert(state3.check_game_over({}, {}) is True)
    # there is a black piece but it has no available move
    state4 = GameState()
    state4.squares = [
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "black"],
      ["empty", "empty", "empty", "red", "empty", "empty", "red", "empty"],
      ["empty", "red", "empty", "empty", "empty", "red", "empty", "empty"],
      ["empty", "empty", "red", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["red", "empty", "empty", "empty", "empty", "empty", "red", "empty"],
      ["empty", "red", "empty", "red", "empty", "red", "empty", "red"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"]
    ]
    assert(state4.check_game_over({}, {}) is True)


def test_non_cap_update():
    # black move
    state1 = GameState()
    state1.squares = [
      ["empty", "empty", "empty", "black", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"]
    ]
    assert(state1.non_cap_update((1, 2), (0, 3)) == [
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "black", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"]
    ])

    # red move
    state2 = GameState()
    state2.squares = [
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["red", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "red", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"]
    ]
    assert(state2.non_cap_update((5, 2), (6, 1)) == [
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["red", "empty", "red", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"]
    ])


def test_cap_update():
    # black move
    state1 = GameState()
    state1.squares = [
      ["empty", "empty", "empty", "black", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "red", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"]
    ]
    assert(state1.cap_update((2, 1), (1, 2), (0, 3)) == [
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "black", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"]
    ])

    # red move
    state2 = GameState()
    state2.squares = [
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["red", "empty", "black", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "red", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"]
    ]
    assert(state2.cap_update((4, 3), (5, 2), (6, 1)) == [
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "red", "empty", "empty", "empty", "empty"],
      ["red", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"]
    ])


# DrawingFoundation class
def test_drawingfoundation_constructor():
    turt = turtle.Turtle()
    draw = DrawingFoundation(turt, 8, 8, 200)
    assert(draw.pen == turt)
    assert(draw.square_size == 8)
    assert(draw.num_squares == 8)
    assert(draw.corner_position == 200)


# Move class
def test_move_constructor():
    locs = [
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "red", "empty", "empty", "empty", "empty"],
      ["red", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
      ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"]
    ]
    move = Move(locs, "black")
    assert(move.squares == locs)
    assert(move.turn == "black")


# CheckerGame class
# GAME STARTS WHEN TEST IS RUN. PLEASE CLOSE THE GAME TO PROCEED TEST.
def test_checkergame_constructor():
    checker = CheckerGame()
    # check squares in the beginning of the game
    assert(checker.squares == [
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
        ])
    # check turn in the beginning of the game
    assert(checker.turn == "black")

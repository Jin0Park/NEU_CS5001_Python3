"""

Jin Young Park
CS5001 Fall 2021
HW04 test_hangman.py

Tests functions in hangman.py

"""

from hangman import convert_letter_to_underscore, check_if_word, \
                    check_word_with_answer, check_if_already_guessed, \
                    store_letter, guesses_so_far, check_game_over, \
                    secret_word_to_list, check_if_got_all_letters, \
                    check_if_win


def test_convert_letter_to_underscore():
    assert(convert_letter_to_underscore([], "coke") == "____")
    assert(convert_letter_to_underscore(["D", "I", "K"], "DIETCOKE") ==
           "DI____K_")
    assert(convert_letter_to_underscore(["S", "U", "G", "A", "R"], "SUGAR") ==
           "SUGAR")


def test_check_if_word():
    assert(check_if_word("coke") is True)
    assert(check_if_word("c") is False)
    # invalid input, but count it as a letter (take it as a user guess)
    assert(check_if_word(" ") is False)


def test_check_word_with_answer():
    assert(check_word_with_answer("COKE", "COKE") is True)
    assert(check_word_with_answer("COKE", "DIETCOKE") is False)
    assert(check_word_with_answer("ZEROSUGAR", "NOSUGAR") is False)


def test_check_if_already_guessed():
    assert(check_if_already_guessed("C", ["C"]) is True)
    assert(check_if_already_guessed("O", []) is False)
    assert(check_if_already_guessed("O", ["C", "P"]) is False)


def test_store_letter():
    assert(store_letter("C", []) == ["C"])
    assert(store_letter("C", ["O", "K", "E"]) == ["O", "K", "E", "C"])
    assert(store_letter("A", ["P", "L", "E"]) == ["P", "L", "E", "A"])


def test_guesses_so_far():
    assert(guesses_so_far(["C", "O", "K"]) == "Your guesses so far: COK")
    assert(guesses_so_far(["C"]) == "Your guesses so far: C")
    assert(guesses_so_far(["S", "U", "G", "R"]) == "Your guesses so far: SUGR")


def test_check_game_over():
    # case when one of winning condition is satisfied before used all attempts
    assert(check_game_over(True, False, 4) is True)
    # case when no winning condition is satisfied and used all the attempts
    assert(check_game_over(False, False, 0) is True)
    # case when no winning condition is satisfied but a few attempts left
    assert(check_game_over(False, False, 3) is False)


def test_secret_word_to_list():
    assert(secret_word_to_list("COKE") == ["C", "O", "K", "E"])
    assert(secret_word_to_list("ZEROSUGAR") ==
           ["Z", "E", "R", "O", "S", "U", "G", "A", "R"])
    assert(secret_word_to_list("DIET") == ["D", "I", "E", "T"])


def test_check_if_got_all_letters():
    assert(check_if_got_all_letters(["C", "O", "K", "E"], "COKE") is True)
    assert(check_if_got_all_letters(["O", "C", "K"], "COOK") is True)
    assert(check_if_got_all_letters([], "COKE") is False)


def test_check_if_win():
    # cases that one of winning conditions is satisfied
    assert(check_if_win(True, False) is True)
    assert(check_if_win(False, True) is True)
    # case that no winning conditions is satisfied
    assert(check_if_win(False, False) is False)
    # case that both of winning conditions are satisfied
    assert(check_if_win(True, True) is True)

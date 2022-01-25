"""
Jin Young Park
CS5001 Fall 2021
HW06 test_vowelsearch.py
Tests check_list, check_string, check_letter_is_vowel functions
in vowelsearch.py
"""

from vowelsearch import check_list, check_string, check_letter_is_vowel


def test_check_letter_is_vowel():
    assert(check_letter_is_vowel("a") is True)
    assert(check_letter_is_vowel("e") is True)
    assert(check_letter_is_vowel("i") is True)
    assert(check_letter_is_vowel("o") is True)
    assert(check_letter_is_vowel("u") is True)
    assert(check_letter_is_vowel("p") is False)
    assert(check_letter_is_vowel("r") is False)
    assert(check_letter_is_vowel("s") is False)
    assert(check_letter_is_vowel("n") is False)
    assert(check_letter_is_vowel("") is False)


def test_check_string():
    assert(check_string("ana") is True)
    assert(check_string("hhp") is False)
    assert(check_string("PaRK") is True)
    assert(check_string("cOmpUtEr") is True)
    assert(check_string("PWrd") is False)
    assert(check_string("") is False)


def test_check_list():
    assert(check_list(["garage", "this", "man"]) is True)
    assert(check_list(["fff", "this", "man"]) is False)
    assert(check_list(["park", "jin", "Young"]) is True)
    assert(check_list(["cs", "comp", "uter"]) is False)
    assert(check_list([""]) is False)

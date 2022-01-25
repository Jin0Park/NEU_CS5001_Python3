"""

Jin Young Park
CS5001 Fall 2021
HW3 test_sizefinder.py
The program contains test functions for every function in sizefinder.py
besides main function.

"""


from sizefinder import find_size, find_kids, find_womens, find_mens,\
                       size_statement


def test_find_size():
    assert(find_size(30, 28, 40, 2) == "M")
    assert(find_size(20, 28, 40, 2) == "not available")
    assert(find_size(39, 28, 41, 3) == "XL")


def test_find_kids():
    assert(find_kids(30) == "L")
    assert(find_kids(36) == "not available")
    assert(find_kids(35.9) == "XXL")


def test_find_womens():
    assert(find_womens(30) == "S")
    assert(find_womens(36) == "XL")
    assert(find_womens(42) == "not available")


def test_find_mens():
    assert(find_mens(30) == "not available")
    assert(find_mens(36) == "S")
    assert(find_mens(51.6) == "XXXL")


def test_size_statement():
    assert(size_statement("not available", "XXXL", "L") ==
           "Your size choices: \nKids size: " + "not available" +
           "\nWomens size: " + "XXXL" + "\nMens size: " + "L")
    assert(size_statement("XXL", "L", "S") ==
           "Your size choices: \nKids size: " + "XXL" + "\nWomens size: " +
           "L" + "\nMens size: " + "S")
    assert(size_statement("not available", "not available", "not available")
           == "Sorry, we don't carry your size")

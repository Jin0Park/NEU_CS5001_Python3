"""

Jin Young Park
CS5001 Fall 2021
HW04 test_palindrome.py

Tests is_palindrome function in palindrome.py

"""

from palindrome import is_palindrome


def test_is_palindrome():
    # one character cases
    assert(is_palindrome("c") is False)
    assert(is_palindrome("!") is False)
    assert(is_palindrome("a") is False)
    assert(is_palindrome("K") is False)
    assert(is_palindrome(";") is False)
    assert(is_palindrome("l") is False)

    # palindrome cases
    assert(is_palindrome("racecar") is True)
    assert(is_palindrome("deified") is True)
    assert(is_palindrome("Aibohphobia") is True)
    assert(is_palindrome("noon") is True)
    assert(is_palindrome("civic") is True)

    # palindrome cases ignoring spaces
    assert(is_palindrome("madam im adam") is True)
    assert(is_palindrome("k a  yak") is True)
    assert(is_palindrome("r        ot      or") is True)
    assert(is_palindrome("able was i ere i saw elba") is True)
    assert(is_palindrome("mr owl ate my metal worm") is True)

    # palindrome cases ignoring letter cases
    assert(is_palindrome("RevIVEr") is True)
    assert(is_palindrome("TaCocAt") is True)
    assert(is_palindrome("TaTTaRraTtAt") is True)
    assert(is_palindrome("MuRDrUm") is True)
    assert(is_palindrome("TooBadIHidABoot") is True)

    # not palindrome cases
    assert(is_palindrome("jin") is False)
    assert(is_palindrome("coke") is False)
    assert(is_palindrome("EVER") is False)
    assert(is_palindrome("NEVER") is False)
    assert(is_palindrome("revivers") is False)
    assert(is_palindrome("defieder") is False)

"""
Jin Young Park
CS5001 Fall 2021
HW05 test_password.py
Test secure_password function in password.py
"""
from password import check_length, string_to_list, secure_password


def test_check_length():
    assert(check_length("!!!!!!!CDCDCDabv123") is False)
    assert(check_length("AB!@34CEcd") is True)
    assert(check_length("AB!@") is False)


def test_string_to_list():
    assert(string_to_list("ABCDE") == ["A", "B", "C", "D", "E"])
    assert(string_to_list("!@34CEcd") ==
           ["!", "@", "3", "4", "C", "E", "c", "d"])


def test_secure_password():
    # FALSE CASES
    # case where it does not meet the length condition
    assert(secure_password("!!!!!!!CDCDCDabv123") is False)
    assert(secure_password("!@34CEcd") is False)
    # case where it does not have uppercase and lowercase letter
    assert(secure_password("!@#$1313123") is False)
    assert(secure_password("!@#!@#1!@#!") is False)
    # case where it does not have uppercase letter and digit
    assert(secure_password("cdcdcdcdcd!") is False)
    assert(secure_password("!@#$fourfour") is False)
    # case where it does not have uppercase letter and special characters
    assert(secure_password("noupper123") is False)
    assert(secure_password("i123456789") is False)
    # case where it does not have lowercase letter and digit
    assert(secure_password("!@#$ABCDE") is False)
    assert(secure_password("!@#!@#A!@#!") is False)
    # case where it does not have lowercase letter and special characters
    assert(secure_password("123123ABCD") is False)
    assert(secure_password("ABCDEFG1") is False)
    # case where it does not have digit and special characters
    assert(secure_password("abcdABCDEF") is False)
    assert(secure_password("onlylowUP") is False)
    # case where it has special characters that are not allowed
    assert(secure_password("?123abcABC") is False)
    assert(secure_password("!@ab12AB&*") is False)
    # TRUE CASES
    assert(secure_password("!123abcABC") is True)
    assert(secure_password("NEUcs5001@") is True)
    assert(secure_password("!@#$1aABC") is True)
    assert(secure_password("!1Aa!1Aa!1Aa") is True)

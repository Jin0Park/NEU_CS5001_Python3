"""
Jin Young Park
CS5001 Fall 2021
HW05 test_upc.py
Test functions in upc.py
"""
from upc import check_string_is_only_num, remove_space, string_to_list,\
                list_to_backward_in_int, calculate_sum_of_upc, is_valid_upc


def test_check_string_is_only_num():
    assert(check_string_is_only_num("123456798") is True)
    assert(check_string_is_only_num("123456asdFE") is False)
    assert(check_string_is_only_num("123456!@#") is False)


def test_remove_space():
    assert(remove_space("a b c d") == "abcd")
    assert(remove_space("1 2        3 4") == "1234")
    assert(remove_space("1 A 2 B 3 c 4 d ! @") == "1A2B3c4d!@")


def test_string_to_list():
    assert(string_to_list("9780128053904") ==
           ["9", "7", "8", "0", "1", "2", "8", "0", "5", "3", "9", "0", "4"])
    assert(string_to_list("123456789") ==
           ["1", "2", "3", "4", "5", "6", "7", "8", "9"])


def test_list_to_backward_in_int():
    assert(list_to_backward_in_int(["5", "1", "2", "8"]) == [8, 2, 1, 5])
    assert(list_to_backward_in_int(["1", "2", "3"]) == [3, 2, 1])
    assert(list_to_backward_in_int(["51", "61", "82", "101"]) ==
           [101, 82, 61, 51])


def test_calculate_sum_of_upc():
    assert(calculate_sum_of_upc("123456789") == 85)
    assert(calculate_sum_of_upc("5012345678900") == 90)
    assert(calculate_sum_of_upc("9780128053904") == 80)


def test_is_valid_upc():
    # case where the string contains only numbers but is not valid
    assert(is_valid_upc("123456789") is False)
    # True cases
    assert(is_valid_upc("5012345678900") is True)
    assert(is_valid_upc("9 7 8 0 1 2 8 0 5 3 9 0 4") is True)
    assert(is_valid_upc("22334545453") is True)
    # cases where the string contains other charaters than number
    assert(is_valid_upc("123abc789") is False)
    assert(is_valid_upc("123456789!") is False)

"""
Jin Young Park
CS5001 Fall 2021
HW05 upc.py
The program checks if the upc digits are valid or invalid.

Contains five functions: remove_space, check_string_is_only_num,
                string_to_list, list_to_backward, calculate_sum_of_upc,
                is_valid_upc
"""


def remove_space(string):
    """
        Function -- remove_space
            Remove blank spaces in a string
        Parameters:
            string -- a given upc digits in string
        Returns:
            Returns a string without any blank spaces.
    """
    no_space = string.replace(" ", "")
    return no_space


def check_string_is_only_num(string):
    """
        Function -- check_string_is_only_integers
            Check if there is no character other than number
        Parameters:
            string -- a given upc digits in string
        Returns:
            Returns True if the string only consist number.
    """
    return string.isnumeric()


def string_to_list(string):
    """
        Function -- string_to_list
            Converts string into list by each character
        Parameters:
            string -- a given upc digits in string
        Returns:
            Returns a list of each character or digit in the given string.
    """
    string_in_list = []
    string_in_list[:0] = string
    return string_in_list


def list_to_backward_in_int(list):
    """
        Function -- list_to_backward
            Convert a list into backward order to read
            the upc right to left order
        Parameters:
            list -- a list returned by string_to_list function containing
                    each digit in the given string as elements
        Returns:
            Returns a list of the given list in backward order and convert
            the elements into int.
    """
    list_in_backward = []
    for i in range(len(list), 0, -1):
        list_in_backward.append(int(list[i - 1]))
    return list_in_backward


def calculate_sum_of_upc(string):
    """
        Function -- list_to_backward
            Calculate the arranged upc digits (right to left) by adding
            each digit (multiply digits in odd positions by 3)
        Parameters:
            string -- a given upc digits in string
        Returns:
            Return the calculated sum followed by the instruction.
            Use string_to_list, list_to_backward functions to
            set up elements needed for calculation.
    """
    # number to be multiplied to numbers in odd positions are 3
    NUM_TO_MULTIPLY = 3
    sum = 0
    # convert the string to a list of each character
    upc_in_list = string_to_list(string)
    # have the list backward
    upc_backward = list_to_backward_in_int(upc_in_list)
    # calculate the sum of the digits followed by instruction
    for i in range(len(upc_backward)):
        if i % 2 != 0:
            upc_backward[i] *= NUM_TO_MULTIPLY
        sum += upc_backward[i]
    return sum


def is_valid_upc(string):
    """
        Function -- is_valid_upc
            Check if the given upc value is valid or not
        Parameters:
            string -- a given upc digits in string
        Returns:
            Use remove_space, check_string_is_only_num, string_to_list,
            list_to_backward, calculate_sum_of_upc functions to get the
            calculated sum of upc digits followed by the instruction.
            Return True if the sum is multiple of 10 (valid upc),
            or return False if not (invalid upc or contains character
            other than number).
    """
    MULTIPLE_OF_TO_BE_VALID = 10
    # remove space from the string
    no_space_string = remove_space(string)
    # if string has only numbers, then see if it is a valid upc
    if check_string_is_only_num(no_space_string) is True:
        sum = calculate_sum_of_upc(no_space_string)
        if sum % MULTIPLE_OF_TO_BE_VALID == 0:
            return True
    return False

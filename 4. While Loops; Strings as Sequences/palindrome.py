"""

Jin Young Park
CS5001 Fall 2021
HW04 panlindrome.py
The function is_palindrome checks if the given stirng is a palindrome or not

"""


def is_palindrome(string):
    """
        Function -- is_palindrome
            Checks if the given string is palindrome or not
        Parameters:
            string -- a string given in the main function
        Returns:
            Returns True if the string (after spaces are removed) is
            palindrome, returns False if not.
    """
    # Lower and remove spaces from the string
    new_string = string.lower().replace(" ", "")
    # if the length of the string is one or zero return False
    if len(new_string) <= 1:
        return False
    else:
        # while the length of string is higher than 0
        while len(new_string) > 0:
            last_index = len(new_string) - 1
            # if the first letter and the last letter of string is same
            # remove those letters from the string
            if new_string[0] == new_string[last_index]:
                new_string = new_string[1:-1]
            # if the first and last letter of string is not same, return False
            else:
                return False
        return True

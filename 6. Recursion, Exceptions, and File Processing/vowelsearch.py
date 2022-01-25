"""

Jin Young Park
CS5001 Fall 2021
HW06 vowelsearch.py
The program contains a recursive function which checks if every string in
a list has a vowel or not.

"""


def check_letter_is_vowel(letter):
    '''
        Function -- check_letter_is_vowel
            checks if a letter is a vowel.
        Parameters:
            letter -- a character in a given string
        Returns:
            Returns true if the letter is a vowel. Otherwise, return False.
    '''
    VOWEL = ("a", "e", "i", "o", "u")
    return letter.lower() in VOWEL


def check_string(string):
    '''
        Function -- check_string
            checks if a string has a vowel using check_letter_is_vowel
            function.
        Parameters:
            string -- a string in a given list
        Returns:
            Returns true if the string contains a vowel.
            Otherwise, return False.
    '''
    if len(string) == 0:
        return False
    elif len(string) == 1:
        return check_letter_is_vowel(string)
    else:
        if check_letter_is_vowel(string[0]) is True:
            return True
        else:
            return check_letter_is_vowel(string[0]) or check_string(string[1:])


def check_list(lst):
    '''
        Function -- check_list
            checks if every string in a list has a vowel using
            check_letter_is_vowel and check_string functions.
        Parameters:
            lst -- a given list
        Returns:
            Returns true if every string in a list has a vowel.
            Otherwise, return false.
    '''
    if len(lst) == 0:
        return False
    elif len(lst) == 1:
        return check_string(lst[0])
    else:
        return check_string(lst[0]) and check_list(lst[1:])


def main():
    print(check_list(["aba", "bab", "acd"]))
    print(check_list([]))
    print(check_list(["aba", "bBb", "acd"]))
    print(check_list(["a", "i", "e"]))


if __name__ == "__main__":
    main()

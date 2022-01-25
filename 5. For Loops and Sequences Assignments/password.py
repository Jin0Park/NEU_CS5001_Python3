"""
Jin Young Park
CS5001 Fall 2021
HW05 password.py
The program checks if the password is a proper password
meeting with all the conditions.

Contains three functions: check_length, string_to_list, secure_password
"""


def check_length(string):
    """
        Function -- check_length
            Check the length of the string if it falls into the instruction
        Parameters:
            string -- a given password in string
        Returns:
            Return True if the length of string is in between 9 and 12
            inclusively or return False.
    """
    MINIMUM_LENGTH = 9
    MAXIMUM_LENGTH = 12
    return (len(string) >= MINIMUM_LENGTH and len(string) <= MAXIMUM_LENGTH)


def string_to_list(string):
    """
        Function -- string_to_list
            Converts string into list by each character
        Parameters:
            string -- a given password in string
        Returns:
            Returns a list of each character or digit in the given string.
    """
    string_in_list = []
    string_in_list[:0] = string
    return string_in_list


def secure_password(string):
    """
        Function -- secure_password
            Checks if the given string is proper password or not
        Parameters:
            string -- a password needed to be checked under a few conditions
        Returns:
            Returns True
            1) if the string is between 9 and 12 characters long inclusive,
            2) if it has at least one lowercase and one uppercase letter,
            3) if it has at least one digit,
            4) if it has at least one of specific special characters: $,#,@,! ,
            5) if it does not has any special characters other than those four.
            Returns False otherwise.
    """
    # Three out of Four requirements should be met for the second part of rules
    PART_TWO_RULE_AT_LEAST = 3
    # returns false if it does not meet the length condition (rule #1)
    if check_length(string) is False:
        return False

    # default variable for the four conditions are False
    if_there_digit = False
    if_there_uppercase = False
    if_there_lowercase = False
    if_there_special_character = False
    # a list of four special characters
    special_characters = ("$", "#", "@", "!")

    # convert the string into a list of each character
    string_in_list = string_to_list(string)

    # if statement to check if it is proper password
    for i in string_in_list:
        if i.isupper():
            if_there_uppercase = True
        elif i.islower():
            if_there_lowercase = True
        elif i.isnumeric():
            if_there_digit = True
        else:
            # returns false if contains special character other than the four
            # (rule #3)
            if i not in special_characters:
                return False
            else:
                if_there_special_character = True

    # add the conditions up to see if at least three requirements are met
    how_many_conditions = if_there_digit + if_there_uppercase + \
        if_there_lowercase + if_there_special_character
    if how_many_conditions >= PART_TWO_RULE_AT_LEAST:
        return True
    return False

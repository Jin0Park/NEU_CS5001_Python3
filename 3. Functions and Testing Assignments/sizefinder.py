"""

Jin Young Park
CS5001 Fall 2021
HW3 sizefinder.py
The program prompts the user for their chest measurement in inches
then return the user’s size according to the company’s three
size charts: kids, women, and men.
Contains five functions: find_size, find_kids, find_womens, find_mens,
                         size_statement

Test cases:
1)
Chest measurement in inches: 48
Your size choices:
Kids size: not available
Womens size: not available
Mens size: XXL

2)
Chest measurement in inches: 32.5
Your size choices:
Kids size: XL
Womens size: M
Mens size: not available

3)
Chest measurement in inches: 22
Sorry, we don't carry your size

4)
Chest measurement in inches: 35
Your size choices:
Kids size: XXL
Womens size: L
Mens size: S

"""


def main():
    user_size = float(input("Chest measurement in inches: "))
    corresponding_kids = find_kids(user_size)
    corresponding_womens = find_womens(user_size)
    corresponding_mens = find_mens(user_size)
    size_statement(corresponding_kids, corresponding_womens,
                   corresponding_mens)


def find_size(chest_size, min, max, level):
    """
        Function -- find_size
            Using the values of parameters to find out which size in the
            company's size charts that the user's chest size fits to.
        Parameters:
            chest_size -- the user's chest size value in float which the user
                          wants to compare with the company's size charts.
            min -- the minimum value of a chart.
            max -- the maximum value of a chart.
            level -- the interval of each chart's size.
        Returns corresponding sizes of each chart based on the min, max, level
        values of kids, womens, mens charts each.
        If the user's chest size does not have a match with any of the sizes
        in the size chart, then it would return not available for that chart.
    """
    # If the user's chest size is in between min and max values,
    # then compare with each chart and return the corresponding size.
    if chest_size < max and chest_size >= min:
        # Size S
        if chest_size >= min and chest_size < min + level:
            return "S"
        # Size M
        elif chest_size >= min + level and chest_size < min + level * 2:
            return "M"
        # Size L
        elif chest_size >= min + level * 2 and chest_size < min + level * 3:
            return "L"
        # Size XL
        elif chest_size >= min + level * 3 and chest_size < min + level * 4:
            return "XL"
        # Size XXL
        elif chest_size >= min + level * 4 and chest_size < min + level * 5:
            return "XXL"
        # Size XXXL
        else:
            return "XXXL"
    else:
        return "not available"


def find_kids(chest_size):
    """
        Function -- find_kids
            Using the find_size function to determine which kid's size
            the user's chest size corresponds.
        Parameters:
            chest_size -- the user's chest size in float
        Returns the corresponding kid's size in the company's size charts.
        The function contains constants to be used for the parameters for
        find_size function.
    """
    # minimum value of kid's chart
    KIDS_MIN = 26
    # maximum value of kid's chart
    KIDS_MAX = 36
    # interval of kid's chart's sizes
    KIDS_LEVEL = 2
    # calling the find_size function
    kids_size = find_size(chest_size, KIDS_MIN, KIDS_MAX, KIDS_LEVEL)
    return kids_size


def find_womens(chest_size):
    """
        Function -- find_womens
            Using the find_size function to determine which women's size
            the user's chest size corresponds.
        Parameters:
            chest_size -- the user's chest size in float
        Returns the corresponding women's size in the company's size charts.
        The function contains constants to be used for the parameters for
        find_size function.
    """
    # minimum value of women's chart
    WOMENS_MIN = 30
    # maximum value of women's chart
    WOMENS_MAX = 42
    # interval of women's chart's sizes
    WOMENS_LEVEL = 2
    # calling the find_size function
    womens_size = find_size(chest_size, WOMENS_MIN, WOMENS_MAX, WOMENS_LEVEL)
    return womens_size


def find_mens(chest_size):
    """
        Function -- find_mens
            Using the find_size function to determine which men's size
            the user's chest size corresponds.
        Parameters:
            chest_size -- the user's chest size in float
        Returns the corresponding men's size in the company's size charts.
        The function contains constants to be used for the parameters for
        find_size function.
    """
    # minimum value of men's chart
    MENS_MIN = 34
    # maximum value of men's chart
    MENS_MAX = 52
    # interval of men's chart's sizes
    MENS_LEVEL = 3
    # calling the find_size function
    mens_size = find_size(chest_size, MENS_MIN, MENS_MAX, MENS_LEVEL)
    return mens_size


def size_statement(kids, womens, mens):
    """
        Function -- size_statement
            Using the values of variables determined from the functions above
            to inform the user which size charts they would fit
        Parameters:
            kids -- Kid's size value that corresponds to the user's chest size
                    returned from kids_size function.
            womens -- Women's size value that corresponds to the user's chest
                      size returned from womens_size function.
            mens -- Men's size value that corresponds to the user's chest size
                    returned from mens_size function.
        Returns:
            If all three sizes are unavailable, it will return a string,
            "Sorry we don't carry your size", and print it.
            If at least one is available, then it will return a string
            with correspoding sizes for kids, womens, and mens, and print it.
    """
    # If the user's size does not fit to any of the size charts,
    # inform the user that there are no matching sizes.
    if kids == womens == mens == "not available":
        not_available_statement = "Sorry, we don't carry your size"
        print(not_available_statement)
        return not_available_statement
    # Otherwise, message the user with corresponding kid's size, women's size,
    # and men's size.
    else:
        size_statement = "Your size choices: \nKids size: " + kids + \
                         "\nWomens size: " + womens + "\nMens size: " + mens
        print(size_statement)
        return size_statement


if __name__ == "__main__":
    main()

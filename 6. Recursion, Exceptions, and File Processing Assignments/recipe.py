"""

Jin Young Park
CS5001 Fall 2021
HW06 recipe.py
The program prompts the user either to save or to read a recipe.
If the user chooses to save, the program prompts the user
to put information on recipe and save as a file.
If the user chooses to read, the program prompts the user
to put the recipe name to open the file.

"""


def remove_whitespaces(list):
    '''
        Function -- remove_whitespace
            Removes leading and trailing whitespaces. If an element in
            a list is an empty string, it ignores it.
        Parameters:
            list -- list of recipe ingredients provided by the user
        Returns:
            Returns a list of ingredients after leading and
            trailing whitespaces of each element is removed.
    '''
    new_list = []
    for i in list:
        i = i.strip()
        if i != "":
            new_list.append(i)
    return new_list


def name_validate(string):
    '''
        Function -- name_validate
            Converts the recipe name to lowercase,
            removes any leading or trailing whitespace,
            Converts any other white space to underscores,
            removes any remaining non-alphanumeric characters
        Parameters:
            string -- a recipe name provided by the user
        Returns:
            Returns a validated recipe name which can be used
            for a filename.
    '''
    new_string = ""
    for i in range(len(string)):
        if string[i].isalpha() or string[i].isdigit() or string[i] == " ":
            new_string += string[i].lower()
    new_string = new_string.strip().replace(" ", "_")
    return new_string


def main():
    VALID_INPUT = (1, 2, 3)
    INVALID_MESSAGE = "Invalid choice."
    prompt = 0
    prompt_is_int = False
    while prompt != 3:
        while prompt_is_int is False:
            try:
                prompt = int(input("MENU: 1 - Save a new recipe, "
                                   "2 - Read a recipe, 3 - Quit "))
                if prompt in VALID_INPUT:
                    prompt_is_int = True
                else:
                    print(INVALID_MESSAGE)
            except ValueError:
                print(INVALID_MESSAGE)

        # if the user chooses to save a new recipe
        if prompt == 1:
            enough_ingredients = False
            # prompts the user to input ingredients for the recipe
            while enough_ingredients is False:
                ingredient = input("Enter the ingredients on one line. "
                                   "Separate each ingredient with a comma. ")
                splited_ingredient = ingredient.split(", ")
                validated_ingredient = remove_whitespaces(splited_ingredient)
                if len(validated_ingredient) > 0:
                    enough_ingredients = True
                else:
                    print("Recipe must have at least one ingredient.")

            # prompts the user to input direction for the recipe
            recipe_direction = \
                input("Enter the directions (1 paragraph only): ")

            # prompts the user to input time to cook
            time_is_int = False
            while time_is_int is False:
                try:
                    recipe_time = \
                        int(input("Enter the time needed in minutes: "))
                    if recipe_time > 0:
                        time_is_int = True
                except ValueError or recipe_time < 1:
                    print("Invalid time."
                          " Must be an integer greater than or equal to 0.")

            # prompts the user to input name for the recipe
            recipe_name = input("Enter the name of the recipe: ")

            # check if the filename is usable
            filename = name_validate(recipe_name)
            writing_file_path = filename + ".txt"
            while writing_file_path == ".txt":
                print("Unable to create the filename.")
                other_name = input("Enter a string containing only letters,"
                                   " numbers, and spaces. ")
                filename = name_validate(other_name)
                writing_file_path = filename + ".txt"

            # write the information in the file
            file = open(writing_file_path, "w")
            file.writelines([recipe_name + "\n\n", "Ingredients:\n"])
            for item in validated_ingredient:
                file.write(item + "\n")
            file.writelines(["\n", "Time: " + str(recipe_time) +
                             " minutes\n\n", "Directions: \n",
                             recipe_direction])
            file.close()
            print(recipe_name + " recipe saved to " + writing_file_path)
            prompt = 0
            prompt_is_int = False

        # if the user chooses to read a recipe
        elif prompt == 2:
            try:
                want_to_read = input("Enter the name of the recipe: ")
                read_file = name_validate(want_to_read)
                reading_file_path = read_file + ".txt"
                file = open(reading_file_path, "r")
                print(file.read())
                file.close()
            except FileNotFoundError:
                print("Unable to print " + reading_file_path)
            prompt = 0
            prompt_is_int = False

    exit()


if __name__ == "__main__":
    main()

"""

Jin Young Park
CS5001 Fall 2021
HW04 hangman.py
The program runs a hangman game with given secret words. The user has
6 attempts avaliable per a round, and they win if they guess the right
word or guess all the characters in the sercret word.

Contains ten functions: convert_letter_to_underscore, check_if_word,
                    check_word_with_answer, check_if_already_guessed,
                    store_letter, guesses_so_far, check_game_over,
                    secret_word_to_list, check_if_got_all_letters,
                    check_if_win

"""


def convert_letter_to_underscore(guess_stored, secret_word):
    """
        Function -- convert_letter_to_underscore
            Converts each letter of the secret word into underscore character.
        Parameters:
            guess_stored -- A list that stores all the guesses in letter.
            secret_word -- String value. The secret word for this hangman game.
        Returns:
            If the user did not make any guess yet, it will convert all letters
            into underscore character and return it. If the user has made
            guesses, it will compare the letter in the guess_storage and
            the letters of the secret_word and convert the letters
            which are not in the storage into underscore character and
            return it.
    """
    index = 0
    output = ""
    if len(guess_stored) == 0:
        return "_" * len(secret_word)
    else:
        while index < len(secret_word):
            output = secret_word[index]
            if output not in guess_stored:
                secret_word = secret_word.replace(output, "_")
            index += 1
        return secret_word


def check_if_word(word):
    """
        Function -- check_letter_or_word
            Checks if the guess that the user made is a letter or a word.
        Parameters:
            word -- String value. The guess input that the user made.
        Returns:
            Returns "word" if the length of the word is higher than 1,
            returns "letter" if the length of the word otherwise.
    """
    if len(word) > 1:
        return True
    return False


def check_word_with_answer(word, secret_word):
    """
        Function -- check_word_with_answer
            Checks if the guess that the user made matches the secret word.
        Parameters:
            word -- String value. The guess input that the user made.
            secret_word -- String value. The secret word for this hangman game.
        Returns:
            If the user's guess matches the secret word, then return True.
            Returns False if not.
    """
    if word == secret_word:
        return True
    else:
        return False


def check_if_already_guessed(letter, guess_stored):
    """
        Function -- check_if_already_guessed
            Checks if the guess that the user made is same as the one
            that they made earlier.
        Parameters:
            letter -- String value. The guess input that the user made.
            guess_stored -- A list that stores all the guesses in letter.
        Returns:
            If the guess is made earlier, then return True.
            Returns False if not.
    """
    if letter in guess_stored:
        return True
    else:
        return False


def store_letter(letter, guess_stored):
    """
        Function -- store_letter
            Stores a guess made into guess storage if the guess is a letter.
        Parameters:
            letter -- String value. The guess input that the user made.
            guess_stored -- A list that stores all the guesses in letter
        Returns:
            Adds the guess input into the list where all the guesses in letter
            are stored.
    """
    guess_stored += letter
    return guess_stored


def guesses_so_far(guess_stored):
    """
        Function -- guesses_so_far
            Informs the user the guesses that they made so far.
        Parameters:
            guess_stored -- A list that stores all the guesses in letter.
        Returns:
            Adds the guess input into the list where all the guesses in letter
            are stored.
    """
    # turn a list into a string
    guesses_in_string = "".join(guess_stored)
    statement = "Your guesses so far: " + guesses_in_string
    return statement


def check_game_over(is_correct_word, got_all_letters, attempt):
    """
        Function -- check_game_over
            Checks if the game is over by meetings one of winning or
            losing conditions.
        Parameters:
            is_correct_word -- Boolean value returned by check_word_with_answer
                               function. True if the guessed word matches the
                               secret word, False if not.
            got_all_letters -- Boolean value returned by
                               check_if_got_all_letters function. True if
                               the user guessed all the letters in the secret
                               word, False if not.
            attempt -- Int value of remaining attempts.
        Returns:
            Adds the guess input into the list where all the guesses in letter
            are stored.
    """
    if is_correct_word is True:
        return True
    elif got_all_letters is True:
        return True
    elif attempt == 0:
        return True
    else:
        return False


def secret_word_to_list(secret_word):
    """
        Function -- secret_word_to_list
            Turns characters of the secret word into a list and does not
            include characters that overlaps.
        Parameters:
            secret_word -- String value. The secret word for this hangman game.
        Returns:
            Returns a list of characters in the word without having overlapped
            character.
    """
    secret_word_in_list = []
    while len(secret_word) > 0:
        if len(secret_word) == 1:
            secret_word_in_list += secret_word
        elif secret_word[0] not in secret_word_in_list:
            secret_word_in_list += secret_word[0]
        secret_word = secret_word[1:]
    return secret_word_in_list


def check_if_got_all_letters(guess_stored, answer):
    """
        Function -- check_if_got_all_letters
            Checks if the user guessed all the characters in the secret word.
        Parameters:
            guess_storage -- A list that stores all the guesses in letter.
            answer -- A list that stores all characters in the secret word.
                      No overlapped characters.
        Returns:
            After comparing if the list that guessed words are stored has all
            the characters in the list that all characters of the secret word
            are stored.
    """
    check = all(item in guess_stored for item in answer)
    return check


def check_if_win(is_correct_word, got_all_letters):
    """
        Function -- check_if_win
            Checks if the user satisfied the winning conditions.
        Parameters:
            is_correct_word -- Boolean value returned by check_word_with_answer
                               function. True if the guessed word matches the
                               secret word, False if not.
            got_all_letters -- Boolean value returned by
                               check_if_got_all_letters function. True if
                               the user guessed all the letters in the secret
                               word, False if not.
        Returns:
            After checking if the user guessed the word that matches with the
            secret word or if the user guessed all the letters in the secret
            word, returns True if satisfies one of these conditions. Returns
            False otherwise.
    """
    if is_correct_word is True or got_all_letters is True:
        return True
    else:
        return False


def main():
    SECRET_WORDS = ["APPLE", "OBVIOUS", "XYLOPHONE"]
    count_game_won = 0
    round = 0

    # GAME STARTS
    while round < len(SECRET_WORDS):
        # variable for checking if the user guessed all letters in the secret
        # word. Default is False. Turns to True if the user does so.
        got_all_letters = False
        # variable for checking if the user guessed the word matches the
        # secret word. Default is False. Turns to True if the user does so.
        is_right_word = False
        # a list that stores all the guesses in letter the user makes
        guessed_stored = []
        # attempts to guess in each round is 6
        remaining_attempts = 6

        # Choose the first word in the list as the word for this game
        secret_word = SECRET_WORDS[round]
        # make a list of each letter of each secret word
        letters_of_the_word = secret_word_to_list(secret_word)

        # default state of win is FALSE and round counts as each round goes
        win = False
        round += 1
        # game goes until the user wins or loses
        while (not win) and (remaining_attempts > 0):
            # converting letters of the secret word that are not guessed yet
            # into underscore
            underscored_word = convert_letter_to_underscore(guessed_stored,
                                                            secret_word)
            print(underscored_word)
            # prompts the user to guess a letter or a word
            get_guess = input("Enter a letter or word: ").upper()
            # each time the user makes a guess, avaliable attempts decrease
            remaining_attempts -= 1

            # check if the guess is a letter or a word
            is_word = check_if_word(get_guess)
            # if the guess is a word
            if is_word:
                # check if the guessed word matches with the secret word
                is_right_word = check_word_with_answer(get_guess, secret_word)
                # if the guess is a word, it does not count as an attempt
                remaining_attempts += 1
            else:
                # if the guess is a letter,
                # check if it was guessed in previous attempt
                already_guessed = check_if_already_guessed(get_guess,
                                                           guessed_stored)
                # if it was guessed in previous attempt,
                # print a statement and it does not count as an attempt
                if already_guessed:
                    print("You've already guessed that letter!")
                    remaining_attempts += 1
                # if it is a new guess, then store the guess in the
                # list where it stores all the guesses in letter
                else:
                    store_letter(get_guess, guessed_stored)
                    # checks if the user guessed all the characters
                    # in the secret word
                    got_all_letters = \
                        check_if_got_all_letters(guessed_stored,
                                                 letters_of_the_word)
            # checks if the game is over
            is_game_over = check_game_over(is_right_word, got_all_letters,
                                           remaining_attempts)
            # if the game is over, checks if the user won
            if is_game_over:
                win = check_if_win(is_right_word, got_all_letters)
                # if the user wins, print the statement and
                # increase the game won count
                if win:
                    print("You win!")
                    count_game_won += 1
                # if the user loses, print the statement
                else:
                    print("You lose! The word was " + secret_word)
            # if the game is not over, print what guesses the user
            # made so far
            else:
                guesses_made = guesses_so_far(guessed_stored)
                print(guesses_made)

    # After the user played all the rounds, print their score.
    print("You won", count_game_won, "out of", round)


if __name__ == "__main__":
    main()

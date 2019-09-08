import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    for letter in secret_word:
        if letter not in letters_guessed:
            return False

    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    # https://stackoverflow.com/a/50016017
    guessed_word = []
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word.append(letter)
        else:
            guessed_word.append("_")

    word = "".join(guessed_word)
    return word


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word
    if guess in secret_word:
        return True
    else:
        return False

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    letters_guessed = []
    guesses_left = 7
    game_over = False



    #TODO: show the player information about the game according to the project spec

    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    while not game_over and guesses_left != 0:
        print(secret_word)
        guess = user_input("Enter a letter: ")
        guess_in_word = is_guess_in_word(guess, secret_word)

        if len(guess) != 1:
            print("Error: More than one letter was detected")
            continue

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback
        if guess_in_word and guess not in letters_guessed:
            print("Your letter is in the word")
            letters_guessed.append(guess)
            print(letters_guessed)
        elif guess in letters_guessed:
            print("You already guessed that letter")
            print(f" Attempts left: {guesses_left} ")
            continue
        else:
            print("Your letter was not found in the word")
            guesses_left -= 1

        print(f" Attempts left: {guesses_left} ")
    #TODO: show the guessed word so far
        print(get_guessed_word(secret_word, letters_guessed))

    #TODO: check if the game has been won or lost
        word_is_guessed = is_word_guessed(secret_word, letters_guessed)

        if word_is_guessed:
            print("You guessed the word. You win!")
            play_again = user_input("Would you like to play again? [y/n]: ")
            if play_again.lower() == 'y':
                secret_word = load_word()
                letters_guessed = []
                guesses_left = 7
                continue
            else:
                game_over = True
        elif guesses_left == 0:
            print("You have run out of attempts, you lose!")
            print(f"The word was {secret_word}")
            play_again = user_input("Would you like to play again? [y/n]: ")
            if play_again.lower() == 'y':
                secret_word = load_word()
                letters_guessed = []
                guesses_left = 7
                continue
            else:
                game_over = True



#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)

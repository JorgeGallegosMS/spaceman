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
    # Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
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

    # Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
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
    # check if the letter guess is in the secret word
    if guess in secret_word:
        return True
    else:
        return False

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def reset():
    secret_word = load_word()
    letters_guessed = []
    guesses_left = len(secret_word)
    num_letters = f"\nThe word I'm thinking of has {len(secret_word)} letters in it\n"
    print(num_letters)

    return secret_word,letters_guessed,guesses_left

def play_again():
    play_again = user_input("Would you like to play again? [y/n]: ").lower()
    while play_again != 'y' and play_again != 'n':
        print("\nYou need to use 'y' or 'n'\n")
        play_again = user_input("Would you like to play again? [y/n]: ").lower()
    return play_again

def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    letters_guessed = []
    guesses_left = len(secret_word)
    game_over = False
    num_letters = f"\nThe word I'm thinking of has {len(secret_word)} letters in it\n"



    # show the player information about the game according to the project spec
    print("\nWelcome to Spaceman, a word guessing game.\n")
    print("You must guess one letter at a time.\n")
    print(f"You have {guesses_left} attempts to figure out the word, good luck!\n")
    print(num_letters)
    # Ask the player to guess one letter per round and check that it is only one letter
    while not game_over and guesses_left != 0:
        attempts_left = f"Attempts left: {guesses_left}\n"
        print(attempts_left)
        letters = ", ".join(letters_guessed)
        guessed = f"Letters guessed: {letters}\n"

        print(guessed)

        guess = user_input("Enter a letter: ")
        guess_in_word = is_guess_in_word(guess, secret_word)

        print(guessed)

        if len(guess) != 1:
            print("Please use only 1 letter")
            print(guessed)
            continue

        print("========================================")
    # Check if the guessed letter is in the secret or not and give the player feedback
        if (guess_in_word and guess.isalpha()) and guess not in letters_guessed:
            print("Your letter is in the word")
            letters_guessed.append(guess)
        elif guess in letters_guessed:
            print("You already guessed that letter. Try again!")
            print(get_guessed_word(secret_word, letters_guessed))
            print("========================================")
            continue
        elif not guess_in_word and guess.isalpha():
            print("Your letter was not found in the word")
            guesses_left -= 1
            letters_guessed.append(guess)
        else:
            print("Your guess must be a letter")
            print("========================================")
            continue
    # show the guessed word so far
        print(get_guessed_word(secret_word, letters_guessed))
        print("========================================")

    # check if the game has been won or lost
        word_is_guessed = is_word_guessed(secret_word, letters_guessed)

        if word_is_guessed:
            print(f"You guessed it! The word was {secret_word}. You win!\n")
            again = play_again()
            if play_again == 'y':
                secret_word,letters_guessed, guesses_left = reset()
                continue
            else:
                game_over = True

        elif guesses_left == 0:
            print("You have run out of attempts, you lose!\n")
            print(f"The word was {secret_word}")
            again = play_again()
            if again == 'y':
                secret_word,letters_guessed, guesses_left = reset()
                continue
            else:
                game_over = True



#These function calls that will start the game
if __name__ == '__main__':
    secret_word = load_word()
    spaceman(secret_word)


# All the code is readable and seamless to follow. Only one issue I can think of is making sure your code follows DRY principles.
# 'Don't Repeat Yourself'. If you look at lines (140-145) and lines (152-157) they are identical can hence don't need to be repeated
# You might want to create a function for that.

"""
File: hangman.py
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    """
    This program is for a game which lasts a very long time- Hangman!!!
    At first, users see the dashed words and know how many alphabets they have to guess.
    Users have N_TURNS to be able to win this game.
    Also, users were expected only to type in one alphabet per round.
    """
    string = random_word()
    # gives a random word
    hid_word = '-' * len(string)
    print('The word looks like: ' + hid_word)
    print('You have ' + str(N_TURNS) + ' guesses left.')
    guess(N_TURNS, string, hid_word)
    # start guessing by giving alphabets


def guess(N_TURNS, string, hid_word):
    """
    At first, it will check whether users type in only one character.
    Then, it will check if the letter is in string.
    """
    while True:
        new_word = ''
        # for every round's string manipulation
        guess = input('Your guess: ')
        # alphabet
        while guess.isalpha() is False or len(guess) > 1:
            # to avoid any kinds of strange format other than a single alphabet
            print('illegal format.')
            guess = input('Your guess: ')
        guess = guess.upper()
        if guess not in string:
            N_TURNS -= 1
            print('There is no ' + str(guess) + '\'s in the word.')
            if N_TURNS == 0:
                print('You are completely hung : (')
                print('The word was: '+str(string))
                break
            print('The word looks like: ' + hid_word)
            print('You have ' + str(N_TURNS) + ' guesses left.')
        else:
            print('You are correct!')
            for i in range(len(string)):
                # take out the correct alphabet one by one from hid_word
                if guess == string[i]:
                    new_word += guess
                else:
                    new_word += hid_word[i]
            hid_word = new_word
            # put the new word to hid_word then new_word can do the new string manipulation
            if new_word == string:
                print('You Win!!')
                print('The word was: '+new_word)
                break
            print('The word looks like: ' + new_word)
            print('You have ' + str(N_TURNS) + ' guesses left.')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()

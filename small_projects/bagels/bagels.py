import random


def main():
    print('Bagels, a deductive logic game.')

    num_digits = get_num_digits()
    max_guesses = get_max_guesses()

    print('''

I am thinking of a {}-digit number. 
Try to guess what it is. Here are some clues:
When I say: \tThat means:
Pico \t\tOne digit is correct but in the wrong position.
Fermi \tOne digit is correct and in the right position.
Bagels \tNo digit is correct.'''.format(num_digits))

    while True:  # Main game loop.
        # Stores the secret number player needs to guess.
        secret_num = get_secret_num(num_digits)
        print('I have thought up a number.')
        print('You have {} guesses to get it.'.format(max_guesses))

        num_guesses = 1
        while num_guesses <= max_guesses:
            guess = ''
            # Keep looping until they enter a valid guess:
            while len(guess) != num_digits or not guess.isdecimal():
                print('Guess #{}'.format(num_guesses))
                guess = input('> ')

            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break  # They're correct so break out of this loop.

            if num_guesses > max_guesses:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secret_num))

        # Ask the player if they want to play again.
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break

    print('Thanks for playing!')


def get_num_digits():
    """Ask the player the num_digits and returns it."""
    num_digits = int(input('How many digits would you like to guess? '
                           '(default is 3) \n> '))
    return num_digits


def get_max_guesses():
    """Ask the player the max_guesses and returns it."""
    max_guesses = int(input('How many guess attempt would you like? '
                            '(default is 10)\n> '))
    return max_guesses


def get_secret_num(num_digits):
    """Returns a string made up of num_digits unique random digits."""
    numbers = list('0123456789')  # Make a list of digits 0 to 9.
    random.shuffle(numbers)  # Shuffle the order randomly.

    # Get the first num_digits digits in the list for the secret numbers:
    secret_num = ''
    for i in range(num_digits):
        secret_num += str(numbers[i])
    return secret_num


def get_clues(guess, secret_num):
    """Returns a string with pico, fermi, bagels clues for a guess and secret
    number pair."""
    if guess == secret_num:
        return 'You win!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            # A correct digit is in the correct place.
            clues.append('Fermi')
        elif guess[i] in secret_num:
            # A correct digit is in the wrong place.
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels'  # There are no correct digits.
    else:
        # Sort the clues into alphabetical order so their original order
        # doesn't give information away.
        clues.sort()
        # Make a single string from the list of string clues.
        return ' '.join(clues)


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()

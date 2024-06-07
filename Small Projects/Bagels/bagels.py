from random import randint


# TODO fix duplicate number case

print("Bagels, a deductive logic game.")

print("I am thinking of a 3-digit number. Try to guess what it is.")
print("Here are some clues:")
print("When I say: \tThat means:")
print("  Pico \t\tOne digit is correct but in the wrong position.")
print("  Fermi \tOne digit is correct and in the right position.")
print("  Bagels \tNo digit is correct.")
print("I have thought up a number.")
print("You have 10 guesses to get it.", end="")


def get_random_number():
    """Get a random number from 1 to 999 and convert it into string."""
    random_num = randint(1, 999)

    """Add 0 in front if the number is less than 100 and 00 if less than 10"""
    if random_num < 10:
        random_num = str(random_num)
        random_num = '00' + random_num

    elif random_num < 100:
        random_num = str(random_num)
        random_num = '0' + random_num

    else:
        random_num = str(random_num)

    return random_num


def str_compare(num):
    score = []

    # Fermi = 1, Pico = 2, Bagels = 0

    if num[0] == num_list[0]:
        score.append('1')
    elif num[0] != num_list[0] and num[0] in num_list:
        score.append('2')
    elif num[0] not in num_list:
        score.append('0')

    if num[1] == num_list[1]:
        score.append('1')
    elif num[1] != num_list[1] and num[1] in num_list:
        score.append('2')
    elif num[0] not in num_list:
        score.append('0')

    if num[2] == num_list[2]:
        score.append('1')
    elif num[2] != num_list[2] and num[2] in num_list:
        score.append('2')
    elif num[0] not in num_list:
        score.append('0')

    return score


def game_logic(score):
    state = ""

    if score == ['0', '0', '0']:
        return state == 'bagels'
    elif score == ['1', '1', '1']:
        return state == 'win'
    else:
        for num in score:
            if num == '1':
                print("Fermi", end=" ")
            elif num == "2":
                print('Pico', end=" ")


count = 1
num_list = []
random_num = get_random_number()
for i in range(3):
    num_list.append(random_num[i])

while True:
    print(f"\nGuess #{count}:")
    num = input("> ")
    count += 1
    score = []
    state = ""

    print(random_num)
    score = str_compare(num)
    # print(score)
    state = game_logic(score)

    if state == 'win':
        play_again = input("Do you want to play again? (yes or no)")
        if play_again == 'yes':
            count = 1
            random_num = get_random_number()
            for i in range(3):
                num_list.append(random_num[i])
            continue
        else:
            break

    # if score == ['0', '0', '0']:
    #     print("Bagels", end="")
    # elif score == ['1', '1', '1']:
    #     print("You win!")
    #     play_again = input("Do you want to play again? (yes or no)")
    #     if play_again == 'yes':
    #         continue
    #     else:
    #         break

    # else:
    #     for num in score:
    #         if num == '1':
    #             print("Fermi", end=" ")
    #         elif num == "2":
    #             print('Pico', end=" ")

"""
How many M&Ms are in a jar?
"""

import random


def main():
    show_header()
    guess_attempt()


def show_header():
    print('-----------------------')
    print("  Guess How Many M&M's     ")
    print('-----------------------')
    print("Guess the number of M&M's and you get a free lunch.")
    print()

    attempt_limit, attempts, mm_count = guess_attempt()

    guess_the_correct_number(attempts, mm_count, attempt_limit)


def guess_the_correct_number(attempts, mm_count, attempt_limit):
    while attempts < attempt_limit:  # Boolean- True of False. while True
        guess_text = input("How many M&M's are in the jar? ")  # code runs as long as the statement is true
        guess = int(guess_text)
        attempts += 1  # counting up the remaining guesses

        if guess == mm_count:
            print(f"You have free lunch! It was {guess} in the jar")
            break
        elif guess < mm_count:
            print("Sorry too LOW")
        else:
            print("Your guess is too HIGH!")


def guess_attempt():
    mm_count = random.randint(1, 100)  # number of m&m's
    attempt_limit = 7  # given 7 attempts
    attempts = 0
    return attempt_limit, attempts, mm_count


if __name__ == '__main__':
    main()

# Choose a Number Game#
"""
guess = None

while guess != 0:
    user_pick_number = int(input("Please choose a number. "))
    if user_pick_number == 0:
        print("Goodbye")
        break
    if (user_pick_number % 2 ) == 0:
        print("Even")
    elif (user_pick_number % 1) == 0:
        print('Odd')

"""

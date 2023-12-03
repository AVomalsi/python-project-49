#!/usr/bin/env python3
from brain_games.cli import welcome_user
import random
import prompt


def is_even(num):
    return num % 2 == 0


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(3):
        number = random.randint(1, 100)
        print(f'Question: {number}')

        ans = prompt.string('Your answer: ')
        correct_ans = 'yes' if is_even(number) else 'no'

        if ans == correct_ans:
            print('Correct!')
        else:
            print(
                f"'{ans}' is wrong answer ;(. "
                f"Correct answer was '{correct_ans}'."
            )
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()

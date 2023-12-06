#!/usr/bin/env python3
from brain_games.cli import welcome_user
import random
import prompt
import operator


def calculate(variable_a, variable_b, operation):
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    return operations[operation](variable_a, variable_b)


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('What is the result of the expression?')

    for _ in range(3):
        number_a = random.randint(1, 100)
        number_b = random.randint(1, 100)
        list_operator = ['+', '-', '*']
        operator = random.choice(list_operator)
        print(f'Question: {number_a} {operator} {number_b}')

        user_answer = prompt.integer('Your answer: ')
        correct_answer = calculate(number_a, number_b, operator)

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()

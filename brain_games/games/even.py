import random


INITIAL_VALUE = 1
FINAL_VALUE = 100


def is_even(num):
    return num % 2 == 0


def show_game_name():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def get_result_program():
    number = random.randint(INITIAL_VALUE, FINAL_VALUE)
    result = 'yes' if is_even(number) else 'no'
    return number, result

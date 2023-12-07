import random


INITIAL_VALUE = 1
FINAL_VALUE = 100


def calculate_gcd(variable_a, variable_b):
    while variable_b > 0:
        variable_c = variable_a % variable_b
        variable_a = variable_b
        variable_b = variable_c
    return variable_a


def show_game_name():
    return 'Find the greatest common divisor of given numbers.'


def get_result_program():
    first_number = random.randint(INITIAL_VALUE, FINAL_VALUE)
    second_number = random.randint(INITIAL_VALUE, FINAL_VALUE)
    random_numbers = f'{first_number} {second_number}'
    result = str(calculate_gcd(first_number, second_number))
    return random_numbers, result

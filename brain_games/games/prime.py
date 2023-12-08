import random


INITIAL_VALUE = 2
FINAL_VALUE = 100


def is_prime(number):
    for i in range(INITIAL_VALUE, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def show_game_name():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_result_program():
    random_number = random.randint(INITIAL_VALUE, FINAL_VALUE)
    result = 'yes' if is_prime(random_number) else 'no'
    return random_number, result

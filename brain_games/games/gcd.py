import random


INITIAL_VALUE = 1
FINAL_VALUE = 100
GAME_RULES = 'Find the greatest common divisor of given numbers.'


def calculate_gcd(variable_a: int, variable_b: int) -> int:
    while variable_b > 0:
        variable_c = variable_a % variable_b
        variable_a = variable_b
        variable_b = variable_c
    return variable_a


def get_question_and_answer() -> tuple[str, str]:
    first_number = random.randint(INITIAL_VALUE, FINAL_VALUE)
    second_number = random.randint(INITIAL_VALUE, FINAL_VALUE)
    question = f'{first_number} {second_number}'
    answer = str(calculate_gcd(first_number, second_number))
    return question, answer

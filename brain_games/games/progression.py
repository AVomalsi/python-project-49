import random


INITIAL_VALUE = 1
FINAL_VALUE = 50
STEP_TO_TEN = 10


def show_game_name():
    return 'What number is missing in the progression?'


def generate_sequence():
    start_number = random.randint(INITIAL_VALUE, FINAL_VALUE)
    step = random.randint(INITIAL_VALUE, STEP_TO_TEN)
    end_number = start_number + step * 9
    progression_list = [
        str(i) for i in range(start_number, end_number + 1, step)
    ]
    return progression_list


def get_result_program():
    arithmetic_sequence = generate_sequence()
    random_index = random.randint(0, 9)
    random_value = arithmetic_sequence[random_index]
    arithmetic_sequence[random_index] = '..'
    final_sequence = ' '.join(arithmetic_sequence)
    return final_sequence, random_value

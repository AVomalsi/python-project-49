import random


INITIAL_VALUE = 1
FINAL_VALUE = 50
SEQUENCE_LENGTH = 10
START_OF_INDEX = 0
END_OF_INDEX = 9
GAG_SYMBOL = '..'


def show_game_name():
    return 'What number is missing in the progression?'


def generate_sequence():
    start_number = random.randint(INITIAL_VALUE, FINAL_VALUE)
    step = random.randint(INITIAL_VALUE, SEQUENCE_LENGTH)
    end_number = END_OF_INDEX * step + start_number
    progression_list = [
        str(i) for i in range(start_number, end_number + 1, step)
    ]
    return progression_list


def get_result_program():
    arithmetic_sequence = generate_sequence()
    random_index = random.randint(START_OF_INDEX, END_OF_INDEX)
    random_value = arithmetic_sequence[random_index]
    arithmetic_sequence[random_index] = GAG_SYMBOL
    final_sequence = ' '.join(arithmetic_sequence)
    return final_sequence, random_value

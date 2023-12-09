import random


INITIAL_VALUE = 1
FINAL_VALUE = 50
SEQUENCE_LENGTH = 10
START_OF_INDEX = 0
END_OF_INDEX = 9
GAG_SYMBOL = '..'
GAME_RULES = 'What number is missing in the progression?'


def generate_sequence() -> list:
    start_number = random.randint(INITIAL_VALUE, FINAL_VALUE)
    step = random.randint(INITIAL_VALUE, SEQUENCE_LENGTH)
    end_number = END_OF_INDEX * step + start_number
    progression_list = [
        str(i) for i in range(start_number, end_number + 1, step)
    ]
    return progression_list


def get_question_and_answer() -> tuple[str, str]:
    arithmetic_sequence = generate_sequence()
    random_index = random.randint(START_OF_INDEX, END_OF_INDEX)
    answer = arithmetic_sequence[random_index]
    arithmetic_sequence[random_index] = GAG_SYMBOL
    question = ' '.join(arithmetic_sequence)
    return question, answer

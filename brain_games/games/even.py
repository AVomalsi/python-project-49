import random


INITIAL_VALUE = 1
FINAL_VALUE = 100
GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num: int) -> bool:
    return num % 2 == 0


def get_question_and_answer() -> tuple[str, str]:
    question = random.randint(INITIAL_VALUE, FINAL_VALUE)
    answer = 'yes' if is_even(question) else 'no'
    return question, answer

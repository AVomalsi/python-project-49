import random


INITIAL_VALUE = 2
FINAL_VALUE = 100
GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number: int) -> bool:
    for i in range(INITIAL_VALUE, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def get_question_and_answer() -> tuple[str, str]:
    question = random.randint(INITIAL_VALUE, FINAL_VALUE)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer

import random
import operator


INITIAL_VALUE = 1
FINAL_VALUE = 100
TUPLE_OF_OPERATIONS = ('+', '-', '*')
GAME_RULES = 'What is the result of the expression?'
OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}


def get_question_and_answer() -> tuple[str, str]:
    first_number = random.randint(INITIAL_VALUE, FINAL_VALUE)
    second_number = random.randint(INITIAL_VALUE, FINAL_VALUE)
    operator = random.choice(TUPLE_OF_OPERATIONS)
    question = f'{first_number} {operator} {second_number}'
    answer = str(OPERATIONS[operator](first_number, second_number))
    return question, answer

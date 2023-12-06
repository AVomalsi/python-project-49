import random
import operator


INITIAL_VALUE = 1
FINAL_VALUE = 100
LIST_OF_OPERATIONS = ['+', '-', '*']


def calculate(variable_a, variable_b, operation):
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    return operations[operation](variable_a, variable_b)


def show_game_name():
    return 'What is the result of the expression?'


def get_result_program():
    first_number = random.randint(INITIAL_VALUE, FINAL_VALUE)
    second_number = random.randint(INITIAL_VALUE, FINAL_VALUE)
    operator = random.choice(LIST_OF_OPERATIONS)
    expression = f'{first_number} {operator} {second_number}'
    result = str(calculate(first_number, second_number, operator))
    return expression, result

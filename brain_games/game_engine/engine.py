import prompt


NUMBER_OF_ATTEMPTS = 3


def game_template(some_game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(some_game.show_game_name())
    for _ in range(NUMBER_OF_ATTEMPTS):
        value_question, correct_answer = some_game.get_result_program()
        print(f'Question: {value_question}')

        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')

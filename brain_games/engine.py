from brain_games.cli import welcome_user
import prompt


GAME_MESSAGE = 'Welcome to the Brain Games!'
NUMBER_OF_ATTEMPTS = 3


def run_game(game):
    print(GAME_MESSAGE)
    name = welcome_user()
    print(game.GAME_RULES)
    for _ in range(NUMBER_OF_ATTEMPTS):
        content_of_question, correct_answer = game.get_question_and_answer()
        print(f'Question: {content_of_question}')

        user_answer = prompt.string('Your answer: ').lower()

        if user_answer != correct_answer:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f'Congratulations, {name}!')

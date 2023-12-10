#!/usr/bin/env python3
from brain_games import engine
from brain_games.games import calc


def main():
    engine.run_game(calc.GAME_RULES, calc.get_question_and_answer)


if __name__ == '__main__':
    main()

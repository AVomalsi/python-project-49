#!/usr/bin/env python3
from brain_games import engine
from brain_games.games import even


def main():
    engine.run_game(even.GAME_RULES, even.get_question_and_answer)


if __name__ == '__main__':
    main()

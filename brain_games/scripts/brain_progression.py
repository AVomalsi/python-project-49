#!/usr/bin/env python3
from brain_games import engine
from brain_games.games import progression


def main():
    engine.run_game(progression.GAME_RULES, progression.get_question_and_answer)


if __name__ == '__main__':
    main()

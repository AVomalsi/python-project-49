#!/usr/bin/env python3
from brain_games import engine
from brain_games.games import gcd


def main():
    engine.run_game(gcd.GAME_RULES, gcd.get_question_and_answer)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
from brain_games import engine
from brain_games.games import prime


def main():
    engine.run_game(prime.GAME_RULES, prime.get_question_and_answer)


if __name__ == '__main__':
    main()

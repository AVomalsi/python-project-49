#!/usr/bin/env python3
from brain_games.game_engine import engine
from brain_games.games import gcd


def main():
    engine.game_template(gcd)


if __name__ == '__main__':
    main()

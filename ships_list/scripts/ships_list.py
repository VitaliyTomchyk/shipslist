#!/usr/bin/env python3
from ships_list.ships_list.ships_list import ships_list
from ships_list.cli.cli import parcer


def main():
    parced_result = parcer()
    ships_list(parced_result)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
from ships_list.ships_list.ships_list import ships_list
from ships_list.cli.cli import parcer


def main():
    ships_list()


if __name__ == '__main__':
    main(*parcer())

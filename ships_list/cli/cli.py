import argparse


def parcer():
    parser = argparse.ArgumentParser(description='Working with ship\'s list.')
    parser.add_argument('--ship')
    parser.add_argument('--importance')
    parser.add_argument('--add_ship')
    args = parser.parse_args()
    print(args.accumulate(args.integers))
    return []

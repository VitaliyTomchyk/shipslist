import argparse


def parcer():
    parser = argparse.ArgumentParser(description='Working with ship\'s list.')
    parser.add_argument('--ship')
    parser.add_argument('--importance')
    result = [parser.parse_args().ship,
              parser.parse_args().importance]
    return result

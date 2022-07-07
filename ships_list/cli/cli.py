import argparse


def parcer():
    parser = argparse.ArgumentParser(description='Working with ship\'s list.')
    parser.add_argument('--add_ship')
    parser.add_argument('--IMO')
    parser.add_argument('--add_task')

    ships_name = parser.parse_args().add_ship
    task = parser.parse_args().add_task
    IMO = parser.parse_args().IMO

    result = {'add_ship': bool(ships_name),
              'add_task': bool(task),
              'ships_name': ships_name,
              'IMO': IMO,
              'tasks_name': task}
    print(result)
    return result

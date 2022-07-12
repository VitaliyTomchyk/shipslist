import argparse
import json


def parcer():
    # grepping options for choise arguments
    with open('ships_list/lists/standard/supporting_info.json', 'r') as f:
        file = json.load(f)
        stages = file['stages']
        parties = file['parties']
    with open('ships_list/lists/ships.json', 'r') as f:
        file = json.load(f)
        ships = list(map(lambda x: x['name'], file))

    # creating parser
    parser = argparse.ArgumentParser(description='Working with ship\'s list.')

    parser.add_argument('-add_voyage', help='add voyage')
    parser.add_argument('-add_ship', help='enter name of ship to be added',
                        type=str)
    parser.add_argument('-remove_ship', help='removes ship from list based' +
                        ' on name of the ship', choices=ships)
    parser.add_argument('-ship', help='enter name of ship to work with',
                        choices=ships)
    parser.add_argument('-IMO', help='put IMO number',
                        type=int)
    parser.add_argument('-add_task', help='put name of task',
                        type=str)
    parser.add_argument('-task_stage', help='task stage',
                        choices=stages)
    parser.add_argument('-task_party', help='name or role task is related to',
                        choices=parties)
    parser.add_argument('-read_list', help='read list of stated ship')
    parser.add_argument('-add_list')

    # creating varuables
    added_ship = parser.parse_args().add_ship
    ships_name = parser.parse_args().ship
    task = parser.parse_args().add_task
    IMO = parser.parse_args().IMO
    task_stage = parser.parse_args().task_stage
    task_party = parser.parse_args().task_party
    ship_to_remove = parser.parse_args().remove_ship
    add_list = parser.parse_args().add_list
    read_list = parser.parse_args().read_list

    # generating resul
    result = {'remove_ship': bool(ship_to_remove),
              'add_list': add_list,
              'read_list': read_list,
              'added_ship': added_ship,
              'ship': ships_name,
              'ship_to_remove': ship_to_remove,
              'IMO': IMO,
              'tasks_name': task,
              'task_stage': task_stage,
              'task_party': task_party}
    return result

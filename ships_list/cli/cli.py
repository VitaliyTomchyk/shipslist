import argparse
import json
from ships_list.additional_functions.additional_functions import list_to_string


def parcer():
    # grepping options for choise arguments
    with open('ships_list/lists/supporting_info.json', 'r') as f:
        file = json.load(f)
        stages = file['stages']
        parties = file['parties']
    with open('ships_list/lists/ships.json', 'r') as f:
        file = json.load(f)
        ships = list_to_string(list(map(lambda x: x['name'], file)))

    # creating parser
    parser = argparse.ArgumentParser(description='Working with ship\'s list.')
    parser.add_argument('-add_ship', help='enter name of ship to be added')
    parser.add_argument('-ship', help='enter name of ship to work with',
                        choices=ships)
    parser.add_argument('-IMO', help='put IMO number')
    parser.add_argument('-add_task', help='put name of task')
    parser.add_argument('-task_stage', help='task stage:\n' +
                                            list_to_string(stages),
                        choices=stages)
    parser.add_argument('-task_party', help='name or role ' +
                                            'task is related to \n' +
                                            list_to_string(parties),
                        choices=parties)
    parser.add_argument('-remove_ship', help='removes ship from list based' +
                        ' on name of the ship', choices=ships)
    parser.add_argument('-add_list')

    # creating varuables
    added_ship = parser.parse_args().add_ship
    ships_name = parser.parse_args().ship
    task = parser.parse_args().add_task
    IMO = parser.parse_args().IMO
    task_stage = parser.parse_args().task_stage
    task_party = parser.parse_args().task_party
    ship_to_remove = parser.parse_args().remove_ship
    stage = parser.parse_args().add_list

    # generating resul
    result = {'add_ship': bool(added_ship),
              'add_task': bool(task),
              'remove_ship': bool(ship_to_remove),
              'add_list': stage,
              'added_ship': added_ship,
              'ship': ships_name,
              'ship_to_remove': ship_to_remove,
              'IMO': IMO,
              'tasks_name': task,
              'task_stage': task_stage,
              'task_party': task_party}
    return result

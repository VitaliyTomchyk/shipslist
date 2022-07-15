import argparse
import json


def parcer():
    # grepping options for choise arguments
    with open('ships_list/lists/Standard/supporting_info.json', 'r') as f:
        file = json.load(f)
        stages = file['stages']
        parties = file['parties']
        voyage_types = file['voyage_types']
    with open('ships_list/lists/ships.json', 'r') as f:
        file = json.load(f)
        ships = list(map(lambda x: x['name'], file))

    # creating parser
    parser = argparse.ArgumentParser(description='Working with ship\'s list.')

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
    parser.add_argument('-add_voyage', help='add voyage', nargs=1)
    parser.add_argument('-read_voyage', help='read details of voyage from id',
                        nargs=1)
    parser.add_argument('-remove_voyage', help='remove voyage by id',
                        nargs=1)
    parser.add_argument('-l_ports', help='load ports', nargs="*")
    parser.add_argument('-d_ports', help='discharge ports', nargs="*")
    parser.add_argument('-restr_points', help='restriction points on the way',
                        nargs="*", default=None)
    parser.add_argument('-voy_type', help='choose type of voyage',
                        choices=voyage_types)

    # creating varuables
    added_ship = parser.parse_args().add_ship
    ships_name = parser.parse_args().ship
    task = parser.parse_args().add_task
    IMO = parser.parse_args().IMO
    task_stage = parser.parse_args().task_stage
    task_party = parser.parse_args().task_party
    ship_to_remove = parser.parse_args().remove_ship
    read_list = parser.parse_args().read_list
    add_list = parser.parse_args().add_list
    add_voyage = parser.parse_args().add_voyage
    l_ports = parser.parse_args().l_ports
    d_ports = parser.parse_args().d_ports
    restr_points = parser.parse_args().restr_points
    voy_type = parser.parse_args().voy_type
    voyage_id = parser.parse_args().read_voyage
    rm_voyage_id = parser.parse_args().remove_voyage 

    # generating result
    result = {'remove_ship': bool(ship_to_remove),
              'add_list': add_list,
              'read_list': read_list,
              'added_ship': added_ship,
              'ship': ships_name,
              'ship_to_remove': ship_to_remove,
              'IMO': IMO,
              'tasks_name': task,
              'task_stage': task_stage,
              'task_party': task_party,
              'add_voyage': add_voyage,
              'l_ports': l_ports,
              'd_ports': d_ports,
              'restr_points': restr_points,
              'voy_type': voy_type,
              'read_voyage': voyage_id,
              'remove_voyage': rm_voyage_id}
    return result

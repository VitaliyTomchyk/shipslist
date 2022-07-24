import argparse


def parcer():
    # creating parser
    parser = argparse.ArgumentParser(description='Working with ship\'s list.',
                                     prog='ships_list')

    parser.add_argument('-add_ship',
                        help='function will add the ship', action='store_true')
    parser.add_argument('-remove_ship',
                        help='removes ship from list based' +
                        ' on name of the ship', action='store_true')
    parser.add_argument('-read_ship',
                        help='reads ship\'s details from list based' +
                        ' on name of the ship', action='store_true')

    parser.add_argument('-add_task', help='put name of task',
                        type=str)
    parser.add_argument('-remove_task', help='put name of task',
                        type=str)
    parser.add_argument('-redact_task', help='radact a task element',
                        action='store_true')

    parser.add_argument('-add_voyage', help='add voyage', action='store_true')
    parser.add_argument('-remove_voyage', help='remove voyage by id',
                        action='store_true')
    parser.add_argument('-read_voyage', help='read details of ' +
                        'voyage from id')

    parser.add_argument('-read_tasks_list', help='read the tasks',
                        action='store_true')

    # creating varuables
    add_ship = parser.parse_args().add_ship
    add_task = parser.parse_args().add_task
    remove_task = parser.parse_args().remove_task
    remove_ship = parser.parse_args().remove_ship
    add_voyage = parser.parse_args().add_voyage
    remove_voyage = parser.parse_args().remove_voyage
    read_tasks_list = parser.parse_args().read_tasks_list
    redact_task = parser.parse_args().redact_task
    read_ship = parser.parse_args().read_ship

    # generating result
    result = {'remove_ship': remove_ship,
              'add_ship': add_ship,
              'add_task': add_task,
              'add_voyage': add_voyage,
              'remove_voyage': remove_voyage,
              'read_tasks_list': read_tasks_list,
              'remove_task': remove_task,
              'redact_task': redact_task,
              'read_ship': read_ship
              }
    return result

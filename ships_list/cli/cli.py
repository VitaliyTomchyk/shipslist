import argparse


def parcer():
    # creating parser
    parser = argparse.ArgumentParser(description='Working with ship\'s list.',
                                     prog='ships_list')

    # adding arguments
    parser.add_argument('-add_ship',
                        help='function will add the ship', action='store_true')
    parser.add_argument('-remove_ship',
                        help='removes ship from list based' +
                        ' on name of the ship', action='store_true')
    parser.add_argument('-read_ship',
                        help='reads ship\'s details from list based' +
                        ' on name of the ship', action='store_true')

    parser.add_argument('-add_task', help='put name of task',
                        action='store_true')
    parser.add_argument('-close_task', help='put id of task to close',
                        action='store_true')
    parser.add_argument('-remove_task', help='put name of task',
                        action='store_true')
    parser.add_argument('-redact_task', help='radact a task element',
                        action='store_true')
    parser.add_argument('-amend_task', help='amend a task\' value by key',
                        action='store_true')

    parser.add_argument('-add_voyage', help='add voyage', action='store_true')
    parser.add_argument('-remove_voyage', help='remove voyage by id',
                        action='store_true')
    parser.add_argument('-read_voyage', help='read details of ' +
                        'voyage from id')

    parser.add_argument('-read_tasks_list', help='read the tasks',
                        action='store_true')
    parser.add_argument('-print_ship', help='prints details of ship',
                        action='store_true')

    parser.add_argument('-create_booking', help='create booking',
                        action='store_true')
    parser.add_argument('-read_booking', help='read booking',
                        action='store_true')
    parser.add_argument('-remove_booking', help='remove booking',
                        action='store_true')

    parser.add_argument('-freight_calculator', help='calculate_freight',
                        action='store_true')

    # generating result
    return {
        'add_ship': parser.parse_args().add_ship,
        'read_ship': parser.parse_args().read_ship,
        'remove_ship': parser.parse_args().remove_ship,

        'add_task': parser.parse_args().add_task,
        'remove_task': parser.parse_args().remove_task,
        'redact_task': parser.parse_args().redact_task,
        'amend_taks': parser.parse_args().amend_task,
        'read_tasks_list': parser.parse_args().read_tasks_list,

        'add_voyage': parser.parse_args().add_voyage,
        'remove_voyage': parser.parse_args().remove_voyage,
        "close_task": parser.parse_args().close_task,
        "print_ship": parser.parse_args().print_ship,

        "create_booking": parser.parse_args().create_booking,
        "read_booking": parser.parse_args().read_booking,
        "remove_booking": parser.parse_args().remove_booking,

        'freight_calculator': parser.parse_args().freight_calculator,
    }

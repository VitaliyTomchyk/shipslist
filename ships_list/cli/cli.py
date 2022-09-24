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

    parser.add_argument('-add_booking', help='create booking',
                        action='store_true')
    parser.add_argument('-read_booking', help='read booking',
                        action='store_true')
    parser.add_argument('-remove_booking', help='remove booking',
                        action='store_true')

    parser.add_argument('-freight_calculator', help='calculate_freight',
                        action='store_true')

    parser.add_argument('-fill_template', help='function will fill a template',
                        action='store_true')
    parser.add_argument('-create_template', help='create a template written ' +
                        'by user', action='store_true')
    parser.add_argument('-remove_template', help='remove a template',
                        action='store_true')

    parser.add_argument('-add_company', help='create a company',
                        action='store_true')
    parser.add_argument('-remove_company', help='remove a company',
                        action='store_true')
    parser.add_argument('-edit_company', help='edit a company',
                        action='store_true')

    parser.add_argument('-add_person', help='create a person',
                        action='store_true')
    parser.add_argument('-remove_person', help='remove a person',
                        action='store_true')
    parser.add_argument('-edit_person', help='edit a person',
                        action='store_true')

    # generating result
    return {
        'add_ship': parser.parse_args().add_ship,
        'read_ship': parser.parse_args().read_ship,
        'remove_ship': parser.parse_args().remove_ship,

        'add_task': parser.parse_args().add_task,
        'remove_task': parser.parse_args().remove_task,
        'amend_taks': parser.parse_args().amend_task,
        'close_task': parser.parse_args().close_task,

        'read_tasks_list': parser.parse_args().read_tasks_list,

        'add_voyage': parser.parse_args().add_voyage,
        'remove_voyage': parser.parse_args().remove_voyage,

        'print_ship': parser.parse_args().print_ship,

        'add_booking': parser.parse_args().add_booking,
        'read_booking': parser.parse_args().read_booking,
        'remove_booking': parser.parse_args().remove_booking,

        'freight_calculator': parser.parse_args().freight_calculator,

        'fill_template': parser.parse_args().fill_template,
        'create_template': parser.parse_args().create_template,
        'remove_template': parser.parse_args().remove_template,

        'add_company': parser.parse_args().add_company,
        'remove_company': parser.parse_args().remove_company,
        'edit_company': parser.parse_args().edit_company,

        'add_person': parser.parse_args().add_person,
        'remove_person': parser.parse_args().remove_person,
        'edit_person': parser.parse_args().edit_person

    }

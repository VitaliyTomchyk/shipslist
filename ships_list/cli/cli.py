import argparse


def adding_arguments(parser):
    # adding arguments
    arguments = [
        ['-add_ship', 'function will add the ship'],
        ['-remove_ship', 'removes ship from list based' +
         ' on name of the ship'],
        ['-read_ship', 'reads ship\'s details from list based' +
         ' on name of the ship'],

        ['-add_task', 'put name of task'],
        ['-close_task', 'put id of task to close'],
        ['-remove_task', 'put name of task'],
        ['-amend_task', 'amend a task\' value by key'],

        ['-add_voyage', 'add voyage'],
        ['-remove_voyage', 'remove voyage by id'],
        ['-read_voyage', 'read details of voyage from id'],

        ['-read_tasks_list', 'read the tasks'],
        ['-print_ship', 'prints details of ship'],

        ['-add_booking', 'create booking'],
        ['-read_booking', 'read booking'],
        ['-remove_booking', 'remove booking'],

        ['-freight_calculator', 'calculate_freight'],

        ['-fill_template', 'function will fill a template'],
        ['-create_template', 'create a template written by user'],
        ['-remove_template', 'remove a template'],

        ['-add_company', 'create a company'],
        ['-remove_company', 'remove a company'],
        ['-edit_company', 'edit a company'],

        ['-add_person', 'create a person'],
        ['-remove_person', 'remove a person'],
        ['-edit_person', 'edit a person'],

        ['-add_position', 'add position'],
        ['-check_position_status', 'select position'],

        ['-add_index', 'add index']]

    for argument in arguments:
        parser.add_argument(argument[0], help=argument[1], action='store_true')

    return parser


def creating_result(parser):
    result = {
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
        'edit_person': parser.parse_args().edit_person,

        'add_position': parser.parse_args().add_position,
        'check_position_status': parser.parse_args().check_position_status,

        'add_index': parser.parse_args().add_index

    }
    return result


def parcer():
    # creating parser
    parser = argparse.ArgumentParser(description='Working with ship\'s list.',
                                     prog='ships_list')

    parser_with_arguments = adding_arguments(parser)

    # generating result
    result = creating_result(parser_with_arguments)

    return result

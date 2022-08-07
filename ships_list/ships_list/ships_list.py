from ships_list.additional_functions.ships_functions import add_ship,\
    remove_ship, read_ship, print_ship
from ships_list.additional_functions.tasks_functions import add_task,\
    remove_task, redact_task, amend_task, read_tasks_list, close_task
from ships_list.additional_functions.voyage_functions import add_voyage, \
    remove_voyage
from ships_list.additional_functions.freight_calculator \
    import freight_calculator


def ships_list(parced_result):
    options = {
        'add_ship': add_ship,
        'read_ship': read_ship,
        'ship_to_remove': remove_ship,
        'remove_ship': remove_ship,
        'print_ship': print_ship,

        'add_task': add_task,
        'amend_task': amend_task,
        'redact_task': redact_task,
        'remove_task': remove_task,
        "read_tasks_list": read_tasks_list,
        "close_task": close_task,

        'add_voyage': add_voyage,
        'remove_voyage': remove_voyage,
        'freight_calculator': freight_calculator,
    }

    function = list(filter(lambda x: parced_result[x], parced_result))[0]
    options[function]()

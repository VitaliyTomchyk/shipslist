from ships_list.additional_functions.ship.ships_functions import add_ship,\
    remove_ship, read_ship, print_ship
from ships_list.additional_functions.tasks_functions import add_task,\
    remove_task, amend_task, read_tasks_list, close_task
from ships_list.additional_functions.voyage.voyage_functions \
    import add_voyage, remove_voyage
from ships_list.additional_functions.freight_calculator.freight_calculator \
    import freight_calculator
from ships_list.additional_functions.booking.booking_functions \
    import add_booking, read_booking, remove_booking
from ships_list.additional_functions.templates.template_manager \
    import fill_template
from ships_list.additional_functions.templates.create_template.\
    create_template import create_template


def ships_list(parced_result):
    options = {
        'add_ship': add_ship,
        'read_ship': read_ship,
        'ship_to_remove': remove_ship,
        'remove_ship': remove_ship,
        'print_ship': print_ship,

        'add_task': add_task,
        'amend_task': amend_task,
        'remove_task': remove_task,
        "read_tasks_list": read_tasks_list,
        "close_task": close_task,

        'add_voyage': add_voyage,
        'remove_voyage': remove_voyage,

        'add_booking': add_booking,
        'read_booking': read_booking,
        'remove_booking': remove_booking,

        'freight_calculator': freight_calculator,

        'fill_template': fill_template,
        'create_template': create_template
    }

    function = list(filter(lambda x: parced_result[x], parced_result))[0]
    options[function]()

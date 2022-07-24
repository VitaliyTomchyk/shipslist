from ships_list.additional_functions.ships_functions import add_ship,\
    remove_ship, read_ship
from ships_list.additional_functions.tasks_functions import add_task,\
    remove_task, redact_task
from ships_list.additional_functions.voyage_functions import add_voyage, \
    remove_voyage


def ships_list(parced_result):
    options = {'add_ship': add_ship,
               'ship_to_remove': remove_ship,
               'add_task': add_task,
               'add_voyage': add_voyage,
               'remove_voyage': remove_voyage,
               'remove_task': remove_task,
               'redact_task': redact_task,
               'remove_ship': remove_ship,
               'read_ship': read_ship}
    function = list(filter(lambda x: parced_result[x], parced_result))[0]
    options[function]()

    # if parced_result['added_ship']:
    #     add_ship()

    # if parced_result['ship_to_remove']:
    #     remove_ship()

    # if parced_result['add_task']:
    #     add_task()

    # if parced_result['add_voyage']:
    #     add_voyage()

    # if parced_result['remove_voyage']:
    #     remove_voyage()

    # if parced_result['remove_task']:
    #     remove_task(parced_result['remove_task'])

    # if parced_result['redact_task']:
    #     redact_task(parced_result['redact_task'])

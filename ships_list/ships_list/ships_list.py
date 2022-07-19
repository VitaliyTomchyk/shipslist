from ships_list.additional_functions.ships_functions import add_ship,\
                                                            remove_ship
from ships_list.additional_functions.tasks_functions import add_task,\
    read_tasks_list, remove_task, redact_task
from ships_list.additional_functions.voyage_functions import add_voyage, \
    read_voyage, remove_voyage


def ships_list(parced_result):
    ship = parced_result['ship']
    task = parced_result['tasks_name']
    stage = parced_result['task_stage']
    party = parced_result['task_party']

    if parced_result['added_ship']:
        add_ship()

    if parced_result['ship_to_remove']:
        remove_ship()

    if task:
        add_task(ship, task, stage, party)

    if parced_result['add_voyage']:
        add_voyage()

    if parced_result['read_voyage']:
        read_voyage(parced_result['read_voyage'])

    if parced_result['remove_voyage']:
        remove_voyage(parced_result['remove_voyage'])

    if parced_result['read_tasks_list']:
        read_tasks_list(parced_result['read_tasks_list'])

    if parced_result['remove_task']:
        remove_task(parced_result['remove_task'])

    if parced_result['redact_task']:
        redact_task(parced_result['redact_task'])

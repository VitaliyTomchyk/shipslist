from ships_list.additional_functions.additional_functions import add_ship,\
                                                                 add_task,\
                                                                 IMO_checker,\
                                                                 remove_ship
from ships_list.additional_functions.import_tasks import add_list


def ships_list(parced_result):
    IMO = parced_result['IMO']
    ship = parced_result['ship']
    task = parced_result['tasks_name']
    stage = parced_result['task_stage']
    party = parced_result['task_party']

    if parced_result['added_ship']:
        add_ship(parced_result['added_ship'], IMO)

    if task:
        add_task(ship, task, stage, party)

    if parced_result['remove_ship']:
        remove_ship(parced_result['ship_to_remove'])

    if parced_result['add_list']:
        add_list(parced_result['add_list'], parced_result['task_party'])

from ships_list.additional_functions.ships_functions import add_ship,\
                                                            remove_ship
from ships_list.additional_functions.tasks_functions import add_task,\
                                                            read_ships_list, \
                                                            add_list

def ships_list(parced_result):
    IMO = parced_result['IMO']
    ship = parced_result['ship']
    task = parced_result['tasks_name']
    stage = parced_result['task_stage']
    party = parced_result['task_party']

    if parced_result['added_ship']:
        add_ship(parced_result['added_ship'], IMO)

    if parced_result['ship_to_remove']:
        remove_ship(parced_result['ship_to_remove'])

    if task:
        add_task(ship, task, stage, party)

    if parced_result['add_list']:
        add_list(parced_result['add_list'], parced_result['task_party'])

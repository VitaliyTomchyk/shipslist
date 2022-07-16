from ships_list.additional_functions.ships_functions import add_ship,\
                                                            remove_ship
from ships_list.additional_functions.tasks_functions import add_task
from ships_list.additional_functions.voyage_functions import add_voyage, \
    read_voyage, remove_voyage


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

    if parced_result['add_voyage']:
        add_voyage(parced_result['ship'], parced_result['l_ports'],
                   parced_result['d_ports'], parced_result['restr_points'],
                   parced_result['voy_type'])
    
    if parced_result['read_voyage']:
        read_voyage(parced_result['read_voyage'])
    
    if parced_result['remove_voyage']:
        remove_voyage(parced_result['remove_voyage'])

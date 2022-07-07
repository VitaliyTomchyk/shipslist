
from ships_list.additional_functions.additional_functions import add_ship
from ships_list.additional_functions.additional_functions import add_task
from ships_list.additional_functions.additional_functions import IMO_checker


def ships_list(parced_result):
    ships_name, IMO = parced_result['ships_name'].upper(), parced_result['IMO']
    task = parced_result['tasks_name']

    if IMO_checker(IMO) is False:
        print('IMO is not correct')
        return

    if parced_result['add_ship']:
        add_ship(ships_name, IMO)

    if parced_result['add_task']:
        add_task(ships_name, IMO, task)

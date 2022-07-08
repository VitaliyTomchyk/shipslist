
from ships_list.additional_functions.additional_functions import add_ship,\
                                                                 add_task,\
                                                                 IMO_checker,\
                                                                 remove_ship
from ships_list.additional_functions.import_tasks import add_list


def ships_list(parced_result):
    print(parced_result)
    ships_name, IMO = parced_result['ships_name'], parced_result['IMO']
    task = parced_result['tasks_name']

    if IMO_checker(IMO) is False:
        print('IMO is not correct')
        return

    if parced_result['add_ship']:
        add_ship(ships_name.upper(), IMO)

    if parced_result['add_task']:
        add_task(ships_name, IMO, task)
    
    if parced_result['remove_ship']:
        remove_ship(parced_result['ship_to_remove'])
    
    if parced_result['add_list']:
        add_list(parced_result['add_list'])

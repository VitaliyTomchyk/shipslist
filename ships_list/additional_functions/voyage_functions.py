from ships_list.additional_functions.additional_functions import id_generator,\
    append_JSON_file, missing_arguments_checker


def add_voyage(ship, list_of_l_ports, list_of_d_ports, list_of_canals, type):
    result = {"id": id_generator(),
              "ship": ship,
              "l_ports": list_of_l_ports,
              "d_ports": list_of_d_ports,
              "restr_points": list_of_canals,
              "voy_type": type}

    checked_reasuls = result.copy()
    del checked_reasuls['restr_points']

    if missing_arguments_checker(checked_reasuls) is False:
        print('Voyage has not been added.')
        return
    else:
        append_JSON_file(result, 'ships_list/lists/list_of_voyages.json')
        print('Voyage has been added.')


def remove_voyage():
    return

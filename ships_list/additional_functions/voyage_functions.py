from ships_list.additional_functions.additional_functions import id_generator,\
    append_JSON_file


def add_voyage(ship, list_of_l_ports, list_of_d_ports, list_of_canals, type):
    result = {"id": id_generator(),
              "ship": ship,
              "load_ports": list_of_l_ports,
              "discharge_ports": list_of_d_ports,
              "canals": list_of_canals,
              "type": type}
    append_JSON_file(result, 'ships_list/lists/list_of_voyages.json')
    return result


def remove_voyage():
    return

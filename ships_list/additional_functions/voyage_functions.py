from ships_list.additional_functions.additional_functions import id_generator,\
    append_JSON_file, missing_arguments_checker, read_JSON_file, \
    write_JSON_file


def add_voyage(ship, list_of_l_ports, list_of_d_ports, list_of_canals, type):
    result = {"id": id_generator(),
              "ship": ship,
              "l_ports": list_of_l_ports,
              "d_ports": list_of_d_ports,
              "restr_points": list_of_canals,
              "voy_type": type}

    checked_results = result.copy()
    del checked_results['restr_points']

    if missing_arguments_checker(checked_results) is False:
        print('Voyage has not been added.')
        return
    else:
        append_JSON_file(result, 'ships_list/lists/list_of_voyages.json')
        print('Voyage has been added.')


def read_voyage(id):
    voyages = read_JSON_file('ships_list/lists/list_of_voyages.json')
    the_voyage = list(filter(lambda x: True if x['id'] == int(id) else False,
                             voyages))[0]

    result = 'Voyage details are following\n'
    for key in the_voyage:
        result = result + "\n" + key + ':  ' + str(the_voyage[key])
    print(result + "\n")


def remove_voyage(id):
    voyages = read_JSON_file('ships_list/lists/list_of_voyages.json')

    the_voyage = list(filter(lambda x: True if x['id'] == int(id) else False,
                             voyages))[0]

    voyages.remove(the_voyage)
    print("Following voyage will be removed.")
    read_voyage(id)

    write_JSON_file(voyages, 'ships_list/lists/list_of_voyages.json')
    print('Voyage is removed.')

from ships_list.additional_functions.additional_functions import id_generator,\
    append_JSON_file, missing_arguments_checker, read_JSON_file, \
    write_JSON_file, dictionary_finder, input_item, \
    input_option, read_dict, input_from_supporting_info


def add_voyage():
    # file = 'ships_list/lists/Standard/supporting_info.json'
    file_with_ships = 'ships_list/lists/ships.json'

    result = {"id": id_generator(),
              "ship": input_option(file_with_ships, 'ships_name',
                                   'ship\'s name'),
              "l_ports": input_item('load port(s)'),
              "d_ports": input_item('disch port(s)'),
              "restr_points": input_item('restricting points'),
              "voy_type": input_from_supporting_info('voyage_types')}

    checked_results = result.copy()
    del checked_results['restr_points']

    if missing_arguments_checker(checked_results) is False:
        return
    else:
        append_JSON_file(result, 'ships_list/lists/list_of_voyages.json')
        print('Following voyage has been added.')
        read_dict(result)


def read_voyage(id):
    voyages = read_JSON_file('ships_list/lists/list_of_voyages.json')
    the_voyage = dictionary_finder(voyages, int(id), 'id')

    result = 'Voyage details are following\n'
    for key in the_voyage:
        result = result + "\n" + key + ':  ' + str(the_voyage[key])
    print(result + "\n")


def remove_voyage():
    print('Please put id of voyage you want to remove')
    the_id = input()

    voyages = read_JSON_file('ships_list/lists/list_of_voyages.json')
    the_voyage = dictionary_finder(voyages, int(the_id), 'id')

    voyages.remove(the_voyage)
    print("Following voyage will be removed.")
    read_voyage(id)

    write_JSON_file('ships_list/lists/list_of_voyages.json', voyages)
    print('Voyage is removed.')

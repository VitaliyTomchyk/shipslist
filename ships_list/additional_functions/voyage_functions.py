from ships_list.additional_functions.additional_functions import id_generator,\
    append_JSON_file, missing_arguments_checker, read_JSON_file, \
    write_JSON_file, dictionary_finder, list_to_string, input_item, \
    input_option


def input_ship():
    ships = [x['ships_name'] for x in
             read_JSON_file('ships_list/lists/ships.json')]
    print('Please put ship\'s name from following list')
    print(list_to_string(ships))

    the_ship = input().upper()
    if the_ship in ships:
        return the_ship
    else:
        print('ship is not correct')
        return None


def add_voyage():

    result = {"id": id_generator(),
              "ship": input_ship(),
              "l_ports": input_item('load port(s)'),
              "d_ports": input_item('disch port(s)'),
              "restr_points": input_item('restricting points'),
              "voy_type": input_option('voyage_types')}

    checked_results = result.copy()
    del checked_results['restr_points']

    if missing_arguments_checker(checked_results) is False:
        return
    else:
        append_JSON_file(result, 'ships_list/lists/list_of_voyages.json')
        print('Following voyage has been added.')
        print(result)


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

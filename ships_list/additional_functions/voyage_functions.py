from ships_list.additional_functions.additional_functions import id_generator,\
    missing_arguments_checker, dictionary_finder, input_item, \
    input_option, read_dict, input_from_supporting_info
from ships_list.lists.Standard.constats import LIST_OF_VOYAGES_FILE, SHIPS_FILE
from ships_list.additional_functions.json_functions import write_JSON_file, \
    append_JSON_file, read_JSON_file


def add_voyage():

    result = {"id": id_generator(),
              "ship": input_option(SHIPS_FILE, 'ships_name',
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
        append_JSON_file(result, LIST_OF_VOYAGES_FILE)
        print('Following voyage has been added.')
        read_dict(result)


def read_voyage(id):
    voyages = read_JSON_file(LIST_OF_VOYAGES_FILE)
    the_voyage = dictionary_finder(voyages, int(id), 'id')

    result = 'Voyage details are following\n'
    for key in the_voyage:
        result = result + "\n" + key + ':  ' + str(the_voyage[key])
    print(result + "\n")


def remove_voyage():
    print('Please put id of voyage you want to remove')
    the_id = input()

    voyages = read_JSON_file(LIST_OF_VOYAGES_FILE)
    the_voyage = dictionary_finder(voyages, int(the_id), 'id')

    voyages.remove(the_voyage)
    print("Following voyage will be removed.")
    read_voyage(id)

    write_JSON_file(LIST_OF_VOYAGES_FILE, voyages)
    print('Voyage is removed.')

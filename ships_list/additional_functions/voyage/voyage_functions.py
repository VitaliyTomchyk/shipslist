from ships_list.additional_functions.supporting_functions.additional_functions\
    import missing_arguments_checker, dictionary_finder, \
    read_dict
from ships_list.lists.Standard.constants import LIST_OF_VOYAGES_FILE
from ships_list.additional_functions.supporting_functions.json_functions \
    import write_JSON_file, append_JSON_file, read_JSON_file
from ships_list.additional_functions.voyage.additional_voyage_functions \
    import voyage_details_collector, voyage_stages_generator, \
    points_sequence_generator


def add_voyage():
    # collect voyage details
    voyage_details = voyage_details_collector()

    # generate voyage stages
    voyage_details['voyage_stages'] = voyage_stages_generator(voyage_details)

    # generate voyage points sequence
    voyage_details['points_sequence'] = points_sequence_generator(
        voyage_details)

    # if all arguments on place append voyage to list of voyages
    if missing_arguments_checker(voyage_details, ['restr_points']) is False:
        return
    else:
        append_JSON_file(voyage_details, LIST_OF_VOYAGES_FILE)
        print('Following voyage has been added.')
        read_dict(voyage_details)


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


def short_voyage_info(voyage):

    ship, charterer = voyage['ship'], voyage['charterer']
    weight, cargo = voyage['weight_of_cargo'], voyage['cargo']
    load_ports, discharge_ports = voyage['l_ports'], voyage['d_ports']

    result = '{} acc {} - {} mt of {}\n from {} to {} '.format(ship, charterer,
                                                               weight, cargo,
                                                               load_ports,
                                                               discharge_ports)
    return result

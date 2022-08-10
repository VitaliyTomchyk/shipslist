from ships_list.additional_functions.additional_functions \
    import id_generator, list_to_ol_string,\
    missing_arguments_checker, dictionary_finder, \
    read_dict, appender
from ships_list.lists.Standard.constats import LIST_OF_VOYAGES_FILE, \
    SHIPS_FILE
from ships_list.additional_functions.json_functions import write_JSON_file, \
    append_JSON_file, read_JSON_file
from ships_list.additional_functions.input_functions import input_point, \
    input_with_num, input_option


def appender_of_stages(voyage, result):

    pairs = []
    # TODO refactor this code to use list comprehension
    for port in voyage['l_ports']:
        pairs.append(tuple([port, 'load port']))

    for port in voyage['d_ports']:
        pairs.append(tuple([port, 'discharge port']))

    for port in voyage['restr_points']:
        pairs.append(tuple([port, 'restriction point']))

    pairs = tuple(filter(lambda x: x if x[1] is not None else False,
                         pairs))
    lines = ('Prior arrival at ', 'At ')

    for value in pairs:
        for line in lines:
            print(value)
            result.append(line + str(str(value[1]) + ' ' + value[0][0]))

    # for load_port in voyage['l_ports']:
    #     result.append(['Prior arrival at load port {}'.format(load_port)])
    #     result.append(['At load port {}'.format(load_port)])

    # for discharge_port in voyage['d_ports']:
    #     result.append(['Prior arrival at discharge ' +
    #                    'port {}'.format(discharge_port)])
    #     result.append(['At discharge port {}'.format(discharge_port)])

    # for restr_point in voyage['restr_point']:
    #     result.append(['Prior arrival at restriction ' + \
    #         'point {}'.format(restr_point)])
    #     result.append(['At load port {}'.format(restr_point)])

    return result


def voyage_stages_generator(voyage):

    result = appender_of_stages(voyage, [])
    result.append('After redelivery')

    return result

# list index switcher based on values


def points_switcher(the_list, instruction):
    index_from, index_to = instruction
    first_value, second_value = the_list[int(index_from)], \
        the_list[int(index_to)]
    ind_first, ind_second = the_list.index(first_value), \
        the_list.index(second_value)
    the_list[ind_first], the_list[ind_second] = the_list[ind_second], \
        the_list[ind_first]
    return the_list


def points_reorderer(list_of_points):
    change_requred = True
    while change_requred:
        print('Please note, following order of points is used:')
        print(list_to_ol_string(list_of_points))

        print('\nDo you want to change order of points? (y/n)')
        if input() == 'y':
            print('\nPlease put new order of points.\n')
            print('If you want to put 1st point on the 2nd place, put "1-2".')
            instruction_for_change = input('Put switch instruction').split('-')
            print(instruction_for_change)

            list_of_points = points_switcher(list_of_points,
                                             instruction_for_change)
        else:
            change_requred = False

    return list_of_points


def points_sequence_generator(voyage):
    result = []

    for key in ['delivery_point', 'l_ports', 'd_ports',
                'restr_points', 'bunkering_point',
                'redel_point']:
        result = appender(result, key, voyage)

    reordered_result = points_reorderer(result)
    return reordered_result


def voyage_details_collector():
    return {
        "id": id_generator(),
        "charterer": input('\nPut name of Charterers company\n'),
        "cargo": input("\nPut name of cargo\n"),
        "weight_of_cargo": input("\nPut weight of cargo in tonns\n"),
        "ship": input_option(
            SHIPS_FILE,
            'ships_name',
            'ship\'s name'),
        "delivery_point": input('\nPut delivery point\n'),
        "l_ports": input_point('load port(s)'),
        "d_ports": input_point('disch port(s)'),
        "restr_points": input_point('restricting points'),
        "bunkering_point": input_point('bunkering point'),
        "redel_point": input('\nPut redelivery point\n'),
        "points_sequence": [],
        "stage_of_voyage": "Prior delivery",
        "voy_type": input_with_num(
            'voyage_types',
            'type of voyage')}


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

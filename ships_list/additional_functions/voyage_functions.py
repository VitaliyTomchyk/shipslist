from ships_list.additional_functions.additional_functions import id_generator,\
    missing_arguments_checker, dictionary_finder, \
    input_option, read_dict, input_with_num
from ships_list.lists.Standard.constats import LIST_OF_VOYAGES_FILE, \
    SHIPS_FILE, SUPPORTING_FILE
from ships_list.additional_functions.json_functions import write_JSON_file, \
    append_JSON_file, read_JSON_file


def appender_of_stages(voyage, result):

    for load_port in voyage['l_ports']:
        result.append(['Prior arrival at load port {}'.format(load_port)])
        result.append(['At load port {}'.format(load_port)])

    for discharge_port in voyage['d_ports']:
        result.append(['Prior arrival at discharge ' +
                       'port {}'.format(discharge_port)])
        result.append(['At discharge port {}'.format(discharge_port)])

    for restr_point in voyage['restr_point']:
        result.append(['Prior arrival at load port {}'.format(restr_point)])
        result.append(['At load port {}'.format(restr_point)])

    return result


def voyage_stages_generator(voyage):

    standard_stages = read_JSON_file(SUPPORTING_FILE)['stages']
    result = [standard_stages[0], standard_stages[1]]
    result = appender_of_stages(voyage, result)
    result.append('After redelivery')

    return result


def input_point(type, quantity_of_ports=None):

    result = []
    if quantity_of_ports is None:
        quantity = int(input('Please put quantity of {}\n'.format(type)))
    else:
        quantity = quantity_of_ports

    i = 0
    while i < quantity:
        text = 'Please put name of {} number {}\n'.format(type, i + 1)
        result.append(str(input(text)))
        i = i + 1

    return result


def add_voyage():

    result = {"id": id_generator(),
              "charterer": input('\nPut name of Charterers company\n'),
              "cargo": input("\nPut name of cargo\n"),
              "weight_of_cargo": input("\nPut weight of cargo in tonns\n"),
              "ship": input_option(SHIPS_FILE, 'ships_name',
                                   'ship\'s name'),

              "delivery_point": input_point('delivery point', 1),
              "del_point": input_point('delivery point', 1),
              "l_ports": input_point('load port(s)'),
              "d_ports": input_point('disch port(s)'),
              "restr_points": input_point('restricting points'),
              "bunkering_point": input_point('bunkering point'),
              "redel_point": input_point('redelivery point', 1),

              "stage_of_voyage": "Prior delivery",
              "voy_type": input_with_num('voyage_types', 'type of voyage')}

    result['voyage_stages'] = voyage_stages_generator(result)

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


def short_voyage_info(voyage):

    ship, charterer = voyage['ship'], voyage['charterer']
    weight, cargo = voyage['weight_of_cargo'], voyage['cargo']
    load_ports, discharge_ports = voyage['l_ports'], voyage['d_ports']

    result = '{} acc {} - {} mt of {}\n from {} to {} '.format(ship, charterer,
                                                               weight, cargo,
                                                               load_ports,
                                                               discharge_ports)
    return result

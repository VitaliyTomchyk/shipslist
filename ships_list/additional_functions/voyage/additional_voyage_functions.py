from ships_list.additional_functions.supporting_functions.input_functions \
    import input_point, \
    input_with_num, input_option
from ships_list.additional_functions.supporting_functions.additional_functions\
    import id_generator, appender, list_to_ol_string
from ships_list.lists.Standard.constants import SHIPS_FILE


def assign_type_to_point(point, voyage):
    pairs = []
    for value in voyage[point]:
        pairs.append((point, value))
    return pairs


def stage_assigner(pairs, result):
    for value in pairs:
        for line in ('Prior arrival at ', 'At '):
            print(value)
            result.append(line + str(str(value[1]) + ' ' + value[0][0]))
    return result


def appender_of_stages(voyage, result):
    points = ['l_ports', 'd_ports', 'restr_points', 'bunkering_point']
    pairs = list(map(lambda x: assign_type_to_point(x, voyage), points))
    pairs = tuple(filter(lambda x: x if x[1] is not None else False,
                         pairs))
    result = stage_assigner(pairs, result)
    return result


def voyage_stages_generator(voyage):
    result = appender_of_stages(voyage, [])
    result.append('After redelivery')
    return result


def points_switcher(the_list, instruction):
    index_from, index_to = instruction
    first_value, second_value = the_list[int(index_from)], \
        the_list[int(index_to)]
    ind_first, ind_second = the_list.index(first_value), \
        the_list.index(second_value)
    the_list[ind_first], the_list[ind_second] = the_list[ind_second], \
        the_list[ind_first]
    return the_list


def order_change_scripts(list_of_points):
    text_line = '\nPlease put new order of points.\n' + \
                'If you want to put 1st point on the 2nd place, ' + \
                'put "1-2".\nPut switch instruction\n'
    instruction_for_change = list(map(int, input(
        text_line).split('-')))
    updated_instruction = [x - 1 for x in instruction_for_change]

    list_of_points = points_switcher(list_of_points, updated_instruction)
    return list_of_points


def points_reorderer(old_list_of_points):
    change_requred = True
    while change_requred:
        print('Please note, following order of points is used:\n' +
              list_to_ol_string(old_list_of_points))

        print('\nDo you want to change order of points? (y/n)')
        if input() == 'y':
            updated_list_of_points = order_change_scripts(old_list_of_points)
        else:
            change_requred = False
    return updated_list_of_points


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

from ships_list.additional_functions.supporting_functions.input_functions \
    import input_option
from ships_list.lists.Standard.constants import SUPPORTING_FILE


# add distance to points for in_SECA = False or True
def add_distances(points):

    print('\nPlease put distance between points in nautical miles.')

    legs = []

    for i in range(len(points) - 1):
        for marker_SECA, SECA_type in [('total', 'total'),
                                       ('only SECA', 'only_SECA')]:
            from_point, to_point = points[i]['point_name'], \
                points[i + 1]['point_name']
            text = 'Please put {} distance \n- from {} {} to {} {}\n'
            request = text.format(
                marker_SECA,
                points[i]['point_type'],
                from_point,
                points[i + 1]['point_type'],
                to_point)

            the_leg = {}
            the_leg['distance_' + SECA_type] = {}
            the_leg['distance_' + SECA_type]['distance'] = \
                int(input(request))
            the_leg['description'] = {'from': from_point,
                                      'to': to_point,
                                      'condition': ask_condition(from_point,
                                                                 to_point),
                                      # TODO input speed type for each SECA
                                      # TYPE
                                      'speed_type': ask_speed_type()}
            legs.append(the_leg)

    return legs

# ask condition for distance


def ask_condition(point_from, point_to):
    text = 'Please put condition of vessel for leg \n' + \
        '- from {} to {}\n'.format(point_from, point_to)
    print(text)

    condition = input_option(SUPPORTING_FILE, 'vessel_conditions',
                             'condition of vessel')
    return condition


def ask_speed_type():
    print('Please put speed type for distance.')
    speed_type = input_option(SUPPORTING_FILE, 'speed_types', 'speed type')
    return speed_type

from ships_list.additional_functions.supporting_functions.input_functions \
    import input_option
from ships_list.lists.Standard.constants import SUPPORTING_FILE


# add distance to points for in_SECA = False or True
def add_distances(points):

    print('\nPlease put distance between points in nautical miles.')

    legs = []

    # adding distances between points
    for i in range(len(points) - 1):
        the_leg = {}
        for marker_SECA, dist_type in [('total', 'total'),
                                       ('only SECA', 'only_SECA')]:
            the_leg = k(the_leg, points, marker_SECA, dist_type, i)
        legs.append(the_leg)

    return legs


def k(the_leg, points, marker_SECA, dist_type, i):

    from_point, to_point = points[i]['point_name'], \
        points[i + 1]['point_name']

    text = 'Please put {} distance \n- from {} {} to {} {}\n'

    request = text.format(
        marker_SECA,
        points[i]['point_type'],
        from_point,
        points[i + 1]['point_type'],
        to_point)
    # TODO add weatherfactor in below dict
    the_leg['distance_' + dist_type] = {'distance': int(input(request)),
                                        'speed': add_speed_type(dist_type)}

    the_leg['description'] = add_leg_description(from_point, to_point,
                                                 dist_type)

    return the_leg


def add_leg_description(from_point, to_point, dist_type):
    result = {'from': from_point,
              'to': to_point,
              'condition': add_leg_condition(from_point, to_point)}
    return result


def add_leg_condition(point_from, point_to):
    # TODO add algorithm to calculate leg condition
    text = 'Please put condition of vessel for leg \n' + \
        '- from {} to {}\n'.format(point_from, point_to)
    print(text)

    condition = input_option(SUPPORTING_FILE, 'vessel_conditions',
                             'condition of vessel')
    return condition


def add_speed_type(dist_type):
    updated_dist_type = dist_type if dist_type != 'total' else 'in SECA'
    print('Please put speed type for {} distance.'.format(updated_dist_type))

    speed_type = input_option(SUPPORTING_FILE, 'speed_types', 'speed type')
    return speed_type

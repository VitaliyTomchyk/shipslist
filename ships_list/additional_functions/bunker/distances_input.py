from ships_list.additional_functions.supporting_functions.input_functions \
    import input_option
from ships_list.lists.Standard.constants import SUPPORTING_FILE
from ships_list.additional_functions.bunker.weather.weather_functions \
    import add_weather_factor


# add distance to points for in_SECA = False or True
def add_distances(points):

    print('\nPlease put distance between points in nautical miles.')

    legs = []

    # adding distances between points
    for i in range(len(points) - 1):
        the_leg = {}
        for marker_SECA, dist_type in [('total', 'total'),
                                       ('only SECA', 'only_SECA')]:
            the_points = [points[i], points[i + 1]]
            the_sub_leg = sub_leg_generator(the_points, marker_SECA, dist_type)
            the_leg[dist_type] = the_sub_leg
        legs.append(the_leg)

    return legs


def sub_leg_generator(points, marker_SECA, dist_type):

    the_dist_type = dist_type if dist_type != 'total' else 'not_SECA'

    the_leg = {}
    from_point, to_point = points[0]['point_name'], \
        points[1]['point_name']

    the_leg['description'] = add_leg_description(from_point, to_point,
                                                 the_dist_type)

    text = 'Please put {} distance \n- from {} {} to {} {}\n'

    request = text.format(
        marker_SECA,
        points[0]['point_type'],
        from_point,
        points[1]['point_type'],
        to_point)

    the_leg['distance_' + the_dist_type] = \
        {'distance': int(input(request)),
         'speed': add_speed_type(the_dist_type),
         'wf': add_weather_factor(the_leg['description'], dist_type)}

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
    print('Please put speed type for {} distance.'.format(dist_type))

    speed_type = input_option(SUPPORTING_FILE, 'speed_types', 'speed type')
    return speed_type

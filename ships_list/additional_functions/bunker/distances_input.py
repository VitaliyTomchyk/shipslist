from ships_list.additional_functions.supporting_functions.input_functions \
    import input_option_from_dict
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
            the_leg[dist_type] = sub_leg_generator(the_points, marker_SECA,
                                                   dist_type)
        legs.append(the_leg)

    return legs


def sub_leg_generator(points, marker_SECA, dist_type):

    from_point, to_point = points[0], points[1]
    text = 'Please put {} distance \n- from {} {} to {} {}\n'
    request = text.format(
        marker_SECA,
        points[0]['point_type'],
        from_point['point_name'],
        points[1]['point_type'],
        to_point['point_name'])

    distance = int(input(request))
    # TODO make algorythm for generating type of leg based on type of points
    leg_type = add_leg_type(from_point, to_point)
    speed = add_speed_type(distance)
    wf = add_weather_factor(distance, dist_type)

    return {'leg_type': leg_type,
            'distance': distance,
            'speed': speed,
            'wf': wf}


def add_leg_type(from_point, to_point):
    result = {'from': from_point,
              'to': to_point,
              'condition': add_leg_condition(from_point, to_point)}
    return result


def add_leg_condition(point_from, point_to):
    # TODO add algorithm to calculate leg condition
    text = 'Please put condition of vessel for leg \n' + \
        '- from {} to {}\n'.format(point_from['point_name'],
                                   point_to['point_name'])
    print(text)

    condition = input_option_from_dict(SUPPORTING_FILE, 'vessel_condition',
                                       'condition of vessel')
    return condition


def add_speed_type(distance):
    print('Please put speed type.')

    if distance == 0:
        return 'full'

    speed_type = input_option_from_dict(
        SUPPORTING_FILE, 'speed_types', 'speed type')
    return speed_type

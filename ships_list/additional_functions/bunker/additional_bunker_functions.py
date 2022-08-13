from ships_list.lists.Standard.constants import SUPPORTING_FILE
from ships_list.additional_functions.input_functions import input_option


# input points of route
def input_points():
    # input points
    points = []
    point_input_required = True
    while point_input_required:

        point = {}
        # adding point parameter 'point_name'
        point['point_name'] = input(
            'Please put name of point, else push Enter\n')
        if point['point_name'] == '':
            point_input_required = False
            break

        # adding point parameter 'point_type'
        point['point_type'] = input_option(SUPPORTING_FILE,
                                           'point_type',
                                           'point type')

        # adding point parameter 'weather_factor_in_SECA'
        in_SECA = input(
            'Is point {} in SECA zone? (y/n)'.format(point['point_name']))
        point['in_SECA'] = True if in_SECA == 'y' else False

        # adding point parameter duration of stay
        point = adding_duration_of_stay(point)

        # adding points with point
        points.append(point)

    return points


def adding_duration_of_stay(point):

    # input quantity of working days
    if point['point_type'] == 'loading' \
            or point['point_type'] == 'discharging':
        question = 'Is point {} working with ship\'s cranes? (y/n)'
        reply_working = input(
            question.format(point['point_name']))
        if reply_working == 'y':
            # input quantity of working days
            point['working_days'] = int(
                input(
                    'Please put quantity of working days at {}\n'.format(
                        point['point_name'])))

    # input quantity of idle days
    point['idle_days'] = int(
        input(
            'Please put quantity of idle days at {}\n'.format(
                point['point_name'])))

    return point


# adding weather factor to distances
def add_weather_factor(distances):
    for distance in distances:
        if distance['distance_in_SECA'] != 0:
            text = 'Please put weather factor for {} in SECA zone\n'.format(
                distance['point_name'])
            distance['wf_in_SECA'] = int(input(text))

        if distance['distance_total'] > distance['distance_in_SECA']:
            text = 'Please put weather factor for {} excluding SECA\n'.format(
                distance['point_name'])
            distance['wf_excluding_SECA'] = int(input(text))
        else:
            distance['wf_excluding_SECA'] = 0
    return distances


# add distance to points for in_SECA = False or True
def add_distance(points):
    distances = []
    for marker_SECA, port_of_key in [('total', 'only SECA',),
                                     ('in_total', 'in_SECA')]:
        for i in range(len(points) - 1):
            request = 'Please put {} distance from {} to {} in SECA\n'.format(
                marker_SECA,
                points[i]['point_name'],
                points[i + 1]['point_name'])

            distances[i]['distance_' + port_of_key] = int(input(request))
            distances[i]['description']['from'] = points[i]['point_name']
            distances[i]['description']['to'] = points[i + 1]['point_name']
    return distances

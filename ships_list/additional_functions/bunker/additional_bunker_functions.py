from ships_list.lists.Standard.constants import SUPPORTING_FILE
from ships_list.additional_functions.input_functions import input_option, \
    input_option_from_dict


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
        point['laytime_port_terms'] = input_option_from_dict(
            SUPPORTING_FILE, 'laytime_port_terms', 'laytime port terms')

        # adding duration of port stay to load and disch point
        point = adding_duration_of_stay(point, point['laytime_port_terms'])

        # adding points with point
        points.append(point)

    return points


def adding_duration_of_stay_working(point, laytime_port_terms):

    # adding laytime port terms for point
    point['lay_time_port_term'] = laytime_port_terms['point_name']
    lt_multiplier = point['lay_time_port_term']

    # adding cargo quantity for handling in the point
    point['cargo_quantity_for_handling'] = int(input(
        'Please put quantity of cargo for handling' +
        ' in {}, mt\n'.format(point['point_name'])))
    cargo_quantity = point['cargo_quantity_for_handling']

    # adding rate_of_handling for point
    point['rate_of_handling'] = int(input(
        'Please put rate of handling in {}, mt\n'.format(
            point['point_name'])))
    rate_of_handling = point['rate_of_handling']

    # input quantity of working days
    point['working_days'] = round(cargo_quantity / rate_of_handling
                                  * lt_multiplier, 2)

    return point


def adding_duration_of_stay(point, laytime_port_terms):

    # input quantity of working days
    if point['point_type'] in ['loading', 'discharging']:
        question = 'Is point {} working with ship\'s cranes? (y/n)'
        reply_working = input(question.format(point['point_name']))

        if reply_working == 'y':
            point = adding_duration_of_stay_working(point, laytime_port_terms)

    # input quantity of idle days
    point['idle_days'] = int(
        input(
            'Please put quantity of idle days at {}\n'.format(
                point['point_name'])))

    return point


def wf_setter(distance, text):

    if distance['distance_in_SECA'] != 0:
        distance['wf_in_SECA'] = int(input(text + ' in SECA, %\n'))
    else:
        distance['wf_in_SECA'] = 0

    if distance['distance_total'] > distance['distance_in_SECA']:
        distance['wf_excluding_SECA'] = int(input(text +
                                                  'excluding SECA, %\n'))
    else:
        distance['wf_excluding_SECA'] = 0

    return distance

# adding weather factor to distances


def add_weather_factor(distances):
    for distance in distances:
        text = 'Please put weather factor for leg' + \
            ' from {} to {}'.format(distance['from'], distance['to'])
        distance = wf_setter(distance, text)
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

            the_distance = distances[i]
            the_distance['distance_' + port_of_key] = int(input(request))
            the_distance['description']['from'] = points[i]['point_name']
            the_distance['description']['to'] = points[i + 1]['point_name']
    return distances

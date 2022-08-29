from ships_list.lists.Standard.constants import SUPPORTING_FILE
from ships_list.additional_functions.supporting_functions.input_functions \
    import input_option_from_dict
from ships_list.additional_functions.bunker.point_consumption import \
    point_consumption_calculator


def add_consuption_calculation(calculations):
    points = calculations['points']

    consumption_at_points = {}
    for point in points:
        consumption_at_points[point['point_name']] = \
            point_consumption_calculator(point, calculations['ship'])

    return calculations


# function returns point details
def inheritance_of_point_details(point_details, point_type):
    point = {}
    point['point_name'] = point_details['point_name']
    point['point_type'] = point_type
    point['in_SECA'] = point_details['in_SECA']
    point['laytime_port_terms'] = point_details['laytime_port_terms']
    return point


# input points of booking in voyage_info
def input_points_from_booking(voyage_info):
    if voyage_info is None:
        return []

    points = voyage_info['booking_info']['points']
    # TODO refactoring of below
    for point in points:
        point = adding_duration_of_stay(point)

    return points


# input points of route
def input_points_detailed(voyage_info):

    # input points
    points = input_points_from_booking(voyage_info)
    while True:

        point = {}
        # adding point parameter 'point_name'
        point['point_name'] = input(
            'Please put name of point, or push Enter to stop adding points\n')
        if point['point_name'] == '':
            break

        # adding point parameter 'point_type'
        point['point_type'] = input_option_from_dict(SUPPORTING_FILE,
                                                     'point_types',
                                                     'point type')

        # adding point parameter 'in_SECA'
        in_SECA = input(
            'Is point {} in SECA zone? (y/n)\n'.format(point['point_name']))
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
            '\nPlease put quantity of idle days at {}\n'.format(
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
    print(points)
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

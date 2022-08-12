from ships_list.additional_functions.input_functions import input_option
from ships_list.lists.Standard.constants import SHIPS_FILE, SUPPORTING_FILE, \
    BUNKERING_FILE
from ships_list.additional_functions.ships_functions import add_speed
from ships_list.additional_functions.json_functions import append_JSON_file
from ships_list.additional_functions.optimal_speed \
    import optimal_speed_calculation


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

        points.append(point)

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
        point['idle_days'] = int(
            input(
                'Please put quantity of idle days at {}\n'.format(
                    point['point_name'])))
    return points


def calculate_bunkers_consumption():
    calculations = {}
    ship = input_option(SHIPS_FILE, 'ships_name', 'ship')

    if 'speed' not in ship:
        ship = add_speed(ship)
    calculations['ship'] = ship

    # input prices of IFO, MGO, hire rate
    bunker_prices = {
        'IFO': int(input('Please put price of IFO, USD\n')),
        'MGO': int(input('Please put price of MGO, USD\n'))
    }
    calculations['bunker_prices'] = bunker_prices

    # input hire rate
    hire_rate = int(input('Please put hire rate, USD per day\n'))
    calculations['hire_rate'] = hire_rate

    # input points of route
    points = input_points()
    calculations['points'] = points

    # input distance including SECA zone from each between points
    distances = add_distance(points)

    # input weather factor for each distance
    distances_with_WF = add_weather_factor(distances)
    calculations['distances_with_WF'] = distances_with_WF

    # finding optimal speed
    optimal_speed = optimal_speed_calculation((ship, hire_rate), bunker_prices)
    print('optimal speed is \n' + str(optimal_speed))

    # save data to JSON file BUNKERING_FILE
    append_JSON_file(BUNKERING_FILE, calculations)

    result = 10
    return result


def add_weather_factor(distances):
    for distance in distances:
        if distance['distance_in_SECA'] != 0:
            distance['wf_in_SECA'] = int(input(
                'Please put weather factor for {} in SECA zone\n'.format(
                    distance['point_name'])))

        if isinstance(distance['distance_in_SECA'], int) and \
                distance['distance_total'] > distance['distance_in_SECA']:
            distance['wf_total'] = int(input(
                'Please put weather factor for {} in total\n'.format(
                    distance['point_name'])))
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

            distances[i]['description'] = '{} to {}'.format(
                points[i]['point_name'],
                points[i + 1]['point_name'])
    return distances

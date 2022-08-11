from ships_list.additional_functions.input_functions import input_option
from ships_list.lists.Standard.constants import SHIPS_FILE, SUPPORTING_FILE, \
    BUNKERING_FILE
from ships_list.additional_functions.ships_functions import add_speed
from ships_list.additional_functions.json_functions import append_JSON_file


def optimal_speed_calculation(ship, bunker_prices, hire_rate):
    optimal_speed = {}
    # # calculating price for any distance
    # duration = 1 / (ship['speed']['laden_full_speed'] * 24)
    # price_FULL_laden_bunkers = duration * \
    #     ship['consumption']['laden_full_speed'] * bunker_prices['IFO']
    # price_FULL_laden_hire = duration * hire_rate
    # total_price_FULL_laden = price_FULL_laden_bunkers \
    #     + price_FULL_laden_hire

    # duration = 1 / (ship['speed']['ballast_full_speed'] * 24)
    # price_FULL_ballast_bunkers = duration * \
    #     ship['consumption']['ballast_full_speed'] * bunker_prices['IFO']
    # price_FULL_ballast_hire = duration * hire_rate
    # total_price_FULL_ballast = price_FULL_ballast_bunkers + \
    #     price_FULL_ballast_hire

    # duration = 1 / (ship['speed']['laden_eco_speed'] * 24)
    # price_ECO_laden_bunkers = duration * \
    #     ship['consumption']['laden_eco_speed'] * bunker_prices['IFO']
    # price_ECO_laden_hire = duration * hire_rate
    # total_price_ECO_laden = price_ECO_laden_bunkers + \
    #     price_ECO_laden_hire

    # duration = 1 / (ship['speed']['ballast_eco_speed'] * 24)
    # price_ECO_ballast_bunkers = duration * \
    #     ship['consumption']['ballast_eco_speed'] * bunker_prices['IFO']
    # price_ECO_ballast_hire = duration * hire_rate
    # total_price_ECO_ballast = price_ECO_ballast_bunkers + \
    #     price_ECO_ballast_hire

    return optimal_speed


def calculate_bunkers_consumption():
    calculations = {}
    ship = input_option(SHIPS_FILE, 'ships_name', 'ship')

    if 'speed' not in ship:
        ship = add_speed(ship)

    # input prices of IFO, MGO, hire rate
    ifo_price = int(input('Please put price of IFO, USD\n'))
    mgo_price = int(input('Please put price of MGO, USD\n'))
    # hire_rate = int(input('Please put hire rate, USD per day\n'))

    # input points
    points = []
    point_input_required = True
    while point_input_required:
        point = input('Please put name of point, else push Enter\n')
        points.append({'point_name': point})
        if point == '':
            point_input_required = False

    # input type of each point
    for point in points:
        point['type'] = input_option(
            SUPPORTING_FILE, 'point_type', 'point type')

    # input if point is in SECA zone
    for point in points:
        reply_SECA = input(
            'Is point {} in SECA zone? (y/n)'.format(point['point_name']))
        point['in_SECA'] = True if reply_SECA == 'y' else False

    # input if point is working
    for point in points:
        question = 'Is point {} working with ship\'s cranes? (y/n)'
        reply_working = input(
            question.format(point['point_name']))
        point['working'] = True if reply_working == 'y' else False

    # input quantity of idle days at each point
    for point in points:
        point['idle_days'] = int(
            input(
                'Please put quantity of idle days at {}\n'.format(
                    point['point_name'])))

    # input quantity of working days at each point
    for point in points:
        point['working_days'] = int(
            input(
                'Please put quantity of working days at {}\n'.format(
                    point['point_name'])))

    distances = []
    # input distance including SECA zone from each between points
    for i in range(len(points) - 1):
        distances[i]['leg_distance'] = int(
            input(
                'Please put total distance from {} to {}\n, nm'.format(
                    points[i]['point_name'], points[i + 1]['point_name'])))

    # input distance in SECA zone only from each between points
    for i in range(len(points) - 1):
        distances[i]['distance_in_SECA'] = int(
            input(
                'Please put total distance from {} to {}\n, nm'.format(
                    points[i]['point_name'], points[i + 1]['point_name'])))

    # input weather_factor in percent for each distance not in SECA
    for i in range(len(points) - 1):
        request = 'Please put weather factor for distance ' \
            'from {} to {} not in SECA\n'
        points[i]['weather_factor_not_SECA'] = int(
            input(
                request.format(
                    points[i]['point_name'], points[i + 1]['point_name'])))

    # input weather_factor in percent for each distance in SECA
    for i in range(len(points) - 1):
        request = 'Please put weather factor for distance ' + \
            'from {} to {} in SECA\n'
        points[i]['weather_factor_in_SECA'] = int(
            input(
                request.format(
                    points[i]['point_name'], points[i + 1]['point_name'])))

    # calculating optimal speed for any distance
    # bunker_prices = {
    #     'IFO': ifo_price,
    #     'MGO': mgo_price
    # }
    # optimal_speed = optimal_speed_calculation(ship, bunker_prices, hire_rate)

    # adding collected information to calculations dictionary
    calculations['ship'] = ship
    calculations['points'] = points
    calculations['distances'] = distances
    calculations['bunker_prices']['ifo_price'] = ifo_price
    calculations['bunker_prices']['mgo_price'] = mgo_price

    # save data to JSON file BUNKERING_FILE
    append_JSON_file(BUNKERING_FILE, calculations)

    result = 10
    return result

from ships_list.additional_functions.input_functions import input_option
from ships_list.lists.Standard.constants import SHIPS_FILE, \
    BUNKERING_FILE
from ships_list.additional_functions.ship.additional_ship_functions import \
    add_parameter
from ships_list.additional_functions.json_functions import append_JSON_file
from ships_list.additional_functions.optimal_speed \
    import optimal_speed_calculation
from ships_list.additional_functions.bunker.additional_bunker_functions \
    import input_points, add_distance, add_weather_factor


def calculate_bunkers_consumption():
    calculations = {}
    ship = input_option(SHIPS_FILE, 'ships_name', 'ship')

    # check if speed is already in ship's details
    if 'speed' not in ship:
        ship = add_parameter(ship, 'speed')

    # check if consumption is already in ship's details
    if 'consumption' not in ship:
        ship = add_parameter(ship, 'consumption')

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

    # input of IFO and MGO on delivery in mt
    calculations['ship']['bunkers_on_delivery'] = {
        'IFO': int(input('Please put IFO delivery, mt\n')),
        'MGO': int(input('Please put MGO delivery, mt\n'))
    }

    # calculating consumption at points
    # TODO refactor below
    consumption_at_points = {}
    for point in points:
        consumption_at_points[point['point_name']] = {
            'IFO': 1,
            'MGO': 1
        }
    calculations['consumption_at_points'] = consumption_at_points

    # calculating consumption during steaming
    # TODO refactor below
    consumption_during_leg = []
    i = 0
    while i < len(distances):
        consumption_during_leg[i] = {
            'IFO': 1,
            'MGO': 1
        }
        i = i + 1
    calculations['consumption_during_leg'] = consumption_during_leg

    # adding expected quantity of bunkers on each key point

    # adding expected date at each key point

    # save data to JSON file BUNKERING_FILE
    append_JSON_file(BUNKERING_FILE, calculations)

    result = 10
    return result

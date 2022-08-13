from ships_list.additional_functions.input_functions import input_option
from ships_list.lists.Standard.constants import SHIPS_FILE, \
    BUNKERING_FILE
from ships_list.additional_functions.ships_functions import add_parameter
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

    # save data to JSON file BUNKERING_FILE
    append_JSON_file(BUNKERING_FILE, calculations)

    result = 10
    return result

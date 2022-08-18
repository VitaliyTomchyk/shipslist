from ships_list.additional_functions.supporting_functions.input_functions \
    import input_option
from ships_list.lists.Standard.constants import SHIPS_FILE, \
    BUNKERING_FILE
from ships_list.additional_functions.supporting_functions.json_functions \
    import append_JSON_file
from ships_list.additional_functions.optimal_speed \
    import optimal_speed_calculation
from ships_list.additional_functions.bunker.additional_bunker_functions \
    import input_points, add_distance, add_weather_factor, \
    add_consuption_calculations


def calculate_bunkers_consumption(input_information):

    calculations = {}
    ship = input_option(SHIPS_FILE, 'ships_name', 'ship')

    calculations['ship'] = ship

    # input prices of IFO, MGO, hire rate
    bunker_prices = {
        'IFO': int(input('Please put price of IFO, USD\n')),
        'MGO': int(input('Please put price of MGO, USD\n'))
    }
    calculations['bunker_prices'] = bunker_prices

    # input points of route
    points = input_points()
    calculations['points'] = points

    # input distance including SECA zone from each between points
    distances = add_distance(points)

    # input weather factor for each distance
    distances_with_WF = add_weather_factor(distances)
    calculations['distances_with_WF'] = distances_with_WF

    # finding optimal speed
    optimal_speed = optimal_speed_calculation((ship,
                                               calculations['hire_rate']),
                                              bunker_prices)
    print('Optimal speed is \n' + str(optimal_speed))

    # calculating consumption at points and steaming leg
    calculations = add_consuption_calculations(calculations, points)

    calculations['total_duration'] = 1
    # adding expected quantity of bunkers on each key point

    # adding expected date at each key point

    # save data to JSON file BUNKERING_FILE
    append_JSON_file(BUNKERING_FILE, calculations)
    input_information['bunker_consumption'] = calculations

    return input_information

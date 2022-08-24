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
    add_consuption_calculation


def calculate_bunkers_consumption(voyage_info):

    calculation = {}

    # adding ship's details to input information
    calculation['ship'] = input_option(SHIPS_FILE, 'ships_name', 'ship')

    # input prices of IFO, MGO
    bunker_prices = {
        'IFO': int(input('Please put price of IFO, USD\n')),
        'MGO': int(input('Please put price of MGO, USD\n'))
    }
    calculation['bunker_prices'] = bunker_prices

    # input points of route
    points = input_points()
    calculation['points'] = points

    # input distance including SECA zone from each between points
    distances = add_distance(points)

    # input weather factor for each distance
    calculation['distances_with_WF'] = add_weather_factor(distances)

    # finding optimal speed
    optimal_speed = optimal_speed_calculation((calculation['ship'],
                                               calculation['hire_rate']),
                                              bunker_prices)
    print('Optimal speed is \n' + str(optimal_speed))

    # calculating consumption at points and steaming leg
    calculation = add_consuption_calculation(calculation)

    # adding total duration of voyage
    calculation['total_duration'] = calculate_total_duration(calculation)

    # print result of calculation
    read_calculation(calculation)

    # save data to JSON file BUNKERING_FILE
    append_JSON_file(BUNKERING_FILE, calculation)
    voyage_info['bunker_consumption'] = calculation

    return voyage_info


def read_calculation(calculation):
    print('Result of calculation:\n' + str(calculation))


# calculates total duraration of voyage
def calculate_total_duration(voyage_info):
    calculation = voyage_info['bunker_consumption']

    total_duration = 0

    # adding total duration of voyage
    for point in calculation['points']:
        total_duration += point['working_days'] + point['idle_days']
    calculation['total_duration'] = total_duration
    return calculation

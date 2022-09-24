from ships_list.additional_functions.supporting_functions.input_functions \
    import input_option
from ships_list.lists.Standard.constants import SHIPS_FILE, \
    BUNKERING_FILE
from ships_list.additional_functions.supporting_functions.json_functions \
    import append_JSON_file
from ships_list.additional_functions.optimal_speed \
    import optimal_speed_calculation
from ships_list.additional_functions.bunker.additional_bunker_functions \
    import input_points_detailed, add_distance, \
    add_consuption_calculation
from ships_list.additional_functions.bunker.weather.weather_functions \
    import add_weather_factor
from ships_list.additional_functions.supporting_functions.\
    additional_functions import id_generator


def calculate_bunkers_consumption(voyage_info):
    print('\nCalculating bunker consumption.')
    calculation = {'id': id_generator}

    # adding ship's details to input information
    calculation['ship'] = input_option(SHIPS_FILE, 'ships_name', 'ship')

    # input prices of IFO, MGO
    calculation['bunker_prices'] = {
        'IFO': int(input('Please put price of IFO, USD\n')),
        'MGO': int(input('Please put price of MGO, USD\n'))
    }

    # input points of route
    calculation['points'] = input_points_detailed(voyage_info)

    # input distance including SECA zone from each between points
    distances = add_distance(calculation['points'])

    # input weather factor for each distance
    calculation['distances_with_WF'] = add_weather_factor(distances)

    # finding optimal speed
    optimal_speed = optimal_speed_calculation(calculation, voyage_info)
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

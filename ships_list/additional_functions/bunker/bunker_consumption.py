from ships_list.lists.Standard.constants import BUNKERING_FILE
from ships_list.additional_functions.supporting_functions.json_functions \
    import append_JSON_file
from ships_list.additional_functions.voyage.optimal_speed \
    import optimal_speed_selector
from ships_list.additional_functions.bunker.additional_bunker_functions \
    import add_consumption_calculation
from ships_list.additional_functions.bunker.points_function \
    import input_points_detailed
from ships_list.additional_functions.bunker.distances_input \
    import add_distances
from ships_list.additional_functions.supporting_functions.\
    additional_functions import id_generator


def calculate_bunkers_consumption(voyage_info):
    print('\nCalculating bunker consumption.')

    # adding bunker consumption calculation
    calculation = {'id': id_generator()}

    # adding ship's details to input information
    calculation['ship'] = voyage_info['ship']

    # input prices of IFO, MGO
    calculation['bunker_prices'] = {
        'IFO': float(input('Please put price of IFO, USD\n')),
        'MGO': float(input('Please put price of MGO, USD\n'))
    }

    # input points of route
    calculation['points'] = input_points_detailed(voyage_info)

    # input distance including SECA zone from each between points
    calculation['legs'] = add_distances(calculation['points'])

    # finding optimal speed
    calculation['optimal_speed'] = optimal_speed_selector(calculation,
                                                          voyage_info)

    # calculating consumption at points and steaming
    calculation['consumption'] = add_consumption_calculation(calculation)

    # adding total duration of voyage
    calculation['total_duration'] = calculate_total_duration(calculation)

    # print result of calculation
    read_calculation(calculation)

    # save data to JSON file BUNKERING_FILE
    append_JSON_file(calculation, BUNKERING_FILE)

    return calculation


def read_calculation(calculation):
    print('Result of calculation:\n' + str(calculation))


# calculates total duraration of voyage
def calculate_total_duration(voyage_info):

    total_duration = 0
    # adding total duration of voyage
    for point in voyage_info['points']:
        total_duration += point['working_days'] + point['idle_days']

    return total_duration

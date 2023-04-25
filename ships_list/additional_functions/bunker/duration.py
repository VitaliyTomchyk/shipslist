from ships_list.additional_functions.supporting_functions.json_functions \
    import read_JSON_file
from ships_list.lists.Standard.constants import SUPPORTING_FILE
from ships_list.additional_functions.bunker.additional_bunker_functions\
    import vessel_info_extractor


# calculating duration of the leg
def calculate_duration_of_leg(leg, ship):
    distance_in_SECA = float(leg['only_SECA']['distance'])
    distance_not_in_SECA = float(leg['total']['distance'] - distance_in_SECA)

    # collecting weather factors for different distances
    wf_in_SECA = float(leg['only_SECA']['wf'])
    wf_not_in_SECA = float(leg['total']['wf'])

    # calculating speed
    speed_type_in_SECA = leg['only_SECA']['speed']
    speed_type_not_in_SECA = leg['total']['speed']

    # collecting speed from ship's details
    speed_in_SECA = vessel_info_extractor(
        leg, ship, speed_type_in_SECA, 'speed')
    speed_not_in_SECA = vessel_info_extractor(
        leg, ship, speed_type_not_in_SECA, 'speed')

    # calculating duration of the leg
    duration_of_the_leg = {"in_SECA": distance_in_SECA * (1 + wf_in_SECA)
                           / speed_in_SECA / 24,
                           "not_in_SECA": distance_not_in_SECA *
                           (1 + wf_not_in_SECA) / speed_not_in_SECA / 24}

    return duration_of_the_leg


def adding_duration_of_stay(point, total_cargo_quantity):

    # input quantity of days in cargo operation
    if point['point_type'] in ['Load port', 'Discharge port']:
        question = 'Is point {} {} working with ship\'s cranes? (y/n)\n'
        cranes_used = input(question.format(point['point_type'],
                                            point['point_name']))
        point['vessel_cranes_used'] = True if cranes_used == 'y' else False
        point = add_duration_of_cargo_operations(point, total_cargo_quantity)
    else:
        point['working_days'] = 0

    # input quantity of idle days
    # TODO: add refactoring summing idle and working days if needed
    idle_days = input(
        '\nPlease put quantity of idle days at {}\n'.format(
            point['point_name']))
    input_idle_days = 0 if idle_days == '' else float(idle_days)

    point['idle_days'] = input_idle_days

    return point


def add_duration_of_cargo_operations(
        point,
        total_cargo_quantity,
        working_days=None):

    # calculating duration of cargo operations
    laytime_port_terms_multiplier = read_JSON_file(SUPPORTING_FILE)[
        'laytime_port_terms'][point['laytime_port_terms']]
    duration_of_cargo_operations = \
        total_cargo_quantity / point['rate_of_handling'] \
        * laytime_port_terms_multiplier

    # if point is not working with ship's cranes
    if working_days is not None:
        point['working_days'] = 0
        point['idle_days'] = point['idle_days'] + duration_of_cargo_operations
        return point

    # printing point_name and point_type
    print('{} {} is working with ship\'s cranes.'.format(
        point['point_type'] .lower(), point['point_name']))

    # adding cargo quantity for handling in the point
    point['cargo_quantity_for_handling'] = int(input(
        '\nTotal quantity of cargo for handling is:\n{}'.format(
            total_cargo_quantity) +
        '\nPlease put quantity of cargo for handling' +
        ' in {}, mt\n'.format(point['point_name'])))

    # adding rate_of_handling for point
    point['rate_of_handling'] = int(input(
        'Please put rate of handling in {}, mt\n'.format(
            point['point_name'])))

    # collecting laytime_port_terms_multiplier
    base_of_terms = read_JSON_file(SUPPORTING_FILE)['laytime_port_terms']
    multiplier = base_of_terms[point['laytime_port_terms']]

    # input quantity of working days
    duration_of_cargo_operations = round(
        point['cargo_quantity_for_handling'] /
        point['rate_of_handling'] *
        multiplier,
        2)

    if point['vessel_cranes_used']:
        point['working_days'] = duration_of_cargo_operations
    else:
        point['working_days'] = 0
        point['idle_days'] = point['idle_days'] + duration_of_cargo_operations

    return point

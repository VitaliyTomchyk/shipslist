from ships_list.lists.Standard.constants import SUPPORTING_FILE, PORTS_FILE
from ships_list.additional_functions.supporting_functions.input_functions \
    import input_option_from_dict
from ships_list.additional_functions.bunker.point_consumption import \
    point_consumption_calculator
from ships_list.additional_functions.supporting_functions.json_functions \
    import read_JSON_file, append_JSON_file


def add_consuption_calculation(calculations):
    points = calculations['points']

    consumption_at_points = {}
    for point in points:
        consumption_at_points[point['point_name']] = \
            point_consumption_calculator(point, calculations['ship'])

    return calculations


# input points of booking in voyage_info
def input_points_from_booking(voyage_info):
    if voyage_info is None:
        return []

    points = voyage_info['booking_info']['points']
    # adding  duration of port stay point
    for point in points:
        point = adding_duration_of_stay(point, voyage_info['cargo_quantity'])

    return points


# input points of route
def input_points_detailed(voyage_info):

    points = []

    # adding delivery point
    point = add_point('Delivery point', point_in_SECA=False)
    points.insert(0, point)

    # input points from booking
    points += input_points_from_booking(voyage_info)

    # adding delivery point
    points += add_point('Redelivery point', point_in_SECA=False)

    # input points from user
    while True:

        # ask if user wants to add point
        reply = input("Do you want to add new point? (y/n)\n")
        if reply == 'y':
            point = add_point()

            # adding points with point
            points.append(point)

        # checker for mandatory points
        if checker_for_mandatory_points(points) is False:
            points.append(add_point())
        break

    # # checker for summ of cargo
    # checker_for_summ_of_cargo(points, voyage_info['cargo_quantity'])

    return points


# checker if summ at load port and discharge port is equal to total cargo
def checker_for_summ_of_cargo(points, total_cargo_quantity):

    summ = 0
    for point in points:
        if point['point_type'] in ['Load port', 'Discharge port']:
            summ += point['cargo_quantity_for_handling']

    if summ / 2 != total_cargo_quantity:
        print('\nSumm of cargo at load and discharge ports is not equal to' +
              ' total cargo quantity.\n')
        return False
    return True


def add_point(point_type=None, total_cargo_quantity=None, point_in_SECA=None):
    point = {}

    # adding point parameter 'point_type'
    point['point_type'] = point_type if point_type is not None \
        else input_option_from_dict(SUPPORTING_FILE,
                                    'point_types',
                                    'point type')

    print('\nYou are adding {} to voyage.'.format(point['point_type'.lower()]))

    # adding point parameter 'point_name'
    point['point_name'] = input('Please put name of point\n')

    # adding point parameter 'in_SECA'
    if point_in_SECA is None:
        point['in_SECA'] = check_point_in_SECA(point['point_name'])
    else:
        point['in_SECA'] = point_in_SECA

    # adding point parameter duration of stay
    if point['point_type'] in ['Load port', 'Discharge port']:
        point['laytime_port_terms'] = input_option_from_dict(
            SUPPORTING_FILE, 'laytime_port_terms', 'laytime port terms')

    # adding duration of port stay to load and disch point
    return adding_duration_of_stay(point, total_cargo_quantity)


def check_point_in_SECA(point_name):
    # checking if point is in PORT_FILE
    ports_in_db = list(filter(lambda x: x['name'] == point_name,
                              read_JSON_file(PORTS_FILE)))

    if point_name in ports_in_db:
        return ports_in_db[point_name]['in_SECA']

    reply = input('Is point {} in SECA zone? (y/n)\n'.format(point_name))
    result = True if reply == 'y' else False

    # saving port to port list
    append_JSON_file({'name': point_name, 'in_SECA': result}, PORTS_FILE)
    return result


def checker_for_mandatory_points(points):
    set_of_points_types = set([x['point_type'] for x in points])
    list_of_mandatory_types = ['Load port', 'Discharge port',
                               'Delivery point', 'Redelivery point']
    for mandatory_type in list_of_mandatory_types:
        if mandatory_type not in set_of_points_types:
            print('\nPlease put {}.\n'.format(mandatory_type))
            return False
    return True


def add_working_days(point, total_cargo_quantity):

    # printing point_name and point_type
    print('{} {} is working with ship\'s cranes.'.format(point['point_type'],
                                                         point['point_name']))

    # adding cargo quantity for handling in the point
    point['cargo_quantity_for_handling'] = int(input(
        '\nTotal quantity of cargo for handling at {} is:\n'.format(
            point['point_name']) +
        '\nPlease put quantity of cargo for handling' +
        ' in {}, mt\n'.format(total_cargo_quantity)))

    # adding rate_of_handling for point
    point['rate_of_handling'] = int(input(
        'Please put rate of handling in {}, mt\n'.format(
            point['point_name'])))

    base_of_terms = read_JSON_file(SUPPORTING_FILE)['laytime_port_terms']

    multiplier = base_of_terms[point['laytime_port_terms']]
    # input quantity of working days
    point['working_days'] = round(
        point['cargo_quantity_for_handling'] /
        point['rate_of_handling'] *
        multiplier,
        2)

    return point


def adding_duration_of_stay(point, total_cargo_quantity):

    # input quantity of working days
    if point['point_type'] in ['Load port', 'Discharge port']:
        question = 'Is point {} working with ship\'s cranes? (y/n)\n'
        reply_if_working = input(question.format(point['point_name']))

        if reply_if_working == 'y':
            point = add_working_days(point,
                                     total_cargo_quantity)

    # input quantity of idle days
    point['idle_days'] = int(
        input(
            '\nPlease put quantity of idle days at {}\n'.format(
                point['point_name'])))

    return point

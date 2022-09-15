from ships_list.additional_functions.supporting_functions.additional_functions\
    import id_generator, list_to_string
from ships_list.additional_functions.supporting_functions.json_functions \
    import read_JSON_file
from ships_list.lists.Standard.constants import SUPPORTING_FILE, BOOKINGS_FILE
from ships_list.additional_functions.supporting_functions.input_functions \
    import input_option_from_dict


# function shows short version of booking details for all
# bookings
def input_booking_short():
    bookings = read_JSON_file(BOOKINGS_FILE)
    for i, booking in enumerate(bookings):
        print('\nBooking number {}\n'.format(i + 1))
        print(read_booking_details(booking))
    option = bookings[int(input('Please input booking number to read\n')) - 1]
    print('You have chosen following booking:\n{}'.format(
        read_booking_details(option)))
    return option


def booking_details_collector():
    result = {'id': id_generator(),
              'name_of_cargo': input('\nPlease input cargo name\n'),
              'cargo_quantity': input('\nPlease input cargo quantity, mt\n'),
              'allowance_of_cargo': input('\nPlease input allowance, %\n'),
              'points': input_points_short(),
              'commission': input_commissions_short(),
              'lay_can': input('\nPlease input lay can in following ' +
                               'format: "20.12.22"\n'),
              'account': input('\nPlease input account name\n'),
              'comments': input('\nPlease input comments\n')
              }
    return result


def input_commissions_short():
    # input points
    commissions = []

    quantity_of_points = input('Please input quantity of commissions\n')

    for i in range(int(quantity_of_points)):
        commission = {}
        print(
            'Please put type of commission type number {} from {}\n'.format(
                i + 1, quantity_of_points))
        commission['type'] = input_option_from_dict(SUPPORTING_FILE,
                                                    'commission_types',
                                                    'commission type')

        commission['value'] = float(
            input(
                'Please put % of {} '.format(
                    commission['type']) +
                "commission number {} of {}, in format \"2.5\"\n".format(
                    i +
                    1,
                    quantity_of_points)))
        commissions.append(commission)

    return commissions


def input_points_short():
    # input points
    points = input_point_short('Load port') + \
        input_point_short('Discharge port')
    return points


def input_point_short(input_point_type):
    point_type = input_point_type.lower()
    points = []

    quantity_of_points = input(
        'Please input QUANTITY of {}s\n'.format(point_type))

    for i in range(int(quantity_of_points)):
        point = {'point_type': point_type}

        # adding point parameter 'point_name'
        point['point_name'] = input(
            'Please put NAME of {} number {} from {}\n'.format(
                point_type, i + 1, quantity_of_points))

        # adding point parameter 'in_SECA'
        in_SECA = input(
            'Is point {} in SECA zone? (y/n)\n'.format(point['point_name']))
        point['in_SECA'] = True if in_SECA == 'y' else False

        # adding point laytime term
        point['laytime_port_terms'] = input_option_from_dict(
            SUPPORTING_FILE, 'laytime_port_terms',
            'laytime port terms')

        points.append(point)

    return points


def booking_selector():
    bookings = read_JSON_file(BOOKINGS_FILE)
    for i, booking in enumerate(bookings):
        print('\nBooking number {}\n'.format(i + 1))
        print(read_booking_details(booking))
    option = bookings[int(input('Please input booking number to read\n')) - 1]
    print('You have chosen following booking:\n{}'.format(
        read_booking_details(option)))
    return option


def booking_finder(booking_id):
    if booking_id is None:
        return booking_selector()

    bookings = read_JSON_file(BOOKINGS_FILE)
    return [booking for booking in bookings
            if booking['id'] == booking_id][0]


def read_booking_details(booking_id=None):

    the_booking = booking_finder(booking_id)

    account = 'Account: {}'.format(str(the_booking['account']))
    cargo_line = 'Booking for {} mt MOL {}% of {}'.format(
        the_booking['cargo_quantity'],
        the_booking['allowance_of_cargo'],
        the_booking['name_of_cargo'])

    # collecting ports
    ports = [(x['point_name'], x['point_type']) for x in the_booking['points']]

    load_ports = list(filter(lambda x: x[1] == 'Load port', ports))
    discharge_ports = list(filter(lambda x: x[1] == 'Discharge port', ports))

    destination_line = 'From {} to {}'.format(list_to_string(load_ports),
                                              list_to_string(discharge_ports))

    lay_can_line = 'Lay can: {}'.format(the_booking['lay_can'])
    commission_line = 'Commissions: {}'.format(
        list_to_string(the_booking['commission']))

    result = '{}\n{}\n{}\n{}\n{}\n'.format(
        account,
        cargo_line,
        destination_line,
        lay_can_line,
        commission_line)

    return result


# function returns short booking details for list of bookings
def read_booking_details_list(bookings):
    result = []
    for booking in bookings:
        result.append(read_booking_details(booking))
    return result

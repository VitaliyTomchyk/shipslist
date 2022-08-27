from ships_list.additional_functions.supporting_functions.additional_functions\
    import id_generator, list_to_string
from ships_list.lists.Standard.constants import SUPPORTING_FILE
from ships_list.additional_functions.supporting_functions.input_functions \
    import input_option_from_dict


def booking_details_collector():
    result = {'id': id_generator(),
              'name_of_cargo': input('\nPlease input cargo name\n'),
              'cargo_quantity': input('\nPlease input quantity, mt\n'),
              'allowance_of_cargo': input('\nPlease input allowance, %\n'),
              'points': input_points_short(),
              'commission': input_commissions_short(),
              'lay_can': input('\nPlease input lay can in following ' +
                               'format: "20.12.22"\n'),
              }
    return result


def input_commissions_short():
    # input points
    commissions = []

    quantity_of_points = input('Please input quantity of commissions\n')

    for i in range(int(quantity_of_points)):
        commission = {}
        # adding point parameter 'point_name'
        commission['type'] = input(
            'Please put name of commission type number {} from {}\n'.format(
                i + 1, quantity_of_points))

        commission['value'] = input(
            'Please put % of {} '.format(commission['type']) +
            "commission number {} of {}\n".format(i + 1,
                                                  quantity_of_points))
        commissions.append(commission)

    return commissions


def input_points_short():
    # input points
    points = input_point_short('Load port') + \
        input_point_short('Discharge port')
    return points


def input_point_short(point_type):
    points = []

    quantity_of_points = input(
        'Please input quantity of {} ports\n'.format(point_type))

    for i in range(int(quantity_of_points)):
        point = {'point_type': point_type}
        # adding point parameter 'point_name'
        point['point_name'] = input(
            'Please put name of {} port number {}\n'.format(point_type, i + 1))

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


def read_booking_details(the_booking):

    cargo_line = '\nBooking for {} mt MOL {}% of {}'.format(
        the_booking['cargo_quantity'],
        the_booking['allowance_of_cargo'],
        the_booking['name_of_cargo'])

    load_ports = [x['point_name'] for x in the_booking['points']['load']]
    discharge_ports = [x['point_name']
                       for x in the_booking['points']['discharge']]

    destination_line = 'From {} to {}'.format(list_to_string(load_ports),
                                              list_to_string(discharge_ports))

    lay_can_line = 'Lay can: {}'.format(the_booking['lay_can'])
    commission_line = 'Commissions: {}'.format(
        list_to_string(the_booking['commission']))
    result = '{}\n{}\n{}\n{}\n'.format(
        cargo_line,
        destination_line,
        lay_can_line,
        commission_line)

    return result

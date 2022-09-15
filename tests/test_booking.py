from ships_list.lists.Standard.constants import BOOKINGS_FILE
from tests.universal_test import standard_test_of_input_function
from ships_list.additional_functions.booking.booking_functions import \
    add_booking, read_booking, remove_booking
from ships_list.lists.Standard.constants import BOOKINGS_FILE


# def test_add_booking():

#     expected_result ='''Account: Test_account
# Booking for 1000 mt MOL 1% of grain
# From  to 
# Lay can: 20.11.22
# Commissions: {'type': 'address', 'value': 2.5}\n'''

#     standard_test_of_input_function(add_booking,
#     ['Test_account', 'grain', '1000', '1', '1', 'Odessa', 'n', '1', 
#      '1', 'Nikolayev',
#     'n', '2', '1', '1', '2.5', '20.11.22', 'test comment'],
#     [             'Booking will be added.',
#              '\n'
#              'Please input account name\n',
#              '\n'
#              'Please input cargo name\n',
#              '\n'
#              'Please input cargo quantity, mt\n',
#              '\n'
#              'Please input allowance, %\n',
#              '\n'
#              'Please input QUANTITY of load ports\n',
#              'Please put NAME of load port number 1 from 1\n',
#              'Is point Odessa in SECA zone? (y/n)\n',
#              '\n'
#              'Please put laytime port terms from following list.',
#              'Choose number from options of laytime_port_terms.',
#              '1. shinc\n'
#              '2. shex\n'
#              '3. fshex\n',
#              '',
#              '\n'
#              'Please input QUANTITY of discharge ports\n',
#              'Please put NAME of discharge port number 1 from 1\n',
#              'Is point Nikolayev in SECA zone? (y/n)\n',
#              '\n'
#              'Please put laytime port terms from following list.',
#              'Choose number from options of laytime_port_terms.',
#              '1. shinc\n'
#              '2. shex\n'
#              '3. fshex\n',
#              '',
#              'Please input quantity of commissions\n',
#              'Please put type of commission type number 1 from 1\n',
#              '\n'
#              'Please put commission type from following list.',
#              'Choose number from options of commission_types.',
#              '1. address\n'
#              "2. broker's\n"
#              '3. other\n',
#              '',
#              'Please put % of address commission number 1 of 1, in format "2.5"\n',
#              '\n'
#              'Please input lay can in following format: "20.12.22"\n',
#              '\n'
#              'Please input comments\n',
#              '\n'
#              '\n'
#              'Booking was created with below details:\n',
#              expected_result],
#     [{'account': 'Test_account',
#                            'allowance_of_cargo': '1',
#                            'cargo_quantity': '1000',
#                            'comments': 'test comment',
#                            'commission': [{'type': 'address',
#                                            'value': 2.5}],
#                            'id': 255,
#                            'lay_can': '20.11.22',
#                            'name_of_cargo': 'grain',
#                            'points': [{'in_SECA': False,
#                                        'laytime_port_terms': 'shinc',
#                                        'point_name': 'Odessa',
#                                        'point_type': 'load port'},
#                                       {'in_SECA': False,
#                                        'laytime_port_terms': 'shex',
#                                        'point_name': 'Nikolayev',
#                                        'point_type': 'discharge port'}]}],
#     BOOKINGS_FILE)
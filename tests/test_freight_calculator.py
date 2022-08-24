# from ships_list.additional_functions.ship.ships_functions import add_ship, \
#     read_ship
# from tests.tug_test_base import set_keyboard_input, get_display_output
# from ships_list.lists.Standard.constants import SHIPS_FILE, \
#     EXPECTED_OUTPUT_NEW_SHIP_FILE
# # , HELP_FILE
# from ships_list.additional_functions.supporting_functions.json_functions \
#     import read_JSON_file, write_JSON_file
# from datetime import datetime


# def test_freight_calculattor():
#     # copy old list
#     old_version = read_JSON_file(SHIPS_FILE)

#     # running function and collecting result of function
#     set_keyboard_input(['POpy'] + list(range(1, 12)))
#     add_ship()
#     output = get_display_output()
#     updated_version = read_JSON_file(SHIPS_FILE)

#     # finding difference
#     diff =  [x for x in updated_version if x not in old_version]

#     # expected values
#     expected_diff = [{
#         'ships_name': "POPY",
#         'IMO': 1,
#         'additional_consumption': {'port_stay': 10,
#                                    'steaming': 11},
#         'speed': {'laden_full_speed': 2,
#                   'laden_eco_speed': 3,
#                   'ballast_full_speed': 4,
#                   'ballast_eco_speed': 5,
#                   'date_of_update': '{:%Y-%m-%d}'.format(datetime.now())},
#         'consumption': {
#                   'laden_full_consumption': 6,
#                   'laden_eco_consumption': 7,
#                   'ballast_full_consumption': 8,
#                   'ballast_eco_consumption': 9,
#                   'date_of_update': '{:%Y-%m-%d}'.format(datetime.now())}}]
#     expected_output_file = EXPECTED_OUTPUT_NEW_SHIP_FILE
#     with open(expected_output_file, 'r') as f:
#         expected_output = f.read()
    
#     # writing back prev version of information
#     write_JSON_file(SHIPS_FILE, old_version)

#     # checkng result against expectations
#     assert output == expected_output
#     assert diff == expected_diff
from ships_list.additional_functions.ship.ships_functions import add_ship, \
    read_ship
from tests.tug_test_base import set_keyboard_input, get_display_output
from ships_list.lists.Standard.constants import SHIPS_FILE
# , HELP_FILE
from ships_list.additional_functions.supporting_functions.json_functions \
    import read_JSON_file, write_JSON_file
from datetime import datetime


# def test_add_ship():
#     proforma_input(add_ship,
#                 ['DISCOVERY', '1', '1', '2', '3', '4', '5', '6', '7', '8'],
#                 ['Please enter IMO of the ship',
#                 'Ship DISCOVERY has been added.\n'],
#                 '',
#                 SHIPS_FILE)

def test_add_not_existing_ship():
    # copy old list
    old_version = read_JSON_file(SHIPS_FILE)

    # running function and collecting result of function
    set_keyboard_input(['POpy'] + list(range(1, 12)))
    add_ship()
    output = get_display_output()
    updated_version = read_JSON_file(SHIPS_FILE)

    # finding difference
    diff =  [x for x in updated_version if x not in old_version]

    # expected values
    expected_diff = [{
        'ships_name': "POPY",
        'IMO': 1,
        'additional_consumption': {'port_stay': 10,
                                   'steaming': 11},
        'speed': {'laden_full_speed': 2,
                  'laden_eco_speed': 3,
                  'ballast_full_speed': 4,
                  'ballast_eco_speed': 5,
                  'date_of_update': '{:%Y-%m-%d}'.format(datetime.now())},
        'consumption': {
                  'laden_full_consumption': 6,
                  'laden_eco_consumption': 7,
                  'ballast_full_consumption': 8,
                  'ballast_eco_consumption': 9,
                  'date_of_update': '{:%Y-%m-%d}'.format(datetime.now())}}]
    
    expected_output = ['Please enter ship\'s name\n',
                      'Please enter IMO of the ship\n',

                      '\nPlease add full laden speed of the ship, kn\n',
                      '\nPlease add eco laden speed of the ship, kn\n',
                      '\nPlease add full ballast speed of the ship, kn\n',
                      '\nPlease add eco ballast speed of the ship, kn\n',

                      '\nPlease add full laden consumption of the ship, mt/day\n',
                      '\nPlease add eco laden consumption of the ship, mt/day\n',
                      '\nPlease add full ballast consumption of the ship, mt/day\n',
                      '\nPlease add eco ballast consumption of the ship, mt/day\n',

                      '\nPlease add additional consumption during port_stay, mt of MGO\n',
                      '\nPlease add additional consumption during steaming, mt of MGO\n',

                      'Ship POPY has been added.\n']
    
    # writing back prev version of information
    write_JSON_file(SHIPS_FILE, old_version)

    # checkng result against expectations
    assert output == expected_output
    assert diff == expected_diff


def test_add_existing_ship():
    # copy old list
    old_version = read_JSON_file(SHIPS_FILE)
    
    existing_ships_name = old_version[0]['ships_name']
    existing_IMO = old_version[0]['IMO']

    # running function and collecting result
    set_keyboard_input([existing_ships_name, existing_IMO])
    add_ship()
    output = get_display_output()
    updated_version = read_JSON_file(SHIPS_FILE)

    # finding difference
    diff =  [x for x in updated_version if x not in old_version]

    # expected values
    expected_diff = []
    expected_output = ['Please enter ship\'s name\n',
                      'Please enter IMO of the ship\n',
                      'IMO is already in list']
    
    # writing back prev version of information
    write_JSON_file(SHIPS_FILE, old_version)

    # checkng result against expectations
    assert output == expected_output
    assert diff == expected_diff


def test_read_existing_ship():
    # copy old list
    old_version = read_JSON_file(SHIPS_FILE)

    # running function and collecting result
    name = 'TESTO'
    set_keyboard_input([name] + list(range(0, 11)))
    add_ship() 

    # running function and collecting result
    set_keyboard_input([name])
    read_ship()
    output = get_display_output()

    expected_output = ["\nPlease add ship's name\n",
                       '\n'
                       'ships_name: TESTO\n'
                       'IMO: 0\n'
                       "speed: {'laden_full_speed': 1, " + \
                               "'laden_eco_speed': 2, " + \
                               "'ballast_full_speed': 3, " + \
                               "'ballast_eco_speed': 4, " + \
                               "'date_of_update': '"+ \
                               "{:%Y-%m-%d}".format(datetime.now()) +"'}\n" + \
                       "consumption: {'laden_full_consumption': 5, " + \
                                     "'laden_eco_consumption': 6, " + \
                                     "'ballast_full_consumption': 7, " + \
                                     "'ballast_eco_consumption': 8, " + \
                                     "'date_of_update': '" + \
                                     "{:%Y-%m-%d}".format(datetime.now()) + \
                                        "'}\n" + \
                       "additional_consumption: {'port_stay': 9, 'steaming': 10}\n",]
    # writing back prev version of information
    write_JSON_file(SHIPS_FILE, old_version)

    # checkng result against expectations
    assert output == expected_output


def test_read_missing_ship():

    # running function and collecting result
    set_keyboard_input(['KO'])
    read_ship()
    output = get_display_output()

    expected_output = ["\nPlease add ship's name\n",
                       'Ship KO is missing in list of ships.']
    
    # checkng result against expectations
    assert output == expected_output


# def test_h():
#     with open(HELP_FILE, 'r') as f:
#         expected_output = f.read()
#     ouput = ships_list -h
#     assert output == expected_output


# def test_read_not_existing_ship():

#     # running function and collecting result
#     set_keyboard_input(['B'])
#     read_ship()
#     output = get_display_output()

#     expected_output = ['\nPlease add ship\'s name\n',
#                        'Ship B is missing in list of ships.']
    
#     # checkng result against expectations
#     assert output == expected_output

from ships_list.additional_functions.ships_functions import add_ship, read_ship
from tests.tug_test_base import set_keyboard_input, get_display_output
from ships_list.lists.Standard.constants import SHIPS_FILE
from ships_list.additional_functions.json_functions import read_JSON_file, write_JSON_file
from datetime import datetime
from tests.file import proforma_input


# def test_add_ship():
#     proforma_input(add_ship,
#                 ['DISCOVERY', '1', '1', '2', '3', '4', '5', '6', '7', '8'],
#                 ['Ship adding function is activated\nPlease enter name of the ship',
#                 'Please enter IMO of the ship',
#                 'Ship DISCOVERY has been added.\n'],
#                 '',
#                 SHIPS_FILE)

def test_add_not_existing_ship():
    # copy old list
    old_version = read_JSON_file(SHIPS_FILE)


    # running function and collecting result
    set_keyboard_input(['POpy', '4', '14', '1', '1', '1', '14', '1', '1', '1'])
    add_ship()
    output = get_display_output()
    updated_version = read_JSON_file(SHIPS_FILE)

    # finding difference
    diff =  [x for x in updated_version if x not in old_version]

    # expected values
    expected_diff = [{
        'ships_name': "POPY",
        'IMO': 4,
        'consumption': {'ballast_eco_consumption': 1,
                  'ballast_full_consumption': 1,
                  'date_of_update': '{:%Y-%m-%d}'.format(datetime.now()),
                  'laden_eco_consumption': 1,
                  'laden_full_consumption': 14},
        'ships_name': 'POPY',
        'speed': {'ballast_eco_speed': 1,
                  'ballast_full_speed': 1,
                  'date_of_update': '{:%Y-%m-%d}'.format(datetime.now()),
                  'laden_eco_speed': 1,
                  'laden_full_speed': 14}}]
    
    expected_output = ['\nShip adding function is activated\n' + \
                      'Please enter name of the ship\n',
                      'Please enter IMO of the ship\n',
                      '\nPlease add full laden speed of the ship, kn\n',
                      'Please add eco ballast speed of the ship, kn\n',
                      'Please add full ballast speed of the ship, kn\n',
                      'Please add eco ballast speed of the ship, kn\n',
                      '\nPlease add full laden consumption of the ship, mt/day\n',
                      'Please add eco ballast consumption of the ship, mt/day\n',
                      'Please add full ballast consumption of the ship, mt/day\n',
                      'Please add eco ballast consumption of the ship, mt/day\n',
                      'Ship POPY has been added.\n']
    
    # writing back prev version of information
    write_JSON_file(SHIPS_FILE, old_version)

    # checkng result against expectations
    assert output == expected_output
    assert diff == expected_diff


def test_add_existing_ship():
    # copy old list
    old_version = read_JSON_file(SHIPS_FILE)
    
    existing_ship = old_version[0]['ships_name']

    # running function and collecting result
    set_keyboard_input([existing_ship, '4'])
    add_ship()
    output = get_display_output()
    updated_version = read_JSON_file(SHIPS_FILE)

    # finding difference
    diff =  [x for x in updated_version if x not in old_version]

    # expected values
    expected_diff = []
    expected_output = ['\nShip adding function is activated\n' + \
                      'Please enter name of the ship\n',
                      'Please enter IMO of the ship\n',
                      'Ship with this name and IMO is already in list, ' + \
                      'therefore, it will not be added again.']
    
    # writing back prev version of information
    write_JSON_file(SHIPS_FILE, old_version)

    # checkng result against expectations
    assert output == expected_output
    assert diff == expected_diff

def test_read_existing_ship():
    name = 'TEST'
    # running function and collecting result
    set_keyboard_input([name])
    read_ship()
    output = get_display_output()

    expected_output = ["\nPlease add ship's name\n",
                       '\n'
                       'ships_name: TEST\n'
                       'IMO: 1\n'
                       "speed: {'laden_full_speed': 1, 'laden_eco_speed':" + \
                       " 1, 'ballast_full_speed': "
                       "1, 'ballast_eco_speed': 1, 'date_of_update':" + \
                       " '2022-08-12'}\n"
                       "consumption: {'laden_full_consumption': 1," + \
                       " 'laden_eco_consumption': 1, "
                       "'ballast_full_consumption': 1," + \
                       " 'ballast_eco_consumption': 1, "
                       "'date_of_update': " + \
                       "'{:%Y-%m-%d}'".format(datetime.now()) + "}\n"]
    
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


# def test_read_not_existing_ship():

#     # running function and collecting result
#     set_keyboard_input(['B'])
#     read_ship()
#     output = get_display_output()

#     expected_output = ['\nPlease add ship\'s name\n',
#                        'Ship B is missing in list of ships.']
    
#     # checkng result against expectations
#     assert output == expected_output

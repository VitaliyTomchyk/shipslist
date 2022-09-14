from ships_list.additional_functions.supporting_functions.additional_functions\
    import list_to_string_with_breaks
from ships_list.lists.Standard.constants import BUNKERING_FILE
from ships_list.additional_functions.ship.ships_functions import add_ship, \
    read_ship, remove_ship
from tests.tug_test_base import set_keyboard_input, get_display_output
from ships_list.lists.Standard.constants import BUNKERING_FILE, \
    EXPECTED_OUTPUT_NEW_SHIP_FILE, SHIPS_FILE
from ships_list.additional_functions.supporting_functions.json_functions \
    import read_JSON_file, write_JSON_file
from tests.universal_test import standard_test_of_input_function, \
    standard_test_of_read_function
from datetime import datetime
from tests.fixtures.expected_output_new_ship import fixture_output, \
    fixture_diff, fixture_input


def test_add_not_existing_ship():

    standard_test_of_input_function(add_ship,
                fixture_input,
                fixture_output,
                fixture_diff,
                SHIPS_FILE)


def test_add_existing_ship():
    
    # copy old list
    old_version = read_JSON_file(SHIPS_FILE)

    # check if ships exist  in list
    if len(old_version) == 0:
        return
    
    input_of_function = [old_version[0]['ships_name'],
                         old_version[0]['IMO']]

    standard_test_of_input_function(add_ship,
                input_of_function,
                ['Please enter ship\'s name\n',
                 'Please enter IMO of the ship\n',
                 'IMO is already in list'],
                [],
                SHIPS_FILE)


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

    expected_output = [
             '\n'
             "Please add ship's name\n",
             'ships_name: TESTO\n'
             'IMO: 0\n'
             'speed:\n'
             'laden_full_speed: 1\n'
             'laden_eco_speed: 2\n'
             'ballast_full_speed: 3\n'
             'ballast_eco_speed: 4\n'
             'date_of_update: '+ "{:%Y-%m-%d}".format(datetime.now()) +'\n'
             'consumption:\n'
             'laden_full_consumption: 5\n'
             'laden_eco_consumption: 6\n'
             'ballast_full_consumption: 7\n'
             'ballast_eco_consumption: 8\n'
             'date_of_update: '+ "{:%Y-%m-%d}".format(datetime.now()) +'\n'
             'additional_consumption:\n'
             'port_stay: 9\n'
             'steaming: 10\n',
           ]
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
                       '\nShip KO is missing in list of ships.']
    
    # checkng result against expectations
    assert output == expected_output


# test adding and then deleting ship
def test_delete_ship():
    # copy old list
    old_version = read_JSON_file(SHIPS_FILE)

    # running function and collecting result
    set_keyboard_input(['TESTO'] + list(range(0, 11)))
    add_ship()
    output = get_display_output()

    set_keyboard_input(['TESTO'])
    remove_ship()
    output = output + get_display_output()
    str_with_ships = str(list_to_string_with_breaks([x['ships_name']
                                                    for x in old_version] + \
                                                    ['TESTO']))
    # expected output
    expected_output = ["Please enter ship's name\n",      
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
                       'Ship TESTO has been added.\n',
                       '\nList of ships:\n' + str_with_ships,
                       "Please put ship's name you want to remove.",
                       '\nShip TESTO was removed.\n']

    new_version = read_JSON_file(SHIPS_FILE)
    
    # writing back prev version of information
    write_JSON_file(SHIPS_FILE, old_version)

    # checkng result against expectations
    assert output == expected_output
    assert old_version == new_version


# testing deleting missing ship
def test_delete_missing_ship():
    # copy old list
    old_version = read_JSON_file(SHIPS_FILE)

    # running function and collecting result
    set_keyboard_input(['KO'])
    remove_ship()
    output = get_display_output()
    str_with_ships = str(list_to_string_with_breaks([x['ships_name']
                                                    for x in old_version]))

    expected_output = ['\nList of ships:\n' + str_with_ships,
                       "Please put ship's name you want to remove.",
                       '\nShip KO was not found']
    
    # checkng result against expectations
    assert output == expected_output
    assert old_version == read_JSON_file(SHIPS_FILE)

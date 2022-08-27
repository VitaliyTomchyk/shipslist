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
    output = str(get_display_output())
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
    expected_output = str(["Please enter ship's name\n",      
                      'Please enter IMO of the ship\n',      
                      '\nPlease add full laden speed of the ship, kn\n',      
                      '\nPlease add eco laden speed of the ship, kn\n',      
                      '\nPlease add full ballast speed of the ship, kn\n',      
                      '\nPlease add eco ballast speed of the ship, kn\n',      
                      '\nPlease add full laden consumption of the ship,' +  
                      ' mt/day\n',      
                      '\nPlease add eco laden consumption of the ship,' + 
                      ' mt/day\n',      
                      '\nPlease add full ballast consumption of the ship,' +  
                      ' mt/day\n',      
                      '\nPlease add eco ballast consumption of the ship,' +  
                      ' mt/day\n',      
                      '\nPlease add additional consumption during' +  
                      ' port_stay, mt of MGO\n',      
                      '\nPlease add additional consumption during steaming,' +  
                      ' mt of MGO\n',      
                      'Ship POPY has been added.\n'])
    
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

    # expected difference is empty list, as no new ship has been added
    expected_diff = []

    # expected output
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

# # def test_h():
# #     with open(HELP_FILE, 'r') as f:
# #         expected_output = f.read()
# #     ouput = ships_list -h
# #     assert output == expected_output

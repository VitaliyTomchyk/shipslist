from ships_list.additional_functions.ships_functions import add_ship, read_ship
from tests.tug_test_base import set_keyboard_input, get_display_output
from ships_list.lists.Standard.constats import SHIPS_FILE
from ships_list.additional_functions.json_functions \
    import read_JSON_file, write_JSON_file


def test_add_not_existing_ship():
    # copy old list
    old_version = read_JSON_file(SHIPS_FILE)

    # running function and collecting result
    set_keyboard_input(['POpy', '4'])
    add_ship()
    output = get_display_output()
    updated_version = read_JSON_file(SHIPS_FILE)

    # finding difference
    diff =  [x for x in updated_version if x not in old_version]

    # expected values
    expected_diff = [
    {
        "ships_name": "POPY",
        "IMO": 4,
        "has_tasks": False,
        "ships_list": None,
        "number_of_tasks": 0
    }]
    expected_output = ['\nShip adding function is activated\n' + \
                      'Please enter name of the ship\n',
                      'Please enter IMO of the ship\n',
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

    # running function and collecting result
    set_keyboard_input(['BEDA'])
    read_ship()
    output = get_display_output()

    expected_output = ['\nPlease add ship\'s name\n',
                       '\nships_name: BEDA\nIMO: 2743888347293827411\n' + \
                       'has_tasks: True\nships_list: None\n' + \
                       'number_of_tasks: 1\n']
    
    # checkng result against expectations
    assert output == expected_output


def test_read_not_existing_ship():

    # running function and collecting result
    set_keyboard_input(['B'])
    read_ship()
    output = get_display_output()

    expected_output = ['\nPlease add ship\'s name\n',
                       'Ship B is missing in list of ships.']
    
    # checkng result against expectations
    assert output == expected_output

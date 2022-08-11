from ships_list.additional_functions.json_functions import read_JSON_file, \
    write_JSON_file
from ships_list.lists.Standard.constants import TASKS_FILE, SHIPS_FILE
from tests.tug_test_base import set_keyboard_input, get_display_output


def proforma_input(function, input_info, expected_output,
                           expected_diff, file):

    # copy old list
    old_version = read_JSON_file(file)

    # running function and collecting result
    print('mark1')
    set_keyboard_input(input_info)
    function()
    output = get_display_output()
    print('mark2')
    updated_version = read_JSON_file(file)
    print('mark3')
    # finding difference
    diff =  [x for x in updated_version if x not in old_version]
  

    # writing back prev version of information
    write_JSON_file(TASKS_FILE, old_version)

    # checkng result against expectations
    assert output == expected_output
    assert diff == expected_diff
    assert output == expected_output


def standard_test_of_read_function(function, input, expected_output):

    # running function and collecting result
    set_keyboard_input(input)
    function()
    output = get_display_output()

    # checkng result against expectations
    assert output == expected_output
    assert output == expected_output


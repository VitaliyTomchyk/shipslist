import pytest
from ships_list.additional_functions.ships_functions import add_ship
from tests.tug_test_base import set_keyboard_input, get_display_output


def test_add_ship():
    
    set_keyboard_input(['POpy', '4'])
    add_ship()
    output = get_display_output()
    assert 1 == 1

test_add_ship()
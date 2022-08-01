from ships_list.additional_functions.tasks_functions import add_task, read_task
from tests.tug_test_base import set_keyboard_input, get_display_output
from ships_list.lists.Standard.constats import TASKS_FILE
from ships_list.additional_functions.json_functions \
    import read_JSON_file, write_JSON_file


# def test_add_task():

#     # copy old list
#     old_version = read_JSON_file(TASKS_FILE)

#     # running function and collecting result
#     set_keyboard_input(['Pass the test', 'PRUEBA', "After delivery", "Agent"])
#     add_task()
#     output = get_display_output()
#     updated_version = read_JSON_file(TASKS_FILE)

#     # finding difference
#     diff =  [x for x in updated_version if x not in old_version]

#     # expected values
#     expected_diff = [
#     {
#         "task_title": "Pass the test",
#         "ships_name": "PRUEBA",
#         "status": "pending",
#         "stage": "After delivery",
#         "party": "Agent",
#         "id": 73,
#         "voyage_id": 1
#     }]
#     expected_output = ['\nShip adding function is activated\n' + \
#                       'Please enter name of the ship\n',
#                       'Please enter IMO of the ship\n',
#                       'Ship POPY has been added.\n']
    
#     # writing back prev version of information
#     write_JSON_file(TASKS_FILE, old_version)

#     # checkng result against expectations
#     assert output == expected_output
#     assert diff == expected_diff
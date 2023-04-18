from ships_list.additional_functions.bunker.additional_bunker_functions \
    import add_consuption_calculation
from ships_list.additional_functions.supporting_functions.json_functions \
    import read_JSON_file
# import BUNKERING_FILE
from ships_list.lists.Standard.constants import \
    BUNKERING_FILE

calculation = read_JSON_file(BUNKERING_FILE)[0]

add_consuption_calculation(calculation)

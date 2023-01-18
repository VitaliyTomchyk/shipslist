from ships_list.lists.Standard.constants import INDEXES_FILE
from ships_list.additional_functions.supporting_functions.json_functions \
    import append_JSON_file
from datetime import datetime

def add_index():

    ships_details = {"name": input('Name of index: '),
                     "value": input('Value: '),
                     "date": datetime.now().strftime("%d/%m/%Y")}

    append_JSON_file(ships_details, INDEXES_FILE)

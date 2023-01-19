from ships_list.lists.Standard.constants import INDEXES_FILE, SUPPORTING_FILE
from ships_list.additional_functions.supporting_functions.json_functions \
    import append_JSON_file, read_JSON_file
from ships_list.additional_functions.supporting_functions.input_functions \
    import input_from_list
from datetime import datetime


def collecting_indexes():
    disct_of_indexes = read_JSON_file(SUPPORTING_FILE)['indexes']
    return disct_of_indexes


def add_index():

    # collecting indexes dicts
    disct_of_indexes = collecting_indexes()

    # choosing index type
    type_of_index = input_from_list('type of index', list(disct_of_indexes))

    # choosing index name
    list_of_sub_indexes = list(map(lambda x: list(x)[0],
                                   disct_of_indexes[type_of_index]))

    sub_type_of_index = input_from_list('type of index',
                                        list_of_sub_indexes)

    sub_dict = list(filter(lambda x: x if list(x)[0] == sub_type_of_index
                           else False,
                           disct_of_indexes[type_of_index]))[0]

    list_of_sub_indexes = list(sub_dict[sub_type_of_index])

    # # choosing index subtype
    index_sub_type = input_from_list('subtype of index',
                                     list_of_sub_indexes)

    # adding index to database
    ships_details = {
        "type": type_of_index,
        "sub_type": sub_type_of_index,
        "name": index_sub_type,
        "value": input('Value: '),
        "date": datetime.now().strftime("%d/%m/%Y")}

    append_JSON_file(ships_details, INDEXES_FILE)

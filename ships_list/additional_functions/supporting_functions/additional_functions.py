import json

from ships_list.lists.Standard.constants import SUPPORTING_FILE
from ships_list.additional_functions.supporting_functions.json_functions \
    import read_JSON_file, amend_JSON_dict


def list_to_string(the_list):
    result = ''
    for line in the_list:
        result = result + '- ' + str(line) + '\n'
    return result


def list_to_ol_string(the_list):
    result = ''
    i = 1
    while i < len(the_list) + 1:
        result = result + str(i) + '. ' + str(the_list[i - 1]) + '\n'
        i = i + 1
    return result


def dict_to_ol_string(the_dict):
    result = ''
    the_list = list(set(the_dict))
    i = 1
    while i < len(the_list) + 1:
        result = result + str(i) + '. ' + str(the_list[i - 1]) + '\n'
        i = i + 1
    return result


def id_generator():
    i = 0
    with open(SUPPORTING_FILE, 'r') as f:
        i = json.load(f)['id'] + 1
    amend_JSON_dict({"id": i}, SUPPORTING_FILE)
    return i


def keys_excluder(the_dict, excluded_keys):
    updated_dict = the_dict
    the_dict.copy()
    if excluded_keys is not None:
        for key in excluded_keys:
            updated_dict.pop(key)
    return updated_dict


def missing_arguments_checker(the_dict, excluded_keys=None):
    # creating updated dictionary without excluded keys
    updated_dict = keys_excluder(the_dict, excluded_keys)

    # creates a list of keys that are missing in the_dict
    list_of_keys = list(filter(lambda x: x if updated_dict[x] is None
                               else False,
                               updated_dict))
    result_of_check = True
    if list_of_keys:
        print('Missing arguments are \n' + list_to_string(list_of_keys))
        result_of_check = False

    return result_of_check


def dictionary_finder(list_of_dictionaries, value, key):
    return list(filter(lambda x: True if x[key] == value
                else False, list_of_dictionaries))[0]


def list_of_val_by_key(key, the_list):
    result = list(map(lambda x: x[key], the_list))
    return result


def list_of_val_by_key_from_dict(key, the_dict):
    result = list(map(lambda x: x[key], the_dict))
    return result


def options_generator(key, document, key2=None, value2=None):
    if document == SUPPORTING_FILE:
        return read_JSON_file(document)[key]

    list_of_dicts = read_JSON_file(document)

    if key2 is None:
        return [x[key] for x in list_of_dicts]

    return [x[key] for x in list_of_dicts if x[key2] == value2]


def read_dict(the_dict):
    result = '\n'
    for key in the_dict:
        result = result + key + ": " + str(the_dict[key]) + '\n'
    print(result)


def appender(result, key, voyage):
    for point in voyage[key]:
        if isinstance(voyage[key], list):
            result.append(point)
        else:
            result.append(voyage[key])
    return result

# function checks if argument is number and if it is higher than 0 and
# lower than 100


def check_percentage(percentage):
    try:
        percentage = int(percentage)
        if percentage < 0 or percentage > 100:
            raise ValueError
    except ValueError:
        print('Percentage is not a number or is not in range 0-100')
        return False
    return True

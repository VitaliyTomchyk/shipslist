import json

from ships_list.lists.Standard.constats import SUPPORTING_FILE
from ships_list.additional_functions.json_functions import read_JSON_file, \
    amend_JSON_dict


def local_variables():
    links = read_JSON_file(SUPPORTING_FILE)['links']
    return locals().update(links)


def IMO_checker(IMO):
    # bloking function for easier testing
    result = True
    try:
        int(IMO)
    except ValueError:
        print('IMO is not correct')
        print('IMO is not a number')
        result = False

    if IMO is None:
        print('IMO is missing.')
        result = False
    return result
    IMO = str(IMO)

    if len(IMO) != 7:
        result = False

    result = 0
    i = 7
    while i != 1:
        result = result + i * int(IMO[-i])
        i = i - 1
    return True if str(result)[-1] == IMO[-1] else False


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
    return result


def id_generator():
    i = 0
    with open(SUPPORTING_FILE, 'r') as f:
        i = json.load(f)['id'] + 1
    amend_JSON_dict({"id": i}, SUPPORTING_FILE)
    return i


def missing_arguments_checker(the_dict):
    list_of_keys = []
    for key, value in the_dict.items():
        if value is None:
            list_of_keys.append(key)
    if list_of_keys:
        print('Missing arguments are \n' + list_to_string(list_of_keys))
        return False
    else:
        return True


def dictionary_finder(list_of_dictionaries, value, key):
    return list(filter(lambda x: True if x[key] == value
                else False, list_of_dictionaries))[0]


def list_of_val_by_key(key, the_list):
    result = list(map(lambda x: x[key], the_list))
    return result


def input_item(item):
    print('Please put {}'.format(item))
    return input()


def input_option(file, key, el_name):
    print('Please put {} from following list'.format(el_name))
    print('Please choose one of following options from {}'.format(key))

    options = list_of_val_by_key(key, read_JSON_file(file))
    print(list_to_string(options))

    if key == 'ships_name':
        the_option = input().upper()
    else:
        the_option = input()

    if the_option not in options:
        print('Option {} is not found.'.format(the_option))
        return

    return the_option


def input_from_supporting_info(key):
    return 1


def read_dict(the_dict):
    result = '\n'
    for key in the_dict:
        result = result + key + ": " + str(the_dict[key]) + '\n'
    print(result)

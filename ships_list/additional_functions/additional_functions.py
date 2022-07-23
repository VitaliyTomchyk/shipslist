import json


def missing_arguments_checker(dictionary):
    result = []

    for key in dictionary:
        if dictionary[key] is None:
            result.append(key)

    if result != []:
        result = list(map(lambda x: '-' + x, result))
        print('Following arguments are missing:\n' + list_to_string(result))
        print('Element has not been added.')
        return False
    return True


def append_JSON_file(information, file):
    list_of_el = read_JSON_file(file)
    if list_of_el == '':
        list_of_el = []
    list_of_el.append(information)
    write_JSON_file(file, list_of_el)


def read_JSON_file(file):
    with open(file, 'r') as f:
        return json.load(f)


def write_JSON_file(file, information):
    with open(file, "w") as f:
        json.dump(information, f, indent=4, separators=(',', ': '))


def amend_JSON_dict(information, file):
    with open(file, 'r') as f:
        dictionary = json.load(f)
        for key in information:
            dictionary[key] = information[key]
    with open(file, 'w') as f:
        json.dump(dictionary, f, indent=4, separators=(',', ': '))


def local_variables():
    supporting_info = 'ships_list/lists/Standard/supporting_info.json'
    links = read_JSON_file(supporting_info)['links']
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


def id_generator():
    i = 0
    with open('ships_list/lists/Standard/supporting_info.json', 'r') as f:
        i = json.load(f)['id'] + 1
    amend_JSON_dict({"id": i},
                    'ships_list/lists/Standard/supporting_info.json')
    return i


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
    print('Please put ' + el_name + ' from following list')
    print('Please choose one of following options from {}'.format(key))

    options = list_of_val_by_key(key, read_JSON_file(file))
    print(list_to_string(options))

    if key == 'ships_name':
        the_option = input().upper()
    else:
        the_option = input().upper()

    if the_option not in options:
        print('Option {} is not found.'.format(the_option))
        return

    return the_option


def input_from_supporting_info(key):
    file = 'ships_list/lists/Standard/supporting_info.json'
    options = read_JSON_file(file)[key]

    print('Choose one of following option of {}'.format(key))
    print(list_to_string(options))

    the_option = input()

    if the_option in options:
        return the_option
    else:
        print('Option chosed is not from list')
        return


def read_dict(the_dict):
    result = ''
    for key in the_dict:
        result = result + key + ": " + str(the_dict[key]) + '\n'
    print(result)

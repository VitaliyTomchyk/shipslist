import json


def missing_arguments_checker(dictionary):
    result = []
    for key in dictionary:
        if dictionary[key] is None:
            result.append(key)
    if result != []:
        result = list(map(lambda x: '-' + x, result))
        print('Following arguments are missing:\n' + list_to_string(result))
        return False
    return True


def append_JSON_file(information, file):
    with open(file, 'r') as f:
        list_of_el = json.load(f)
        if list_of_el == '':
            list_of_el = []

    list_of_el.append(information)

    with open(file, 'w') as f:
        json.dump(list_of_el, f, indent=4, separators=(',', ': '))


def read_JSON_file(file):
    with open(file, 'r') as f:
        return json.load(f)


def write_JSON_file(information, file):
    with open(file, 'w') as f:
        json.dump(information, f, indent=4, separators=(',', ': '))


def amend_JSON_dict(information, file):
    with open(file, 'r') as f:
        dictionary = json.load(f)
        for key in information:
            dictionary[key] = information[key]
    with open(file, 'w') as f:
        json.dump(dictionary, f, indent=4, separators=(',', ': '))


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


def json_read(file):

    with open(file, "r") as a_file:
        return json.load(a_file)


def json_write(file, information):

    with open(file, "w") as a_file:
        json.dump(information, a_file, indent=4, separators=(',', ': '))

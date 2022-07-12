import json


def append_JSON_file(information, file):
    with open(file, 'r') as f:
        list_of_el = json.load(f)

    list_of_el.append(information)

    with open(file, 'w') as f:
        json.dump(list_of_el, f, indent=4, separators=(',', ': '))


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
    return 2

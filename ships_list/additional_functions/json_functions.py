import json


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

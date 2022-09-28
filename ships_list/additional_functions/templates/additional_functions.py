from ships_list.additional_functions.supporting_functions.json_functions \
    import read_JSON_file
from ships_list.lists.Standard.constants import KEYS_OF_TEMPLATES_FILE
from ships_list.additional_functions.supporting_functions.input_functions \
    import input_from_list
from ships_list.additional_functions.supporting_functions.additional_functions\
    import filter_list_of_dict_by_value
import time


def template_selector():
    list_of_templates = read_JSON_file(KEYS_OF_TEMPLATES_FILE)

    names_of_templates = list(map(lambda x: x['template_name'],
                                  list_of_templates))

    name_of_template = input_from_list(
        'name of template', names_of_templates)

    template = filter_list_of_dict_by_value(list_of_templates, 'template_name',
                                            name_of_template)

    return template


def creating_address_for_filled_template():
    file_name = input('\nPlease enter name of filled template\n')\
        .upper()\
        .replace(" ", "_")
    address = 'ships_list/files/filled_templates/{}.txt'.format(file_name)
    time.sleep(2)
    print('\nAddress of filled template: \n{}\n'.format(address))
    return address


def values_from_user(template):
    keys = template['keys_of_tmplt']

    result = {}
    for key in keys:
        instruction = '\nPlease put value of "{}" to fill template\n'\
            .format(key)
        result[key] = input(instruction)

    return result

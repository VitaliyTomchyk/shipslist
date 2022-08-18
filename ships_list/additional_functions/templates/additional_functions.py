from ships_list.additional_functions.supporting_functions.json_functions \
    import read_JSON_file
from ships_list.additional_functions.supporting_functions.\
    additional_functions import list_to_ol_string
from ships_list.lists.Standard.constants import SUPPORTING_FILE


# function that returns type of template and address of filled template
# from JSON file list of dictionaries
def template_selector():
    list_of_templates = read_JSON_file(SUPPORTING_FILE)['templates']
    print('\nList of templates:')
    print(list_to_ol_string(list_of_templates))

    template_number = int(input('\nPlease enter number of template\n'))

    result = {
        "template_address": list_of_templates[template_number - 1]
        ['address_of_template'],
        "keys_of_tmplt": list_of_templates[template_number - 1]
        ['keys_of_template'],
        "template_type": set(list_of_templates[template_number - 1])[0]}

    return result


# function returns addres of type of template and address of filled template
def details_generator():

    the_template = template_selector()

    return the_template["template_address"], \
        the_template["type_of_template"], the_template["keys_of_tmplt"]


def data_collector(keys_of_tmplt, type_of_template):
    result = {key: input('\nPlease input {} \n'.format(key))
              for key in keys_of_tmplt}
    result['type_of_template'] = type_of_template
    return result


def creating_address_for_filled_template():
    address = 'ships_list/files/filled_templates/{}.txt'.format(
        input('\nPlease enter name of filled template\n').upper())
    # print address
    print('\nAddress of filled template: {}\n'.format(address))
    return address

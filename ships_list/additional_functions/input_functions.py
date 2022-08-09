from ships_list.lists.Standard.constats import SUPPORTING_FILE
from ships_list.additional_functions.additional_functions import \
    list_to_ol_string, options_generator, list_of_val_by_key
from ships_list.additional_functions.json_functions import read_JSON_file


def input_item(item):
    print('Please put {}'.format(item))
    return input()


def input_option(file, key, el_name):
    print('\nPlease put {} from following list.'.format(el_name))
    print('Choose number from options of {}.'.format(key))

    options = list_of_val_by_key(key, read_JSON_file(file))
    print(list_to_ol_string(options))

    the_option = options[int(input()) - 1]

    return the_option


def input_point(type, quantity_of_ports=None):

    result = []
    if quantity_of_ports is None:
        quantity = int(input('Please put quantity of {}\n'.format(type)))
    else:
        quantity = quantity_of_ports

    i = 0
    while i < quantity:
        text = 'Please put name of {} number {}\n'.format(type, i + 1)
        result.append(str(input(text)))
        i = i + 1

    return result


def input_from_list(value, options_list):
    print(f'\nPlease choose number from following list to select {value}.')

    print(list_to_ol_string(options_list))

    try:
        number_chosen = input()
        the_option = options_list[int(number_chosen) - 1]
        return the_option

    except IndexError or ValueError:
        choise = input('The option is out of range. ' +
                       'Do you want to try again? (y/n)')

        if choise == 'y':
            input_from_list(value, options_list)
        return


def input_filtered_with_num(
        pair,
        pair2,
        document=SUPPORTING_FILE):

    key, value = pair
    key2, value2 = pair2
    print(f'\nPlease choose number from following list to select {value}.')

    options = options_generator(key, document, key2, value2)
    print('The value should be from 1 to {}'.format(len(options)))
    print(list_to_ol_string(options))

    try:
        the_option = options[int(input()) - 1]
        return the_option

    except IndexError or TypeError:
        choise = input('The option is out of range. ' +
                       'Do you want to try again? (y/n)')

        if choise == 'y':
            input_with_num(key, value, document)
        return


def input_with_num(key, value, document=SUPPORTING_FILE):
    print(f'\nPlease choose number from following list to select {value}.')

    options = options_generator(key, document)
    print('The value should be from 1 to {}'.format(len(options)))
    print(list_to_ol_string(options))

    try:
        number_chosen = input()
        the_option = options[int(number_chosen) - 1]
        return the_option

    except IndexError or ValueError:
        choise = input('The option is out of range. ' +
                       'Do you want to try again? (y/n)')
        if choise == 'y':
            input_with_num(key, value, document)
        return

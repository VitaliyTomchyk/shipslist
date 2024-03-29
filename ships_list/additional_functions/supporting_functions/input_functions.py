from ships_list.lists.Standard.constants import SUPPORTING_FILE
from ships_list.additional_functions.supporting_functions.additional_functions\
    import list_to_ol_string, options_generator
from ships_list.additional_functions.supporting_functions.json_functions \
    import read_JSON_file


def input_email(element):
    # input email
    email = input('Please enter email of {}\n'.format(element))
    # checking if email is valid
    if not email or '@' not in email:
        print('Email is not valid. Please try again.')
        email = input_email()
    # returning email
    return email


def input_item(item):
    print('Please put {}'.format(item))
    return input('')


def input_option_from_dict(file, key, el_name):

    dict_of_standard = read_JSON_file(file)[key]
    options = list(dict_of_standard)

    print('\nPlease put {} from following list.'.format(el_name))
    print('Choose number from options of {}.'.format(key))
    print(list_to_ol_string(options))

    user_input = input('')
    if not user_input:
        value = options[0]
    else:
        value = options[int(user_input) - 1]

    return value


def input_option(file, key, el_name):
    print('\nPlease put {} from following list.'.format(el_name))
    print('Choose number from options of {}.'.format(el_name))

    options = list(map(lambda x: x[key], read_JSON_file(file)))
    print(list_to_ol_string(options))

    the_option = options[int(input('')) - 1]

    return the_option


def quantity_collector(type):
    input_required = True
    while input_required:
        try:
            quantity = int(
                input('Please put quantity of {}\n'.format(type)))
            input_required = False
        except ValueError:
            print('Quantity is not a number, please put number.\n')
    return quantity


def input_point(type_of_point):
    quantity = quantity_collector(type_of_point)
    result = specifier_of_points(quantity, type_of_point)
    return result


def specifier_of_points(quantity, type='point'):
    result = []
    i = 0
    while i < quantity:
        text = 'Please put name of {} number {}\n'.format(type, i + 1)
        result.append(str(input(text)))
        i = i + 1
    return result


def input_from_list(value, options_list):
    print(f'\nPlease choose number from following list to select {value}.')

    print(list_to_ol_string(options_list))

    number_chosen = input('')
    try:
        the_option = options_list[int(number_chosen) - 1]

    except IndexError or ValueError:
        choise = input('The option is out of range. ' +
                       'Do you want to try again? (y/n)')
        if choise == 'y':
            input_from_list(value, options_list)
        return
    return the_option


def input_filtered_with_num(pair, pair2, document=SUPPORTING_FILE):

    key, value = pair
    key2, value2 = pair2
    print(f'\nPlease choose number from following list to select {value}.')

    options = options_generator(key, document, key2, value2)
    print('The value should be from 1 to {}'.format(len(options)))
    print(list_to_ol_string(options))

    try:
        the_option = options[int(input('')) - 1]
        return the_option

    except IndexError or TypeError:
        choise = input('The option is out of range. ' +
                       'Do you want to try again? (y/n)')

        if choise == 'y':
            input_with_num(key, value, document)
        return


# input instrument for inputing value from list
def input_with_num(key, value, document=SUPPORTING_FILE):
    print(f'\nPlease choose number from following list to select {value}.')

    options = options_generator(key, document)
    print('The value should be from 1 to {}'.format(len(options)))
    print(list_to_ol_string(options))

    try:
        number_chosen = input('')
        the_option = options[int(number_chosen) - 1]
        return the_option

    except IndexError or ValueError:
        choise = input('The option is out of range. ' +
                       'Do you want to try again? (y/n)')
        if choise == 'y':
            input_with_num(key, value, document)
        return

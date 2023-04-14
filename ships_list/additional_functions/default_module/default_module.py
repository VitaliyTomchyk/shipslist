from ships_list.additional_functions.supporting_functions.json_functions \
    import append_JSON_file, read_JSON_file, write_JSON_file
from ships_list.additional_functions.supporting_functions.input_functions \
    import input_from_list
from ships_list.additional_functions.supporting_functions.additional_functions\
    import id_generator
from ships_list.additional_functions.supporting_functions.additional_functions\
    import filter_list_of_dict_by_value


# function input_email
def input_email(element):
    # input email
    email = input('Please enter email of {}\n'.format(element))
    # checking if email is valid
    if not email or '@' not in email:
        print('Email is not valid. Please try again.')
        email = input_email()
    # returning email
    return email


# function to create a element
def create_element(input_element, file):
    element = {
        'id': id_generator(),
        'name': input(f'Please enter {input_element} name\n'),
        'email': input_email(),
        'phone_number': input('Please enter phone' +
                              f' number of {input_element}\n'),
        'address': input(f'Please enter address of {input_element}\n'),
    }
    append_JSON_file(element, file)
    print(f'\nCreated element with the following details:\n{element}')


# function to remove a element
def remove_element(element, file):
    # reading parties from file
    list_of_elements = read_JSON_file(file)

    if list_of_elements == []:
        print('There are no elements to remove.')
        return

    # creating list of element names
    list_of_names = list(
        map(lambda x: x['name'], list_of_elements))

    # selecting element to remove
    element_to_remove = input_from_list('{} to remove'.format(element),
                                        list_of_names)

    # creating new list of parties without selected element
    result = list(filter(lambda x: x['name'] != element_to_remove,
                         list_of_elements))

    # saving new list of parties to file
    write_JSON_file(file, result)

    print('{} {} was removed'.format(element, element_to_remove))


# function to edit a element
def edit_element(element, file):
    # reading parties from file
    list_of_elements = read_JSON_file(file)

    # creating list of element names
    list_of_names = list(
        map(lambda x: x['name'], list_of_elements))

    # selecting name of element to edit
    element_name_to_edit = input_from_list('{} to edit'.format(element),
                                           list_of_names)

    # selecting element to edit
    element_to_edit = filter_list_of_dict_by_value(list_of_elements, 'name',
                                                   element_name_to_edit)

    # select field to edit
    field_to_edit = input_from_list('field to edit',
                                    ['name', 'email',
                                        'phone_number', 'address'])
    # select new value of field
    new_value = input('Please enter new value of field {}\n'.format(
        field_to_edit))

    # updating value of field
    element_to_edit[field_to_edit] = new_value

    # saving new list of parties to file
    write_JSON_file(list_of_elements, file)

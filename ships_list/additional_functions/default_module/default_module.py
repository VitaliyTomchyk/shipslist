from ships_list.lists.Standard.constants import file
from ships_list.additional_functions.supporting_functions.json_functions \
    import append_JSON_file, read_JSON_file, write_JSON_file
from ships_list.additional_functions.supporting_functions.input_functions \
    import input_from_list
from ships_list.additional_functions.supporting_functions.additional_functions\
    import id_generator


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
def add_element(input_element, file):
    # creating a element
    element = {}
    # generating id
    element['id'] = id_generator()
    # adding element name
    element['name'] = input('Please enter {} name\n'.format(input_element))
    # adding email
    element['email'] = input_email()
    # adding phone number
    element['phone_number'] = input(
        'Please enter phone number of {}\n'.format(input_element))
    # adding address
    element['address'] = input(
        'Please enter address of {}\n'.format(input_element))
    # save element to file
    append_JSON_file(element, file)

    # printing created element
    print('\nCreated element with following details:\n')
    print(element)


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
def edit_element(element):
    # reading parties from file
    list_of_elements = read_JSON_file(file)

    # creating list of element names
    list_of_names = list(
        map(lambda x: x['name'], list_of_elements))

    # selecting name of element to edit
    element_name_to_edit = input_from_list('{} to edit'.format(element),
                                           list_of_names)

    # selecting element to edit
    element_to_edit = list(filter(lambda x: x['name'] == element_name_to_edit,
                                  list_of_elements))[0]

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

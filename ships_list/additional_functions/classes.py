from ships_list.additional_functions.supporting_functions.json_functions \
    import append_JSON_file, read_JSON_file, write_JSON_file
from ships_list.additional_functions.supporting_functions.input_functions \
    import input_from_list
from ships_list.additional_functions.supporting_functions.additional_functions\
    import id_generator, read_dict


def input_email(element):
    # input email
    email = input('Please enter email of {}\n'.format(element))
    # checking if email is valid
    if not email or '@' not in email:
        print('Email is not valid. Please try again.')
        email = input_email()
    # returning email
    return email


class StoredElement:
    # class constructor
    def __init__(self, entity, file):
        self.entity = entity
        self.file = file

    # function to create an element
    def create_element(self):
        element = {
            'id': id_generator(),
            'name': input(f'Please enter {self.entity} name\n'),
            'email': input_email(
                self.entity),
            'phone_number': input('Please enter' +
                                  f' phone number of {self.entity}\n')
        }

        # appending element with keys 'company' and 'position' and values from
        # user if self.entity is 'person'
        if self.entity == 'person':
            element['company'] = input('Please enter company name\n')
            element['position'] = input('Please enter position\n')

        # appending element with keys 'address' and 'web site' and values from
        # user if self.entity is 'company'
        if self.entity == 'company':
            element['address'] = input('Please enter company address\n')
            element['web_site'] = input('Please enter web site\n')

        append_JSON_file(element, self.file)

        # printing description of created element
        description_of_element = read_dict(element)
        print(
            f'\nCreated {self.entity} with the following details:\n' +
            f'{description_of_element}\n')

    # function to remove an element

    def remove_element(self):
        list_of_elements = read_JSON_file(self.file)
        if not list_of_elements:
            print('There are no elements to remove.')
            return

        list_of_names = [element['name'] for element in list_of_elements]
        element_to_remove = input_from_list(
            f'{self.entity} to remove', list_of_names)
        result = [
            element for element in list_of_elements
            if element['name'] != element_to_remove]

        write_JSON_file(self.file, result)
        print(f'{self.entity} {element_to_remove} was removed')

    # function to edit an element
    def edit_element(self):
        list_of_elements = read_JSON_file(self.file)
        if not list_of_elements:
            print('There are no elements to edit.')
            return

        list_of_names = [element['name'] for element in list_of_elements]
        element_name_to_edit = input_from_list(
            f'{self.entity} to edit', list_of_names)

        element_to_edit = next(
            (element for element in list_of_elements
             if element['name'] == element_name_to_edit),
            None)
        if not element_to_edit:
            print(f'{self.entity} {element_name_to_edit} not found')
            return

        field_to_edit = input_from_list(
            'field to edit', [
                'name', 'email', 'phone_number', 'address'])
        new_value = input(f'Please enter new value of field {field_to_edit}\n')
        element_to_edit[field_to_edit] = new_value

        write_JSON_file(self.file, list_of_elements)

        # printing description of edeted element
        description_of_element = read_dict(element_to_edit)
        print(
            f'\nCreated {self.entity} with the following details:\n' +
            f'{description_of_element}\n')

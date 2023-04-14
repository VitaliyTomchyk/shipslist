import json
from ships_list.lists.Standard.constants import SUPPORTING_FILE
from ships_list.additional_functions.supporting_functions.json_functions \
    import append_JSON_file, read_JSON_file, write_JSON_file
from ships_list.additional_functions.supporting_functions.input_functions \
    import input_from_list
from ships_list.additional_functions.supporting_functions.additional_functions\
    import id_generator


class Task():
    def __init__(self, title, stage, ship):
        self.ID = 1
        self.title = title
        self.stage = stage
        self.ship = ship
        self.status = 'Pending'

    def close_task(self):
        self.status = 'Done'

    def read_task(self):
        print('Task is \n{}\nShip is \n{}\n'.format(self.title, self.ship) +
              'Stage is \n{}\nStatus is {}').format(self.stage, self.status)


class Ship():
    def __init__(self, name, IMO):
        self.name = name
        self.IMO = IMO
        self.has_list = False
        self.list_related = None

    def set_list(self, name, lists_id):
        self.has_list = True
        self.list_related = lists_id

    def read_ship(self):
        print("Ship is {}\n IMO is {}\n Has list? {}".format(self.name,
                                                             self.IMO,
                                                             self.has_list))


class Ships_list():
    def __init__(self, name_of_ship, title_of_voyage):
        self.ships_list_id = 1
        self.name_of_list = title_of_voyage
        self.name_of_ship = name_of_ship

        with open(SUPPORTING_FILE, 'r') as f:
            standard_list = json.load(f)

        for task in standard_list:
            task["ship"] = name_of_ship

        self.task_list = standard_list

    def read_ships_list(self):
        print('Ships list name is \n{}'.format(self.name_of_list))
        print('Ships name is {}'.format(self.name_of_ship))
        print('Ships list \n{}'.format(self.task_list))

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
                                  f' phone number of {self.entity}\n'),
            'address': input(f'Please enter address of {self.entity}\n'),
        }
        append_JSON_file(element, self.file)
        print(
            f'\nCreated {self.entity} with the following details:\n{element}')

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

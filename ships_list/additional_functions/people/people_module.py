from ships_list.lists.Standard.constants import PEOPLE_FILE
from ships_list.additional_functions.default_module.default_module import \
    add_element, remove_element, edit_element


# function to create a person
def add_person():
    add_element('person', PEOPLE_FILE)


# function to remove a person
def remove_person():
    remove_element('person', PEOPLE_FILE)


# function to edit a person
def edit_person():
    edit_element('person', PEOPLE_FILE)

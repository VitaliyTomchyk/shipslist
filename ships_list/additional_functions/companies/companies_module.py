from ships_list.lists.Standard.constants import COMPANIES_FILE
from ships_list.additional_functions.default_module.default_module import \
    create_element, remove_element, edit_element


# function to create a company
def add_company():
    create_element('company', COMPANIES_FILE)


# function to remove a company
def remove_company():
    remove_element('company', COMPANIES_FILE)


# function to edit a company
def edit_company():
    edit_element('company', COMPANIES_FILE)

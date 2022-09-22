from string import Template
from ships_list.additional_functions.supporting_functions.json_functions \
    import append_JSON_file, read_JSON_file, write_JSON_file
from ships_list.additional_functions.templates.additional_functions import \
    template_selector, creating_address_for_filled_template, values_from_user
from ships_list.additional_functions.supporting_functions.\
    additional_functions import assurance_question
from ships_list.lists.Standard.constants import FILLED_TEMPLATES_FILE, \
    KEYS_OF_TEMPLATES_FILE
import time
import os


# function creates filled template
def fill_template():

    # assurance
    assurance_question('fill a template')

    # selecting template
    selected_template = template_selector()

    # collecting values to put in template from user
    dict_with_input_keys_and_values = values_from_user(selected_template)

    # collecting template information
    with open(selected_template['address_of_template'], 'r') as template_file:
        temp_obj = Template(template_file.read())

    # substituting vars with values
    str_with_result = temp_obj.substitute(**dict_with_input_keys_and_values)

    # saving filled template
    filled_template_address = creating_address_for_filled_template()
    with open(filled_template_address, 'w') as f:
        f.write(str_with_result)

    # saving address of filled template
    data = dict_with_input_keys_and_values
    data['filled_template_address'] = filled_template_address
    append_JSON_file(data, FILLED_TEMPLATES_FILE)

    # reporting to user
    time.sleep(2)
    print('Template has been filled and saved.\n' +
          'Filled template is \nQuote\n{}\nUnquote'.format(str_with_result))


# # function deletes template
def remove_template():

    # assurance
    assurance_question('delete a template')

    # selecting template
    selected_template = template_selector()

    # deleting template file
    os.remove(selected_template['address_of_template'])

    # deleting template details from JSON file
    list_of_templates = read_JSON_file(KEYS_OF_TEMPLATES_FILE)
    list_of_templates.remove(selected_template)

    # writing new list of templates to JSON file
    write_JSON_file(KEYS_OF_TEMPLATES_FILE, list_of_templates)

    # reporting to user
    time.sleep(1)
    print('Template has been deleted.\n')

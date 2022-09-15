from ships_list.additional_functions.supporting_functions. \
    additional_functions import assurance_question
from ships_list.additional_functions.templates.create_template.Tkinter \
    import open_txt_file
from ships_list.additional_functions.templates.create_template.\
    additional_functions import keys_of_template_finder, add_template_to_dict
import time
from ships_list.lists.Standard.constants import INSTRUCTIONS_TO_CREATE_TEMPLATE


def create_template():

    # printing instructions
    with open(INSTRUCTIONS_TO_CREATE_TEMPLATE, 'r') \
            as file:
        instructions = file.read()
    print(instructions)
    time.sleep(2)

    # assurance question
    assurance_question('create/amend a new template')

    # input template name
    template_name = input('Write the name of the template you want to ' +
                          'edit or create:\n')
    address_of_template = (f"ships_list/files/{template_name}.txt")

    # open new file at address_of_template if it doesn't exist yet else pass
    with open(address_of_template, 'a') as file:
        pass

    # input template text with TKinter
    open_txt_file(address_of_template)

    # collecting input text from file
    with open(address_of_template, 'r') as text_file:
        template_text = text_file.read()

    # for every word after $ in template_text, add it to the
    # list of list_of_keys
    list_of_keys = keys_of_template_finder(template_text)

    # add dict with template details to storage of template details
    result = {
        template_name: {
            "address_of_template": address_of_template,
            "keys_of_tmplt": list_of_keys
        }}

    # adding template information
    add_template_to_dict(result)

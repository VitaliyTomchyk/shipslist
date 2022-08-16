from string import Template
# from ships_list.lists.Standard.constants import SUPPORTING_FILE
from ships_list.additional_functions.supporting_functions.json_functions \
    import append_JSON_file


# create function that returns text of fill text template taken from .txt file
# with data taken from user with input function for each field
def fill_template():
    address_to_template = 'ships_list/files/pda_template.txt'
    type_of_template = 'pda_request'

    data = {key: input('Please input {} \n'.format(key))
            for key in type_of_template}

    with open(address_to_template, 'r') as template_file:
        template = template_file.read()

    temp_obj = Template(template)
    result = temp_obj.substitute(**data)

    # write filled template to file
    filled_template_address = 'ships_list/files/filled_pda.txt'
    with open(filled_template_address, 'w') as pda_file:
        pda_file.write(result)

    data = {'template_name': type_of_template,
            'filled_template': filled_template_address}

    # writing data to JSON file
    address_of_json_file = 'ships_list/additional_functions/' + \
        'templates/data_of_templates.json'
    append_JSON_file(address_of_json_file, data)

    print('Template filled and saved.')

from string import Template
from ships_list.additional_functions.supporting_functions.json_functions \
    import append_JSON_file
from ships_list.additional_functions.templates.additional_functions import \
    details_generator, data_collector, creating_address_for_filled_template


# create function that returns text of fill text template taken from .txt file
# with data taken from user with input function for each field
def fill_template():

    # get address, type and keys of template
    tmplt_details = details_generator()

    # get data from user
    data = data_collector(tmplt_details["keys_of_tmpl"],
                          tmplt_details["type_of_template"])

    # read and fill template from file
    with open(tmplt_details["address_to_template"], 'r') as template_file:
        temp_obj = Template(template_file.read())
    str_with_result = temp_obj.substitute(**data)

    # write filled template to file
    filled_template_address = creating_address_for_filled_template()
    with open(filled_template_address, 'w') as pda_file:
        pda_file.write(str_with_result)

    data = {'filled_template_address': filled_template_address}

    # writing data to JSON file
    address_of_json_file = 'ships_list/lists/data_of_templates.json'
    append_JSON_file(data, address_of_json_file)

    print('Template filled and saved.')
    print('Filled template is \n\n{}'.format(str_with_result))

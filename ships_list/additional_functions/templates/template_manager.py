from string import Template
from ships_list.additional_functions.supporting_functions.json_functions \
    import append_JSON_file
from ships_list.additional_functions.templates.additional_functions import \
    details_generator, data_collector, creating_address_for_filled_template
from ships_list.additional_functions.supporting_functions.\
    additional_functions import assurance_question


def fill_template():

    assurance_question('fill a template')

    tmplt_details = details_generator()

    data = data_collector(tmplt_details[2],
                          tmplt_details[1])

    with open(tmplt_details[0], 'r') as template_file:
        temp_obj = Template(template_file.read())
    str_with_result = temp_obj.substitute(**data)

    filled_template_address = creating_address_for_filled_template()
    with open(filled_template_address, 'w') as f:
        f.write(str_with_result)

    data = {'filled_template_address': filled_template_address}

    address_of_json_file = 'ships_list/lists/data_of_templates.json'
    append_JSON_file(data, address_of_json_file)

    print('Template filled and saved.')
    print('Filled template is \n\n{}'.format(str_with_result))

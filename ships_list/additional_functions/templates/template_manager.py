# template filler
from string import Template


# create function that returns text of fill text template taken from .txt file
# with data taken from user with input function for each field
def fill_template():
    data = {
        'receiver': input('Please input receiver\n'),
        'port_type': input('Please input type of port\n'),
        'port_name': input('Please input port name\n'),
        'cargo_name': input('Please input cargo name\n'),
        'cargo_quantity': input('Please input cargo quantity, mt\n'),
        'ships_name': input('Please input ship\'s name\n'),
        'cargo_operations_term': input('Please input cargo operations term\n')}

    with open('ships_list/files/pda_template.txt', 'r') as template_file:
        template = template_file.read()

    temp_obj = Template(template)
    result = temp_obj.substitute(**data)

    with open('ships_list/files/filled_pda.txt', 'w') as pda_file:
        pda_file.write(result)

    print('Template filled and saved.')

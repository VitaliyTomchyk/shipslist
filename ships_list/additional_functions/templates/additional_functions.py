# function returns addres of type of template and address of filled template
def details_generator():
    type_of_template = 'pda_request'
    address_to_template = 'ships_list/files/pda_request_template.txt'
    keys_of_tmplt = [
        "receiver",
        "port_name",
        "port_type",
        "ships_name",
        "cargo_name",
        "cargo_quantity",
        "cargo_operations_term"]
    return address_to_template, type_of_template, keys_of_tmplt


def data_collector(keys_of_tmplt, type_of_template):
    result = {key: input('\nPlease input {} \n'.format(key))
              for key in keys_of_tmplt}
    result['type_of_template'] = type_of_template
    return result


def creating_address_for_filled_template():
    address = 'ships_list/files/filled_templates/{}.txt'.format(
        input('\nPlease enter name of filled template\n').upper())
    # print address
    print('\nAddress of filled template: {}\n'.format(address))
    return address

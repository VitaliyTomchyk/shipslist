from datetime import datetime
from ships_list.lists.Standard.constants import SHIPS_FILE, \
    LIST_OF_VOYAGES_FILE
from ships_list.additional_functions.supporting_functions.json_functions \
    import read_JSON_file


def IMO_checker(IMO):
    # bloking function for easier testing
    result = True
    if isinstance(IMO, int) is False:
        print('IMO is not should be a number.')
        return False

    if IMO in [x['IMO'] for x in read_JSON_file(SHIPS_FILE)]:
        print('IMO is already in list')
        return False

    return result
    IMO = str(IMO)

    if len(str(IMO)) != 7:
        result = False

    i = 7
    while i != 1:
        result = result + i * int(IMO[-i])
        i = i - 1
    return True if str(result)[-1] == IMO[-1] else False


def leg_options_generator(types_of_leg, types_of_speed, parameter):
    options = []
    for leg in types_of_leg:
        for speed in types_of_speed:
            options.append(leg + '_' + speed + '_' + parameter)
    return options


def add_additional_consumption(ship):
    print('Additional consumption will be added now.')

    text = "\nPlease add additional consumption during {}, mt of MGO\n"
    ship['additional_consumption'] = {'steaming': None, 'at_port': None}

    for stage in ['steaming', 'at_port']:
        revised_text = text.format(stage)
        additional_consumption = float(
            str(input(revised_text)).replace(',', '.'))
        ship['additional_consumption'][stage] = additional_consumption

    return ship


def add_stay_consumption(ship, parameter):
    print('Port stay consumption will be added now.')
    text = "\nPlease add main consumption in {} condition, mt\n"

    ship[parameter]['stay_consumption'] = {'idle': None, 'working': None}

    for stage in ['idle', 'working']:
        revised_text = text.format(stage)
        additional_consumption = float(
            str(input(revised_text)).replace(',', '.'))
        ship[parameter]['stay_consumption'][stage] = additional_consumption

    return ship


def add_parameter(ship, parameter):

    print('\n\nParameter {} will be added now.'.format(parameter))
    ship[parameter] = {}

    types_of_leg = ['laden', 'ballast']
    types_of_speed = ['full', 'eco']

    options = leg_options_generator(types_of_leg, types_of_speed, parameter)

    for option in options:
        the_type_of_leg, the_type_of_speed, the_parameter = option.split('_')
        units = 'kn' if the_parameter == 'speed' else 'mt/day'

        text = "\nPlease add {} {} {} of the ship, {}\n".format(
            the_type_of_speed, the_type_of_leg, the_parameter, units)
        input_value = input(text)
        ship[parameter][option] = float(str(input_value).replace(',', '.'))
    ship[parameter]["date_of_update"] = "{:%Y-%m-%d}".format(datetime.now())
    return ship


def ship_in_list_checker(name):
    list_of_ships = read_JSON_file(SHIPS_FILE)
    if list_of_ships == []:
        return False
    for ship in list_of_ships:
        if ship['ships_name'] == name:
            print('Ship with this name and IMO is already in list, ' +
                  'therefore, it will not be added again.')
            return True
    return False


def voyages_assigned_checker(ship):
    list_of_dicts = read_JSON_file(LIST_OF_VOYAGES_FILE)
    ships_with_voyages = list(map(lambda x: x['ship'], list_of_dicts))
    if ship not in ships_with_voyages:
        return False
    return True

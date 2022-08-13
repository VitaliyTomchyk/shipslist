from datetime import datetime
from ships_list.lists.Standard.constants import SHIPS_FILE, \
    LIST_OF_VOYAGES_FILE
from ships_list.additional_functions.json_functions import read_JSON_file


def IMO_checker(IMO):
    # bloking function for easier testing
    result = True
    try:
        int(IMO)
    except ValueError:
        print('IMO is not correct')
        print('IMO is not a number')
        return False

    if IMO in [x['IMO'] for x in read_JSON_file(SHIPS_FILE)]:
        print('IMO is already in list')
        return False

    if IMO is None:
        print('IMO is missing.')
        result = False
    return result
    IMO = str(IMO)

    if len(IMO) != 7:
        result = False

    result = 0
    i = 7
    while i != 1:
        result = result + i * int(IMO[-i])
        i = i - 1
    return True if str(result)[-1] == IMO[-1] else False


def options_generator(types_of_leg, types_of_speed, parameter):
    options = []
    for leg in types_of_leg:
        for speed in types_of_speed:
            options.append(leg + '_' + speed + '_' + parameter)
    return options


def add_additional_consumption(ship):

    text = "\nPlease add additional consumption during {}, mt of MGO\n"
    ship['additional_consumption'] = {'port_stay': None, 'steaming': None}

    for stage in ['port_stay', 'steaming']:
        revised_text = text.format(stage)
        additional_consumption = int(input(revised_text))
        ship['additional_consumption'][stage] = additional_consumption

    return ship


def add_parameter(ship, parameter):

    ship[parameter] = {}

    types_of_leg = ['laden', 'ballast']
    types_of_speed = ['full', 'eco']

    options = options_generator(types_of_leg, types_of_speed, parameter)
    for option in options:
        the_type_of_leg, the_type_of_speed, the_parameter = option.split('_')
        units = 'kn' if the_parameter == 'speed' else 'mt/day'

        text = "\nPlease add {} {} {} of the ship, {}\n".format(
            the_type_of_speed, the_type_of_leg, the_parameter, units)

        ship[parameter][option] = int(input(text))
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

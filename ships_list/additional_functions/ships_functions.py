from ships_list.additional_functions.additional_functions import IMO_checker, \
    list_to_string, list_of_val_by_key
from ships_list.lists.Standard.constats import LIST_OF_VOYAGES_FILE, SHIPS_FILE
from ships_list.additional_functions.json_functions import read_JSON_file, \
    write_JSON_file


def add_ship():
    name = input('\nShip adding function is activated\n' +
                 'Please enter name of the ship\n')
    IMO = input('Please enter IMO of the ship\n')

    if IMO_checker(IMO) is False:
        return

    ships_details = {"ships_name": name.upper(),
                     "IMO": int(IMO),
                     "has_tasks": False,
                     "ships_list": None,
                     "number_of_tasks": 0}

    list_of_ships = read_JSON_file(SHIPS_FILE)
    list_of_ships.append(ships_details)

    write_JSON_file(SHIPS_FILE, list_of_ships)

    print('Ship {} has been added.\n'.format(name.upper()))


def voyages_assigned(ship):
    list_of_dicts = read_JSON_file(LIST_OF_VOYAGES_FILE)
    ships_with_voyages = list(map(lambda x: x['ship'], list_of_dicts))
    if ship not in ships_with_voyages:
        return False
    return True


# removes function from bata base
def remove_ship():

    list_of_ships = read_JSON_file(SHIPS_FILE)
    list_of_names = list_to_string(list_of_val_by_key('ships_name',
                                                      list_of_ships))
    print('\nList of ships:\n' + list_of_names)

    print('Please put ship\'s name.')
    name = input().upper()

    if voyages_assigned(name):
        print('\nShip {} can not be removed due to voyage(s) '.format(name) +
              'assigned.')
        return

    for ship in list_of_ships:
        if ship['ships_name'] == name:
            list_of_ships.remove(ship)
            write_JSON_file(SHIPS_FILE, list_of_ships)
            print('\nShip ' + name + ' was removed.\n')
        else:
            print('\nShip ' + name + ' was not found')


def read_ship(name):
    return name

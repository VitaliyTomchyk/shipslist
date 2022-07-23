from ships_list.additional_functions.additional_functions import IMO_checker, \
    list_to_string, read_JSON_file, write_JSON_file, list_of_val_by_key
from ships_list.lists.Standard.constats import SHIPS_FILE


def add_ship():
    print('\nShip adding function is activated')
    print('Please enter name of the ship')
    name = input()
    print('Please enter IMO of the ship')
    IMO = input()

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
    return False


# removes function from bata base
def remove_ship():
    file = SHIPS_FILE

    list_of_ships = read_JSON_file(file)
    list_of_names = list_to_string(list_of_val_by_key('ships_name',
                                                      list_of_ships))
    print('\nList of ships:\n' + list_of_names)

    print('Please put ship\'s name')
    name = input().upper()
    if voyages_assigned(name):
        print('\nShip {} can not be removed due to voyage(s) assigned.')
        return

    for ship in list_of_ships:
        if ship['ships_name'] == name:
            list_of_ships.remove(ship)
            print('\nShip ' + name + ' was removed.\n')
            return

    print('\nShip ' + name + ' was not found')

    write_JSON_file(file, list_of_ships)


def read_ship(name):
    return name

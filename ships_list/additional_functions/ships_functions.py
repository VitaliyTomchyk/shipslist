from ships_list.additional_functions.additional_functions import IMO_checker, \
    read_JSON_file, write_JSON_file, list_of_val_by_key


def add_ship():
    print('Ship adding function is activated')
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
    file = 'ships_list/lists/ships.json'

    list_of_ships = read_JSON_file(file)
    list_of_ships.append(ships_details)
    write_JSON_file(file, list_of_ships)

    print('Ship {} has been added.'.format(name))


# removes function from bata base
def remove_ship():
    file = 'ships_list/lists/ships.json'

    list_of_ships = read_JSON_file(file)
    list_of_names = list_of_val_by_key(list_of_ships, 'ships_name')
    print('List of ships:\n' + list_of_names)

    print('Please put ship\'s name')
    name = input().upper()

    for ship in list_of_ships:
        if ship['ships_name'] == name:
            list_of_ships.remove(ship)
            print('Ship ' + name + ' was removed')
            break

    print('Ship ' + name + ' was not found')

    write_JSON_file(file, list_of_ships)


def read_ship(name):
    return name

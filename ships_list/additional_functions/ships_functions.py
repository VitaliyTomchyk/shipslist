from ships_list.additional_functions.additional_functions import IMO_checker
import json


def add_ship(name, IMO):
    if IMO_checker(IMO) is False:
        return

    ships_details = {"ships_name": name.upper(),
                     "IMO": int(IMO),
                     "has_tasks": False,
                     "ships_list": None,
                     "number_of_tasks": 0}
    with open('ships_list/lists/ships.json', 'r') as f:
        list_of_ships = json.load(f)

    list_of_ships.append(ships_details)

    with open('ships_list/lists/ships.json', 'w') as f:
        json.dump(list_of_ships, f, indent=4, separators=(',', ': '))

    print('Ship {} has been added.'.format(name))


# removes function from bata base
def remove_ship(name):
    name = name.upper()
    with open('ships_list/lists/ships.json', 'r') as f:
        list_of_ships = json.load(f)

    for ship in list_of_ships:
        if ship['name'] == name:
            list_of_ships.remove(ship)
            print('Ship ' + name + ' was removed')
            break

    print('Ship ' + name + ' was not found')

    with open('ships_list/lists/ships.json', 'w') as f:
        json.dump(list_of_ships, f, indent=4, separators=(',', ': '))


def read_ship(name):
    return

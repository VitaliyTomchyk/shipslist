import json


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


def add_ship(name, IMO):
    ships_details = {"name": name,
                     "IMO": int(IMO),
                     "has_list": False,
                     "ships_list": None}

    with open('ships_list/lists/ships.json', 'r') as f:
        list_of_ships = json.load(f)

    list_of_ships.append(ships_details)

    with open('ships_list/lists/ships.json', 'w') as f:
        json.dump(list_of_ships, f, indent=4, separators=(',', ': '))

    print('Ship {} has been added.'.format(name))


def write_task_in_list(task):
    with open('ships_list/lists/tasks.json', 'r') as f:
        list_of_ships = json.load(f)

    list_of_ships.append(task)

    with open('ships_list/lists/tasks.json', 'w') as f:
        json.dump(list_of_ships, f, indent=4, separators=(',', ': '))


def add_task(name, IMO, task, task_party, task_stage):
    print('task planned to be added is ' + task +
          ' for ship {} with IMO {}'.format(name, IMO))
    the_task = {}
    # Place for Vitaliy to put the code
    # Below functions writs the_task in list of tasks
    # (ships_list/lists/tasks.json)
    write_task_in_list(the_task)


def IMO_checker(IMO):
    # bloking function for easier testing
    return True
    IMO = str(IMO)

    if len(IMO) != 7:
        return False

    result = 0
    i = 7
    while i != 1:
        result = result + i * int(IMO[-i])
        i = i - 1
    return True if str(result)[-1] == IMO[-1] else False

from ships_list.additional_functions.additional_functions \
    import append_JSON_file, id_generator, missing_arguments_checker
import json


def add_task(ship, task, stage, party):
    print('task planned to be added is ' + task +
          ' for ship {}'.format(ship))
    the_task = {'task_title': task,
                'ships_name': ship,
                'status': 'pending',
                'stage': stage,
                'party': party,
                'id': id_generator()}
    file = 'ships_list/lists/tasks.json'

    checked_results = the_task.copy()

    if missing_arguments_checker(checked_results) is False:
        print('Task has not been added.')
        return

    else:
        append_JSON_file(the_task, file)

        print('Task has been added.')

        with open("ships_list/lists/ships.json", "r") as a_file:
            list_of_ships_dictionaries = json.load(a_file)

        the_ship = list(filter(lambda x: True if x['name'] == ship else False,
                        list_of_ships_dictionaries))[0]
        the_ship["has_tasks"] = True
        the_ship["number_of_tasks"] += 1

        with open("ships_list/lists/ships.json", "w") as a_file:
            json.dump(list_of_ships_dictionaries, a_file, indent=4,
                      separators=(',', ': '))


def read_ships_list(ship, voyage):
    # result = ''
    # for task in the_list:
    #     print(result)
    pass

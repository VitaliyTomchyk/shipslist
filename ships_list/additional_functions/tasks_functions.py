from ships_list.additional_functions.additional_functions \
    import append_JSON_file, id_generator, missing_arguments_checker,\
    json_read, json_write, dictionary_finder


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

        ships_list = json_read("ships_list/lists/ships.json")
        the_ship = dictionary_finder(ships_list, ship, "ships_name")
        the_ship["has_tasks"] = True
        the_ship["number_of_tasks"] += 1
        json_write("ships_list/lists/ships.json", ships_list)


def read_tasks_list(ship):

    tasks_list = json_read("ships_list/lists/tasks.json")

    print(f'This are the tasks you have for ship {ship}:')

    for task in tasks_list:
        if task['ships_name'] == ship:
            print(f'-{task["task_title"]}')

    json_write("ships_list/lists/tasks.json", tasks_list)


def remove_task(id):

    tasks_list = json_read("ships_list/lists/tasks.json")
    ships_list = json_read("ships_list/lists/ships.json")
    i = 0
    while i < len(tasks_list):
        i += 1
        if str(tasks_list[i]["id"]) == str(id):
            ship = tasks_list[i]["ships_name"]
            the_ship = dictionary_finder(ships_list, ship, "ships_name")
            the_ship["number_of_tasks"] -= 1
            break
    del tasks_list[1]

    json_write("ships_list/lists/tasks.json", tasks_list)
    json_write("ships_list/lists/ships.json", ships_list)

from ships_list.additional_functions.additional_functions \
    import append_JSON_file, id_generator, input_option, \
    missing_arguments_checker, read_JSON_file, write_JSON_file, \
    dictionary_finder, input_item


def add_task():
    file_with_ships = 'ships_list/lists/ships.json.json'
    file_with_tasks = 'ships_list/lists/tasks.json'
    file_with_info = 'ships_list/lists/Standard/supporting_info.json'

    the_task = {'task_title': input_item('task title'),
                'ships_name': input_option(file_with_ships, 'ships_name',
                                           'ship\'s name'),
                'status': 'pending',
                'stage': input_option(file_with_info, 'stages', 'stage'),
                'party': input_option(file_with_info, 'parties', 'party'),
                'id': id_generator()}

    print('task planned to be added is ' + the_task['task_title'] +
          ' for ship {}'.format(the_task['ships_name']))

    checked_results = the_task.copy()

    if missing_arguments_checker(checked_results) is False:
        print('Task has not been added.')
        return

    else:
        append_JSON_file(the_task, file_with_tasks)
        print('Task has been added.')

        ships_list = read_JSON_file("ships_list/lists/ships.json")
        the_ship = dictionary_finder(ships_list, the_task['ships_name'],
                                     "ships_name")
        the_ship["has_tasks"] = True
        the_ship["number_of_tasks"] += 1
        write_JSON_file("ships_list/lists/ships.json", ships_list)


def read_tasks_list(ship):

    tasks_list = read_JSON_file("ships_list/lists/tasks.json")

    print(f'This are the tasks you have for ship {ship}:')

    for task in tasks_list:
        if task['ships_name'] == ship:
            print(f'-{task["task_title"]}')

    write_JSON_file("ships_list/lists/tasks.json", tasks_list)


def read_task(id):
    tasks = read_JSON_file('ships_list/lists/tasks.json')
    the_task = dictionary_finder(tasks, int(id), 'id')

    result = 'Task details are following\n'
    for key in the_task:
        result = result + "\n" + key + ':  ' + str(the_task[key])
    print(result + "\n")


def remove_task(id):

    tasks_list = read_JSON_file("ships_list/lists/tasks.json")
    ships_list = read_JSON_file("ships_list/lists/ships.json")
    i = 0
    while i < len(tasks_list):
        i += 1
        if str(tasks_list[i]["id"]) == str(id):
            print(f"Following task will be removed:\
            {tasks_list[i]['task_title']}")
            read_task(id)
            ship = tasks_list[i]["ships_name"]
            the_ship = dictionary_finder(ships_list, ship, "ships_name")
            the_ship["number_of_tasks"] -= 1
            break
    del tasks_list[i]

    write_JSON_file("ships_list/lists/tasks.json", tasks_list)
    write_JSON_file("ships_list/lists/ships.json", ships_list)


def redact_task(id):

    tasks_list = read_JSON_file("ships_list/lists/tasks.json")

    for task in tasks_list:
        if str(task["id"]) == str(id):
            print(f'Write the element you want to edit for \
\'{task["task_title"]}\':\n-', end='')
            element = input()

            if element in task:
                print(f'Write the new assingment for \
\'{element}\':\n-', end='')
                task[f'{element}'] = input()
            else:
                print(f'The is no such element in this task, \
in this task you have this list of elements:\n {list(task)}')
            break

    write_JSON_file("ships_list/lists/tasks.json", tasks_list)

from ships_list.additional_functions.additional_functions \
    import append_JSON_file, id_generator, missing_arguments_checker


def add_task(ship, task, stage, party):
    ship = ship.upper()
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


def read_ships_list(ship, voyage):
    # result = ''
    # for task in the_list:
    #     print(result)
    pass

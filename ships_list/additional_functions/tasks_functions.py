from ships_list.additional_functions.additional_functions \
    import append_JSON_file


def add_task(ship, task, stage, party):
    ship = ship.upper()
    print('task planned to be added is ' + task +
          ' for ship {}'.format(ship))
    the_task = {'task_title': task,
                'ships_name': ship,
                'status': 'pending',
                'stage': stage,
                'party': party,
                'id': 1}
    file = 'ships_list/lists/tasks.json'
    append_JSON_file(the_task, file)


def read_ships_list(ship, voyage):
    # result = ''
    # for task in the_list:
    #     print(result)
    pass

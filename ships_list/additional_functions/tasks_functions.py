from ships_list.additional_functions.additional_functions \
    import write_task_in_JSON


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
    write_task_in_JSON(the_task, file)


def read_ships_list(ship, voyage):
    # result = ''
    # for task in the_list:
    #     print(result)
    pass


def add_list():
    pass

from ships_list.additional_functions.additional_functions \
    import write_task_in_list

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
    write_task_in_list(the_task)


def read_ships_list(the_list):
    result = ''
    for task in the_list:
        print(result)

from ships_list.additional_functions.additional_functions \
    import id_generator, input_option, input_with_num,\
    missing_arguments_checker, dictionary_finder, input_item
from ships_list.lists.Standard.constats import TASKS_FILE, \
    SHIPS_FILE, LIST_OF_VOYAGES_FILE
from ships_list.additional_functions.json_functions import append_JSON_file, \
    read_JSON_file, write_JSON_file
from datetime import datetime


def add_task():

    the_task = {'task_title': input_item('task title'),
                'ships_name': input_with_num('ships_name', 'ship\'s name',
                                             SHIPS_FILE,),
                'status': 'pending',
                'stage': input_with_num('stages', 'stage'),
                'party': input_with_num('parties', 'party'),
                'id': id_generator(),
                'voyage_id': input_with_num('id', 'id', LIST_OF_VOYAGES_FILE),
                'time_mark_created': datetime.now().strftime("%Y-%m-%d " +
                                                             "%H:%M:%S"),
                'time_mark_closed': None
                }

    print('Task planned to be added is ' + the_task['task_title'] +
          ' for ship {}'.format(the_task['ships_name']))

    checked_results = the_task.copy()
    del checked_results['time_mark_closed']

    if missing_arguments_checker(checked_results) is False:
        print('Task has not been added.')
        return

    append_JSON_file(the_task, TASKS_FILE)
    print('Task has been added.')

    # amending details of ship to include added task
    update_ship(the_task)


def update_ship(the_task):
    ships_list = read_JSON_file(SHIPS_FILE)

    the_ship = dictionary_finder(ships_list, the_task['ships_name'],
                                 "ships_name")
    the_ship["has_tasks"] = True
    the_ship["number_of_tasks"] += 1

    write_JSON_file(SHIPS_FILE, ships_list)


def read_tasks_list(ship):
    tasks_list = read_JSON_file(TASKS_FILE)

    print(f'This are the tasks you have for ship {ship}:')

    for task in tasks_list:
        if task['ships_name'] == ship:
            print(f'-{task["task_title"]}')

    write_JSON_file(TASKS_FILE, tasks_list)


def read_task(id):
    the_task = dictionary_finder(TASKS_FILE, int(id), 'id')

    result = 'Task details are following\n'
    for key in the_task:
        result = result + "\n" + key + ':  ' + str(the_task[key])
    print(result + "\n")


def remove_task(id):

    tasks_list = read_JSON_file(TASKS_FILE)
    ships_list = read_JSON_file(SHIPS_FILE)
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

    write_JSON_file(TASKS_FILE, tasks_list)
    write_JSON_file(SHIPS_FILE, ships_list)


def redact_task(id):

    tasks_list = read_JSON_file(TASKS_FILE)

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

    write_JSON_file(TASKS_FILE, tasks_list)


def amend_task():

    id = input('Please put id of task you want to amend')

    tasks_list = read_JSON_file(TASKS_FILE)
    the_task = list(filter(lambda x: x['id'] == id, tasks_list))[0]

    key = input('Write the key you want to edit for ' +
                str(the_task["task_title"]))

    if key in the_task:
        the_task[key] = input('Write the new assingment for ' + key)
        write_JSON_file(TASKS_FILE, tasks_list)
    else:
        print('There is no such element in this task, \
              in this task you have this list of elements:\n {}' +
              list(the_task))

# not working yet


def close_task():
    # ship = input_option(SHIPS_FILE, 'ships_name', 'name of ship')
    # voyage = input_option(LIST_OF_VOYAGES_FILE, 'id', 'id of voyage')
    task_id = input_option(TASKS_FILE, 'id', 'id of task')
    time_mark = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

    list_of_tasks = read_JSON_file(TASKS_FILE)
    task = dictionary_finder(list_of_tasks, task_id, '')
    task['time_mark_closed'] = time_mark
    write_JSON_file(TASKS_FILE, list_of_tasks)

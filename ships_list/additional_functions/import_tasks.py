import json
from ships_list.additional_functions.additional_functions import list_to_string


def add_list(stage, party):
    voyage = None

    with open('ships_list/lists/supporting_files/standard_list.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]

    result = []
    for line in lines:
        dictionary = {'task_title': str(line[:-1]),
                      'serial_number': int(line[0]),
                      'stage': stage,
                      'party': party,
                      'status': 'Pending',
                      'voyage': voyage,
                      'ship': None}
        result.append(dictionary)

    with open('ships_list/lists/standard_list.json', 'r') as f:
        existing_list = json.load(f)

    updated_list = existing_list + result
    with open('ships_list/lists/standard_list.json', 'w') as f:
        json.dump(updated_list, f, indent=4, separators=(',', ': '))
    print('\n\nTasks for ' + party + ' at stage "' + stage + '" were added')
    print('Tasks are \n' + list_to_string(lines) + '\n\n')
    with open('ships_list/lists/supporting_files/standard_list.txt', 'w') as f:
        f.write('')

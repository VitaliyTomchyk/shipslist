import json

def add_list(stage):
    party = 'Master'
    voyage = None

    with open('ships_list/lists/standard_list.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]

    result = []
    for line in lines:
        dictionary = {'task_name': str(line[:-1]),
                      'serial_number': int(line[0]),
                      'stage': stage,
                      'party': party,
                      'status': 'Pending',
                      'voyage': voyage}
        result.append(dictionary)

    with open('ships_list/lists/standard_list.json', 'r') as f:
        existing_list = json.load(f)
    
    updated_list = existing_list + result
    with open('ships_list/lists/standard_list.json', 'w') as f:
        json.dump(updated_list, f, indent=4, separators=(',', ': '))
    print(updated_list)

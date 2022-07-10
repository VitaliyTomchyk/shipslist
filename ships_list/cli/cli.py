import argparse


def parcer():
    parser = argparse.ArgumentParser(description='Working with ship\'s list.')
    parser.add_argument('-add_ship', help='enter name of ship to be added')
    parser.add_argument('-ship', help='enter name of ship to work with')
    parser.add_argument('-IMO', help='put IMO number')
    parser.add_argument('-add_task', help='put name of task')
    parser.add_argument('-task_stage', help='''task stage: 1. Prior delivery
                                            2. After delivery
                                            3. Prior arrival at load port
                                            4. Load port
                                            5. Prior arrival Discharge port
                                            6. Discharge port
                                            7. After redelivery
                                            add only number of stage''')
    parser.add_argument('-task_party', help='''name or role task is related to
                                            1. Operator
                                            2. Owner
                                            3. Charterer
                                            4. Port agent
                                            5. Surveyor
                                            6. Master
                                            7. Other role
                                            add only number of party''')
    parser.add_argument('-remove_ship', help='removes ship from list based' +
                        ' on name of the ship')
    parser.add_argument('-add_list')

    added_ship = parser.parse_args().add_ship
    ships_name = parser.parse_args().ship
    task = parser.parse_args().add_task
    IMO = parser.parse_args().IMO
    task_stage = parser.parse_args().task_stage
    task_party = parser.parse_args().task_party
    ship_to_remove = parser.parse_args().remove_ship
    stage = parser.parse_args().add_list

    result = {'add_ship': bool(added_ship),
              'add_task': bool(task),
              'remove_ship': bool(ship_to_remove),
              'add_list': stage,
              'added_ship': added_ship,
              'ship': ships_name,
              'ship_to_remove': ship_to_remove,
              'IMO': IMO,
              'tasks_name': task,
              'task_stage': task_stage,
              'task_party': task_party}
    return result

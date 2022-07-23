import json
from ships_list.lists.Standard.constats import SUPPORTING_FILE


class Task():
    def __init__(self, title, stage, ship):
        self.ID = 1
        self.title = title
        self.stage = stage
        self.ship = ship
        self.status = 'Pending'

    def close_task(self):
        self.status = 'Done'

    def read_task(self):
        print('Task is \n{}\nShip is \n{}\n'.format(self.title, self.ship) +
              'Stage is \n{}\nStatus is {}').format(self.stage, self.status)


class Ship():
    def __init__(self, name, IMO):
        self.name = name
        self.IMO = IMO
        self.has_list = False
        self.list_related = None

    def set_list(self, name, lists_id):
        self.has_list = True
        self.list_related = lists_id

    def read_ship(self):
        print("Ship is {}\n IMO is {}\n Has list? {}".format(self.name,
                                                             self.IMO,
                                                             self.has_list))


class Ships_list():
    def __init__(self, name_of_ship, title_of_voyage):
        self.ships_list_id = 1
        self.name_of_list = title_of_voyage
        self.name_of_ship = name_of_ship

        with open(SUPPORTING_FILE, 'r') as f:
            standard_list = json.load(f)

        for task in standard_list:
            task["ship"] = name_of_ship

        self.task_list = standard_list

    def read_ships_list(self):
        print('Ships list name is \n{}'.format(self.name_of_list))
        print('Ships name is {}'.format(self.name_of_ship))
        print('Ships list \n{}'.format(self.task_list))

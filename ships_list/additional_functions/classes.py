import json


class Task():
    def __init__(self, title, stage, ship):
        self.title = title
        self.stage = stage
        self.ship = ship.upper()
        self.status = 'Open'

    def close_task(self):
        self.status = 'Closed'

    def read_task(self):
        print('Task is \n{}\n\nShip is \n{}'.format(self.title, self.ship) +
              '\n\nStage is \n{}\n\nStatus is:{}').format(self.stage,
                                                          self.status)


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

        with open('ships_list/lists/standrard_list.json', 'r') as f:
            standard_list = json.load(f)
        self.task_list = standard_list

    def read_ships_list(self):
        print('Ships list name is \n{}'.format(self.name_of_list))
        print('Ships name is {}'.format(self.name_of_ship))
        print('Ships list \n{}'.format(self.task_list))

class Task():
    def __init__(self, title, stage, ship):
        self.title = title
        self.stage = stage
        self.ship = ship.upper()
        self.status = 'Open'

    def close_task(self):
        self.status = 'Closed'


class Ship():
    name = ''
    IMO = ''


class Ships_list():
    pass

def add_ship(name, IMO):
    # open file
    # add ship
    print('ship planned to be added is {} with IMO {}'.format(name, IMO))


def add_task(name, IMO, task):
    # open file
    # add ship
    print('task planned to be added is ' + task +
          ' for ship {} with IMO {}'.format(name, IMO))


def IMO_checker(IMO):
    IMO = str(IMO)

    if len(IMO) != 7:
        return False

    result = 0
    i = 7
    while i != 1:
        result = result + i * int(IMO[-i])
        i = i - 1
    return True if str(result)[-1] == IMO[-1] else False

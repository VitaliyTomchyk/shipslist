from ships_list.additional_functions.supporting_functions.additional_functions\
    import list_to_string_with_breaks
from ships_list.lists.Standard.constants import POSITIONS_FILE, INDEXES_FILE
from ships_list.additional_functions.supporting_functions.json_functions \
    import append_JSON_file, read_JSON_file
from datetime import datetime


def add_position():

    ships_details = {"name": input('Name of ship: '),
                     "hire": input('Hire: '),
                     "index": input('Index: '),
                     "caliber": input('Caliber: '),
                     "type": input('Type of position:')}

    append_JSON_file(ships_details, POSITIONS_FILE)


# input of required position by user
def position_selector():

    # read file with positions
    positions = read_JSON_file(POSITIONS_FILE)

    # print list of names of positions
    print('Please select position from list below:')
    names_of_positions = list(map(lambda x: x['name'], positions))
    print(list_to_string_with_breaks(names_of_positions))

    # ask user to select position
    position_name = input('Position name: \n')

    # find index of selected position
    the_position = {}
    for position in positions:
        if position['name'] == position_name:
            the_position = position
            index_of_position = position['index']
            print('Position found. Index of position is: ' + index_of_position)
            print('\nHire of position in USD: ' + position['hire'])
            break
        else:
            print('Position not found')

    # TODO recalculate vessel's hire in USD based on today's index
    return the_position


# function opens file with positions, selects position based on name selscted
# by user and returns index of this position
def check_position_status():

    # input of required position by user
    the_position = position_selector()
    index_of_position = the_position['index']

    # return indexes
    indexes = read_JSON_file(INDEXES_FILE)

    # find today's index of selected position
    today_date = datetime.now().strftime("%d/%m/%Y")
    today_index = list(filter(lambda x: True if x['date'] == today_date \
        and x['name'] == index_of_position else False, indexes))[0]['value']

    # print today's index
    print('Today\'s index is: {}\n'.format(today_index))

    # calculate index equivalent in hire
    index_equivalet_in_hire = int(
        the_position['hire']) * (1 + int(the_position['caliber']) / 100)
    print('Index equivalent in hire in USD is: {}\n'.format(
        index_equivalet_in_hire))

    # calculate difference between today's index and index_equivalet_in_hire
    # of selected position
    difference = float(today_index) - index_equivalet_in_hire
    print('Difference between today\'s index and index ' +
          'equivalent in hire is: \n{}\n'.format(difference))

    return


def index_checker():
    return 

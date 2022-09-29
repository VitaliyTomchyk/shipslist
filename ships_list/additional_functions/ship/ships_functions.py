from ships_list.additional_functions.supporting_functions.additional_functions\
    import list_to_string_with_breaks, read_dict
from ships_list.lists.Standard.constants import SHIPS_FILE
from ships_list.additional_functions.supporting_functions.json_functions \
    import append_JSON_file, read_JSON_file, write_JSON_file
from ships_list.additional_functions.ship.additional_ship_functions import \
    add_parameter, voyages_assigned_checker, add_additional_consumption, \
    IMO_checker, add_stay_consumption


def print_ship():
    #     root = Tk()

    #     root['bg'] = '#fafafa'
    #     root.title('Printing ship\'s details')
    #     root.wm_attributes('-alpha', 0.8)
    #     root.geometry('400x400')

    #     canvas = Canvas(root)
    #     canvas.pack()

    #     frame = Frame(root)
    #     frame.place(relx=0.1, rely=0.1, relwidth=1, relheight=1)
    #     title = Label(frame, text='Please put name of ship')
    #     title.pack()

    #     # find_button = Button(frame, text='Find', font=20, bg='yellow')

    #     root.mainloop()
    return


def add_ship():

    name = input('Please enter ship\'s name\n').upper()

    IMO = int(input('Please enter IMO of the ship\n'))
    if IMO_checker(IMO) is False:
        return

    ships_details = {"ships_name": name.upper(),
                     "IMO": int(IMO)}

    ships_details = add_parameter(ships_details, 'speed')
    ships_details = add_parameter(ships_details, 'consumption')
    ships_details = add_additional_consumption(ships_details)
    ships_details = add_stay_consumption(ships_details, 'consumption')

    append_JSON_file(ships_details, SHIPS_FILE)
    print('Ship {} has been added.\n'.format(name.upper()))


# removes function from bata base
def remove_ship():

    list_of_ships = read_JSON_file(SHIPS_FILE)
    list_of_ships_names = list(map(lambda x: x['ships_name'], list_of_ships))
    list_of_names = list_to_string_with_breaks(list_of_ships_names)

    print('\nList of ships:\n' + list_of_names)

    ships_name = input('Please put ship\'s name you want to remove.').upper()

    if voyages_assigned_checker(ships_name):
        print('\nShip {} can not be removed due to voyage(s) '.format(
            ships_name) + 'assigned.')
        return

    for ship in list_of_ships:
        if ship['ships_name'] == ships_name:
            list_of_ships.remove(ship)
            write_JSON_file(SHIPS_FILE, list_of_ships)
            print('\nShip ' + ships_name + ' was removed.\n')
            return
    print('\nShip ' + ships_name + ' was not found')


def read_ship():
    # input of ship's name
    ships_name = input('\nPlease add ship\'s name\n').upper()

    # list of ships names
    list_of_ships = list(map(lambda x: x['ships_name'],
                             read_JSON_file(SHIPS_FILE)))

    # checker if ship exists
    if ships_name not in list_of_ships:
        print('\nShip ' + ships_name + ' is missing in list of ships.')
        return

    # reading ships from JSON file
    the_dict = list(filter(lambda x: x if x['ships_name'] == ships_name
                           else False, read_JSON_file(SHIPS_FILE)))[0]
    # printing ship's details
    print(read_dict(the_dict))

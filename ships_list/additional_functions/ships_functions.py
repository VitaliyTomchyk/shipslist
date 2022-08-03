from ships_list.additional_functions.additional_functions import IMO_checker, \
    list_to_string, list_of_val_by_key, read_dict
from ships_list.lists.Standard.constats import LIST_OF_VOYAGES_FILE, SHIPS_FILE
from ships_list.additional_functions.json_functions import read_JSON_file, \
    write_JSON_file
# from tkinter import Tk, Canvas, Label, Frame
# # Button


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


def ship_in_list_checker(name):
    list_of_ships = list(map(lambda x: x['ships_name'],
                             read_JSON_file(SHIPS_FILE)))

    if name in list_of_ships:
        print('Ship with this name and IMO is already in list, therefore, ' +
              'it will not be added again.')
        return True
    return False


def add_ship():
    name = input('\nShip adding function is activated\n' +
                 'Please enter name of the ship\n')
    IMO = input('Please enter IMO of the ship\n')

    if IMO_checker(IMO) is False:
        return

    if ship_in_list_checker(name):
        return

    ships_details = {"ships_name": name.upper(),
                     "IMO": int(IMO)}

    list_of_ships = read_JSON_file(SHIPS_FILE)
    list_of_ships.append(ships_details)

    write_JSON_file(SHIPS_FILE, list_of_ships)

    print('Ship {} has been added.\n'.format(name.upper()))


def voyages_assigned_checker(ship):
    list_of_dicts = read_JSON_file(LIST_OF_VOYAGES_FILE)
    ships_with_voyages = list(map(lambda x: x['ship'], list_of_dicts))
    if ship not in ships_with_voyages:
        return False
    return True


# removes function from bata base
def remove_ship():

    list_of_ships = read_JSON_file(SHIPS_FILE)
    list_of_names = list_to_string(list_of_val_by_key('ships_name',
                                                      list_of_ships).sort())
    print('\nList of ships:\n' + list_of_names)

    print('Please put ship\'s name.')
    ships_name = input().upper()

    if voyages_assigned_checker(ships_name):
        print('\nShip {} can not be removed due to voyage(s) '.format(
            ships_name) + 'assigned.')
        return

    for ship in list_of_ships:
        if ship['ships_name'] == ships_name:
            list_of_ships.remove(ship)
            write_JSON_file(SHIPS_FILE, list_of_ships)
            print('\nShip ' + ships_name + ' was removed.\n')
        else:
            print('\nShip ' + ships_name + ' was not found')


def read_ship():
    ships_name = input('\nPlease add ship\'s name\n').upper()
    try:
        the_dict = list(filter(lambda x: x if x['ships_name'] == ships_name
                               else False, read_JSON_file(SHIPS_FILE)))[0]
    except IndexError:
        print('Ship {} is missing in list of ships.'.format(ships_name))
        return
    read_dict(the_dict)

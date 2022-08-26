from ships_list.lists.Standard.constants import BOOKINGS_FILE
from ships_list.additional_functions.supporting_functions.json_functions \
    import amend_JSON_dict, read_JSON_file, append_JSON_file
from ships_list.additional_functions.supporting_functions.additional_functions\
    import list_to_ol_string, read_dict, list_to_string
from ships_list.additional_functions.booking.additional_functions \
    import booking_details_collector


def create_booking():
    # collecting details
    booking_details = booking_details_collector()

    # appending to bookings list in JSON file
    append_JSON_file(booking_details, BOOKINGS_FILE)

    # printing booking details
    print('\n\nBooking created with below details\n')
    print(read_dict(booking_details))


def read_booking():
    # collecting bookins from file
    bookings = read_JSON_file(BOOKINGS_FILE)

    # printing bookings
    print('Bookins are \n' + list_to_ol_string(bookings))

    # input of booking id to read
    booking_id = input('Please input booking id to read from bookings list\n')

    # printing booking details
    print(read_booking_details(bookings[int(booking_id) - 1]))
    return


def read_booking_details(the_booking):

    cargo_line = '\nBooking for {} mt MOL {}% of {}'.format(
        the_booking['cargo_quantity'],
        the_booking['allowance_of_cargo'],
        the_booking['name_of_cargo'])

    load_ports = [x['point_name'] for x in the_booking['points']['load']]
    discharge_ports = [x['point_name']
                       for x in the_booking['points']['discharge']]

    destination_line = 'From {} to {}'.format(list_to_string(load_ports),
                                              list_to_string(discharge_ports))

    lay_can_line = 'Lay can: {}'.format(the_booking['lay_can'])
    commission_line = 'Commissions: {}'.format(
        list_to_string(the_booking['commission']))
    result = '{}\n{}\n{}\n{}\n'.format(
        cargo_line,
        destination_line,
        lay_can_line,
        commission_line)

    return result


def remove_booking():
    bookings = read_JSON_file(BOOKINGS_FILE)
    print('Bookins are \n' + list_to_ol_string(bookings))
    booking_id = input('Please input booking id to remove from bookings list')
    del bookings[booking_id]
    amend_JSON_dict(bookings, BOOKINGS_FILE)
    return

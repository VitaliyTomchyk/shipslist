from ships_list.lists.Standard.constants import BOOKINGS_FILE
from ships_list.additional_functions.supporting_functions.json_functions \
    import amend_JSON_dict, read_JSON_file, append_JSON_file
from ships_list.additional_functions.supporting_functions.additional_functions\
    import list_to_ol_string
from ships_list.additional_functions.booking.additional_functions \
    import booking_details_collector, read_booking_details, \
    read_booking_details_list


def add_booking():
    # collecting details
    booking_details = booking_details_collector()

    # appending to bookings list in JSON file
    append_JSON_file(booking_details, BOOKINGS_FILE)

    # printing booking details
    print('\n\nBooking was created with below details:\n')
    print(read_booking_details(booking_details['id']))


def read_booking():
    # collecting bookins from file
    bookings = read_JSON_file(BOOKINGS_FILE)

    # printing bookings
    print('Bookings are \n' +
          list_to_ol_string(read_booking_details_list(bookings)))

    # input of booking id to read
    booking_id = input('Please input booking id to read from bookings list\n')

    # printing booking details
    print(read_booking_details(bookings[int(booking_id) - 1]))
    return


def remove_booking():
    bookings = read_JSON_file(BOOKINGS_FILE)
    print('Bookings are \n' + list_to_ol_string(bookings))
    booking_id = input('Please input booking id to remove from bookings list')
    del bookings[booking_id]
    amend_JSON_dict(bookings, BOOKINGS_FILE)
    return

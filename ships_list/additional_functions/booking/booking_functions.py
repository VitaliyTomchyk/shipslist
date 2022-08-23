from ships_list.lists.Standard.constants import BOOKINGS_FILE
from ships_list.additional_functions.supporting_functions.json_functions \
    import amend_JSON_dict, read_JSON_file
from ships_list.additional_functions.supporting_functions.additional_functions\
    import list_to_ol_string
from ships_list.additional_functions.booking.additiona_functions \
    import booking_details_collector


def create_booking():
    booking_details = booking_details_collector()
    amend_JSON_dict(booking_details, BOOKINGS_FILE)
    return


def read_booking():
    bookings = read_JSON_file(BOOKINGS_FILE)
    print('bookins are \n' + list_to_ol_string(bookings))
    booking_id = input('Please input booking id to read from bookings list')
    print(bookings[booking_id])
    return


def remove_booking():
    bookings = read_JSON_file(BOOKINGS_FILE)
    print('Bookins are \n' + list_to_ol_string(bookings))
    booking_id = input('Please input booking id to remove from bookings list')
    del bookings[booking_id]
    
    amend_JSON_dict(bookings, BOOKINGS_FILE)
    return

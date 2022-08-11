from ships_list.lists.Standard.constants import BOOKINGS_FILE
from ships_list.additional_functions.json_functions import amend_JSON_dict, \
    read_JSON_file
from ships_list.additional_functions.additional_functions \
    import id_generator, list_to_ol_string


def create_booking():
    booking_details = booking_details_collector()
    amend_JSON_dict(booking_details, BOOKINGS_FILE)
    return


def booking_details_collector():
    result = {'id': id_generator(),
              'name_of_argo': input('Please input cargo name'),
              'cargo_quantity': input('Please input quantity, mt'),
              'allowance_of_cargo': input('Please input allowance, %'),
              'from_point': input('Please input from point'),
              'to_point': input('Please input to point'),
              'type_of_commission': input('Please input type of commission'),
              'commission_rate': input('Please input commission rate, %'),
              }
    return result


def read_booking():
    bookings = read_JSON_file(BOOKINGS_FILE)
    print('bookins are \n' + list_to_ol_string(bookings))
    booking_id = input('Please input booking id to read from bookings list')
    print(bookings[booking_id])
    return


def remove_booking():
    bookings = read_JSON_file(BOOKINGS_FILE)
    print('bookins are \n' + list_to_ol_string(bookings))
    booking_id = input('Please input booking id to remove from bookings list')
    del bookings[booking_id]
    amend_JSON_dict(bookings, BOOKINGS_FILE)
    return

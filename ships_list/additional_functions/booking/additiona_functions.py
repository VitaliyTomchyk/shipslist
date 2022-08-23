from ships_list.additional_functions.supporting_functions.additional_functions\
    import id_generator


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
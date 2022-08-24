from ships_list.additional_functions.supporting_functions.additional_functions\
    import id_generator
from ships_list.additional_functions.supporting_functions.input_functions \
    import input_option_from_dict
from ships_list.lists.Standard.constants import SUPPORTING_FILE
from ships_list.additional_functions.supporting_functions \
    import check_percentage


def booking_details_collector():
    result = {'id': id_generator(),
              'name_of_argo': input('Please input cargo name'),
              'cargo_quantity': input('Please input quantity, mt'),
              'allowance_of_cargo': input('Please input allowance, %'),
              'points': input_points_detailed(),
              'type_of_commission': input('Please input type of commission'),
              'commission_rate': check_percentage(
        input('Please input commission rate, %')),
    }
    return result


def input_points_detailed():

    # input points
    points = []
    while True:

        point = {}
        # adding point parameter 'point_name'
        point['point_name'] = input(
            'Please put name of point, or push Enter to stop adding points\n')
        if point['point_name'] == '':
            break

        # adding point parameter 'point_type'
        point['point_type'] = input_option_from_dict(SUPPORTING_FILE,
                                                     'point_types',
                                                     'point type')

        # adding points with point
        points.append(point)

    return points

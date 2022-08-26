from ships_list.additional_functions.supporting_functions.additional_functions\
    import id_generator


def booking_details_collector():
    result = {'id': id_generator(),
              'name_of_cargo': input('\nPlease input cargo name\n'),
              'cargo_quantity': input('\nPlease input quantity, mt\n'),
              'allowance_of_cargo': input('\nPlease input allowance, %\n'),
              'points': input_points_short(),
              'commission': input_commissions_short(),
              'lay_can': input('\nPlease input lay can\n'),
              }
    return result


def input_commissions_short():
    # input points
    commissions = []

    quantity_of_points = input('Please input quantity of commissions\n')

    for i in range(int(quantity_of_points)):
        commission = {}
        # adding point parameter 'point_name'
        commission['type'] = input(
            'Please put name of commission type number {} from {}\n'.format(
                i + 1, quantity_of_points))

        commission['value'] = input(
            'Please put % of {} '.format(commission['type']) +
            "commission number {} of {}\n".format(i + 1,
                                                  quantity_of_points))
        commissions.append(commission)

    return commissions


def input_points_short():
    # input points
    points = input_point_short('load') | input_point_short('discharge')
    return points


def input_point_short(point_type):
    points = {point_type: []}

    quantity_of_points = input(
        'Please input quantity of {} ports\n'.format(point_type))
    for i in range(int(quantity_of_points)):
        point = {}
        # adding point parameter 'point_name'
        point['point_name'] = input(
            'Please put name of {} port number {}\n'.format(point_type, i + 1))

        points[point_type].append(point)

    return points

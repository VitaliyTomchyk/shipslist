from ships_list.additional_functions.bunker.point_consumption import \
    point_consumption_in_SECA, point_consumption_not_in_SECA
from ships_list.additional_functions.bunker.duration import \
    calculate_duration_of_leg, vessel_info_extractor


# adding bunker consumption to calculations
def add_consumption_calculation(calculations):
    points, legs, ship = calculations['points'], calculations['legs'],\
        calculations['ship']

    # adding bunker consumption to points
    consumption_at_points = {}
    for point in points:
        consumption_at_points[point['point_name']] = \
            point_consumption_in_SECA(point, ship) if point['in_SECA'] else \
            point_consumption_not_in_SECA(point, ship)

    # adding bunker consumption during steaming
    consumption_during_steaming = {}
    for leg in legs:
        consumption_during_steaming[leg['leg_type']] = \
            steaming_consumption_calculator(leg, ship)

    # # return dict with consumption at points and during steaming
    # return {'consumption_at_points': consumption_at_points,
    #         'consumption_during_steaming': consumption_during_steaming}

    print({'consumption_at_points': consumption_at_points,
           'consumption_during_steaming': consumption_during_steaming})


def steaming_consumption_calculator(leg, ship):

    # collecting distances
    duration_of_the_leg = calculate_duration_of_leg(leg, ship)

    # calculating speed
    speed_type_in_SECA = leg['only_SECA']['speed']
    speed_type_not_in_SECA = leg['total']['speed']

    # calculating total consumption in SECA by multiplying duration of the leg
    # by consumption rate
    consumption_SECA = consumption_in_SECA(
        leg, ship, duration_of_the_leg, speed_type_in_SECA)
    consumption_not_SECA = consumption_not_in_SECA(
        leg, ship, duration_of_the_leg, speed_type_not_in_SECA)

    result = {'IFO': consumption_not_SECA['IFO'],
              'MGO': consumption_SECA['MGO'] + consumption_not_SECA['MGO']}

    return result


# calculating consumption in SECA
def consumption_in_SECA(leg, ship, duration, speed_type):

    # collecting bunker consumption rates of the ship
    main_consumption_rate = vessel_info_extractor(leg, ship, speed_type,
                                                  'consumption')
    main_consumption = duration['in_SECA'] * \
        main_consumption_rate

    # calculating additional consumption in SECA by multiplying duration of
    # the leg
    additional_consumption_rate = float(
        ship['additional_consumption'])
    additional_consumption = duration['in_SECA'] * \
        additional_consumption_rate

    MGO_consumption = main_consumption + additional_consumption

    return {'IFO': 0,
            'MGO': MGO_consumption}


# calculating consumption not in SECA
def consumption_not_in_SECA(leg, ship, duration, speed_type):

    # collecting bunker consumption rates of the ship
    main_consumption_rate = vessel_info_extractor(leg, ship, speed_type,
                                                  'consumption')
    main_consumption = duration['not_in_SECA'] * \
        main_consumption_rate

    # calculating additional consumption not in SECA by multiplying duration
    # of the leg
    additional_consumption_rate = float(
        ship['additional_consumption'])
    additional_consumption = duration['not_in_SECA'] * \
        additional_consumption_rate

    return {'IFO': main_consumption,
            'MGO': additional_consumption}


# checker if summ at load port and discharge port is equal to total cargo
def checker_for_summ_of_cargo(points, total_cargo_quantity):

    summ = 0
    for point in points:
        if point['point_type'] in ['Load port', 'Discharge port']:
            summ += point['cargo_quantity_for_handling']

    if summ / 2 != total_cargo_quantity:
        print('\nSumm of cargo at load and discharge ports is not equal to' +
              ' total cargo quantity.\n')
        return False
    return True

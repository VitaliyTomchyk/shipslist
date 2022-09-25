def price_for_mile(speed_type, hire_info, ship, bunker_price):

    hire, hire_commission = hire_info
    duration = 1 / (int(ship['speed'][speed_type]) * 24)

    price_of_bunkers = duration * \
        ship['consumption'][speed_type] * bunker_price

    total_price = price_of_bunkers + duration * hire * (1 - hire_commission)

    return total_price


def compearing_speed_options(ships_details, bunker_price, speed_type,
                             hire_commission):

    ship, hire_rate = ships_details

    price_FULL_laden = price_for_mile(speed_type + '_full_speed', (hire_rate,
                                      hire_commission), ship, bunker_price)
    price_ECO_laden = price_for_mile(speed_type + '_eco_speed', (hire_rate,
                                     hire_commission), ship, bunker_price)
    return 'Full' if price_FULL_laden < price_ECO_laden else "Eco"


def optimal_speed_calculation(calculation, voyage_info):

    ships_details = (calculation['ship'], voyage_info['hire_rate'])
    bunker_prices, commission_on_hire = calculation['bunker_prices'], \
        voyage_info['commission_on_hire']

    optimal_speed = {}
    for leg_type in {'laden', 'ballast'}:
        optimal_speed[leg_type] = {}
        for SECA_type in {'in_SECA', 'not_SECA'}:
            bunker_type = 'IFO' if SECA_type != 'in_SECA' else 'MGO'
            optimal_speed[leg_type][SECA_type] = compearing_speed_options(
                ships_details,
                bunker_prices[bunker_type],
                'leg_type',
                commission_on_hire)

    # optimal_speed = {
    #     'laden': {
    #         'not_SECA': compearing_speed_options(
    #             ships_details,
    #             bunker_prices['IFO'],
    #             'laden',
    #             commission_on_hire),
    #         'in_SECA': compearing_speed_options(
    #             ships_details,
    #             bunker_prices['MGO'],
    #             'laden',
    #             commission_on_hire)},
    #     'ballast': {
    #         'not_SECA': compearing_speed_options(
    #             ships_details,
    #             bunker_prices['IFO'],
    #             'ballast',
    #             commission_on_hire),
    #         'in_SECA': compearing_speed_options(
    #             ships_details,
    #             bunker_prices['MGO'],
    #             'ballast',
    #             commission_on_hire)}}

    return optimal_speed

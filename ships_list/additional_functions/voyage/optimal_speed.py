# calculates basic price for 1 mile
def price_for_mile(leg_and_speed_type, hire_info, ship, bunker_price):

    # unpacking ship details
    consumption_type = leg_and_speed_type + '_consumption'
    hire, hire_commission = hire_info

    duration = 1 / (int(ship['speed'][consumption_type + "_speed"]) / 24)

    price_of_bunkers = duration * \
        ship['consumption'][consumption_type] * bunker_price

    total_price = price_of_bunkers + duration * hire * (1 - hire_commission)

    return total_price


# compares two options of speed and returns optimal
def compearing_speed_options(ships_details, bunker_price, leg_type,
                             hire_commission):

    # unpacking ships details
    ship, hire_rate = ships_details

    # calculating price for 1 mile for each speed option
    price_FULL_laden = price_for_mile(leg_type + '_full', (hire_rate,
                                      hire_commission), ship, bunker_price)
    price_ECO_laden = price_for_mile(leg_type + '_eco', (hire_rate,
                                     hire_commission), ship, bunker_price)

    return 'Full' if price_FULL_laden < price_ECO_laden else "Eco"


# calculates optimal speed for each leg type and SECA zone type
def speed_option(leg_type, calculation, voyage_info):

    the_ship = calculation['ship']

    ships_details = (the_ship, voyage_info['hire_rate'])
    bunker_prices, commission_on_hire = calculation['bunker_prices'], \
        voyage_info['commission_on_hire']

    # calculating optimal speed for each SECA zone type
    optimal_speed = {}
    for SECA_type in {'in_SECA', 'not_SECA'}:
        bunker_type = 'IFO' if SECA_type != 'in_SECA' else 'MGO'
        optimal_speed[SECA_type] = compearing_speed_options(
            ships_details,
            bunker_prices[bunker_type],
            leg_type,
            commission_on_hire)

    return optimal_speed


# calculates optimal speed for each leg type and SECA zone type
def optimal_speed_selector(calculation, voyage_info):

    selected_speed = {}
    for leg_type in {'laden', 'ballast'}:
        selected_speed[leg_type] = speed_option(leg_type, calculation,
                                                voyage_info)

    return selected_speed

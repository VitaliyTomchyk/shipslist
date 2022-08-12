def price_for_mile(speed_type, hire, ship, bunker_prices):
    duration = 1 / (ship['speed'][speed_type] * 24)
    price_of_bunkers = duration * \
        ship['consumption'][speed_type] * bunker_prices
    price_of_hire = duration * hire
    total_price = price_of_bunkers + price_of_hire
    return total_price


def compearing_speed_options(ships_details, bunker_prices, speed_type):
    ship, hire_rate = ships_details

    price_FULL_laden = price_for_mile(speed_type + '_full_speed', hire_rate,
                                      ship, bunker_prices)
    price_ECO_laden = price_for_mile(speed_type + '_eco_speed', hire_rate,
                                     ship, bunker_prices)
    return 'Full' if price_FULL_laden < price_ECO_laden else "Eco"


def optimal_speed_calculation(ships_details, bunker_prices):
    optimal_speed = {
        'laden': {
            'not_SECA': compearing_speed_options(
                ships_details, bunker_prices['IFO'], 'laden'),
            'in_SECA': compearing_speed_options(
                ships_details, bunker_prices['MGO'], 'laden')},
        'ballast': {
            'not_SECA': compearing_speed_options(
                ships_details, bunker_prices['IFO'], 'ballast'),
            'in_SECA': compearing_speed_options(
                ships_details, bunker_prices['MGO'], 'ballast')}}

    return optimal_speed

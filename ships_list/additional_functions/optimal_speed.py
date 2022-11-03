from ships_list.additional_functions.supporting_functions.json_functions \
    import read_JSON_file
from ships_list.lists.Standard.constants import SHIPS_FILE

# calculates basic price for 1 mile


def price_for_mile(leg_type, hire_info, ship, bunker_price):

    consumption_type = leg_type + '_consumption'
    hire, hire_commission = hire_info

    print('Ship is {}'.format(ship))
    print('ship consumption is {}'.format(ship['consumption']))
    print('ship consumption type is {}'.format(
        ship['consumption'][consumption_type]))
    duration = 1 / (int(ship['consumption'][consumption_type]) * 24)

    price_of_bunkers = duration * \
        ship['consumption'][consumption_type] * bunker_price

    total_price = price_of_bunkers + duration * hire * (1 - hire_commission)
    print(total_price)

    return total_price


def compearing_speed_options(ships_details, bunker_price, leg_type,
                             hire_commission):

    ship, hire_rate = ships_details

    price_FULL_laden = price_for_mile(leg_type + '_full', (hire_rate,
                                      hire_commission), ship, bunker_price)
    price_ECO_laden = price_for_mile(leg_type + '_eco', (hire_rate,
                                     hire_commission), ship, bunker_price)

    return 'Full' if price_FULL_laden < price_ECO_laden else "Eco"


def speed_option(leg_type, calculation, voyage_info):

    the_ship = filter(
        lambda ship: ship['ships_name'] == calculation['ship'],
        read_JSON_file(SHIPS_FILE))
    ships_description = list(the_ship)[0]

    ships_details = (ships_description, voyage_info['hire_rate'])
    bunker_prices, commission_on_hire = calculation['bunker_prices'], \
        voyage_info['commission_on_hire']

    optimal_speed = {}
    for SECA_type in {'in_SECA', 'not_SECA'}:
        bunker_type = 'IFO' if SECA_type != 'in_SECA' else 'MGO'
        optimal_speed[SECA_type] = compearing_speed_options(
            ships_details,
            bunker_prices[bunker_type],
            leg_type,
            commission_on_hire)

    print('Optimal speed is \n{}'.format(str(optimal_speed)))

    return optimal_speed


def optimal_speed_calculation(calculation, voyage_info):

    optimal_speed = {}
    for leg_type in {'laden', 'ballast'}:
        optimal_speed[leg_type] = speed_option(leg_type, calculation,
                                               voyage_info)

    return optimal_speed

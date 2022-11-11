from ships_list.additional_functions.booking.additional_functions \
    import input_booking_short
import math

from ships_list.additional_functions.booking.booking_functions \
    import add_booking
# function checker_for_to_use returns booking information if input is 'y' else
# returns None


def checker_for_booking_to_use():
    if input('\nDo you want to use existing booking? (y/n)\n') == 'y':
        option = input_booking_short()
        return option
    return add_booking()

# functions summs all values in list of dicts under key 'value'


def summ_commitions(booking_info):
    commissions = booking_info['commission']
    list_of_values = [float(comm['value']) for comm in commissions]
    return math.fsum(list_of_values)


# function commition_calculator returns input() if booking_id is None else
# returns booking_id['commition']
def commition_calculator(booking_info=None):
    return summ_commitions(booking_info)


def cargo_quantity_calculator(booking_info=None):
    if booking_info is None:
        return int(input('Quantity of cargo, mt\n'))
    else:
        return booking_info['cargo_quantity']


def add_voyage_details(booking_info=None):
    # adding voyage details to input information
    input_information = {
        "freight_rate": int(input('\nPlease input freight rate, USD\n')),
        "commission_on_freight": commition_calculator(booking_info),
        "cargo_quantity": booking_info['cargo_quantity'],

        "hire_rate": int(input('Hire rate, USD per day\n')),
        "commission_on_hire":
            float(input('Commition on hire, %\n').replace(',', '.')) / 100,
        'booking_info': booking_info
    }
    return input_information


def sum_bunkers_cost(input_information):
    return sum([cost['price']
                for cost in input_information['bunker_consumption']])


def total_calculator(rate, base, persentage):
    return round(rate * base * (1 - persentage), 2)


def additional_costs_collector(input_information):
    additional_costs = []
    while True:
        cost = {
            "name": input('\nPlease input name of additional cost\n'),
            "price": int(
                input('\nPlease input price of additional cost\n'))}
        additional_costs.append(cost)
        if input('Do you want to add another cost? (y/n)\n') == 'n':
            break
    input_information['additional_costs'] = additional_costs
    return additional_costs

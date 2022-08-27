from ships_list.additional_functions.supporting_functions.input_functions \
    import input_option
from ships_list.lists.Standard.constants import BOOKINGS_FILE


# function checker_for_to_use returns booking information if input is 'y' else
# returns None
def checker_for_booking_to_use():
    if input('Do you want to use existing booking? (y/n)\n') == 'y':
        option = input_option(BOOKINGS_FILE, 'id', 'id of booking')
        return option

# functions summs all values in list of dicts under key 'value'


def summ_commitions(booking_info):
    commissions = booking_info['commitions']
    list_of_values = [commission['value'] for commission in commissions]
    return sum(list_of_values)


# function commition_calculator returns input() if booking_id is None else
# returns booking_id['commition']
def commition_calculator(booking_info=None):
    if booking_info is None:
        return int(input('Total commition on freight, %\n')) / 100
    else:
        return summ_commitions(booking_info)


def cargo_quantity_calculator(booking_info=None):
    if booking_info is None:
        return int(input('Quantity of cargo, mt\n'))
    else:
        return booking_info['cargo_quantity']


def add_voyage_details(booking_info=None):
    # adding voyage details to input information
    input_information = {
        "freight_rate": int(input('Input freight rate, USD per mt\n')),
        "commition_on_freight": commition_calculator(booking_info),
        "cargo_quantity": cargo_quantity_calculator(booking_info),

        "hire_rate": int(input('Hire rate, USD per day\n')),
        "commition_on_hire": int(input('Commition on hire, %\n')) / 100,
        'booking_info': booking_info
    }
    return input_information


def sum_bunkers_price(input_information):
    return sum([cost['price']
                for cost in input_information['bunker_consumption']
                ['additional_costs']])


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

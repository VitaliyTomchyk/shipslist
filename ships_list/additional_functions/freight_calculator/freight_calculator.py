from ships_list.additional_functions.bunker.bunker_consumption \
    import calculate_bunkers_consumption
from ships_list.additional_functions.freight_calculator.additional_functions \
    import add_voyage_details, sum_bunkers_price, total_calculator, \
    additional_costs_collector


def freight_calculator():
    # TODO hire rate should be collected in one place
    # adding voyage details to input information
    input_information = add_voyage_details()

    # calculating total cost of bunker consumption
    input_information = calculate_bunkers_consumption(input_information)
    total_bunkers_price = sum_bunkers_price(input_information)

    # calculating total cost of freight
    total_freight = total_calculator(input_information['freight_rate'],
                                     input_information['cargo_quantity'],
                                     input_information['commition_on_freight'])

    # calculating total cost of additional costs
    input_information = additional_costs_collector(input_information)
    total_additional_costs = sum(
        [cost['price'] for cost in input_information['additional_costs']])

    # calculating total cost of hire
    total_hire = total_calculator(
        input_information['bunker_consumption']['hire_rate'],
        input_information['bunker_consumption']['total_duration'],
        input_information['commition_on_hire'])

    # calculating total cost of voyage
    total_expanses = total_hire + total_additional_costs + total_bunkers_price

    # calculating profit
    profit = round(total_freight - total_expanses, 2)
    daily_profit = round(profit / input_information['duration'], 2)

    print('Voyage profit is expected to be USD {}.\n'.format(profit))
    print('Daily profit is expected to be USD {}.\n'.format(daily_profit))

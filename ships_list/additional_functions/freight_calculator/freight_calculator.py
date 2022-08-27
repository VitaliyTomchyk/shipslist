from ships_list.additional_functions.bunker.bunker_consumption \
    import calculate_bunkers_consumption
from ships_list.additional_functions.freight_calculator.additional_functions \
    import add_voyage_details, sum_bunkers_price, total_calculator, \
    additional_costs_collector, checker_for_booking_to_use
from ships_list.lists.Standard.constants import \
    FREIGHT_CALCULATIONS_FILE
from ships_list.additional_functions.supporting_functions.json_functions \
    import append_JSON_file


def freight_calculator():
    booking_info = checker_for_booking_to_use()

    # TODO hire rate should be collected in one place
    # adding voyage details to input information
    voyage_info = add_voyage_details(booking_info)

    # calculating total cost of bunker consumption
    voyage_info = calculate_bunkers_consumption(voyage_info)
    total_bunkers_price = sum_bunkers_price(voyage_info)

    # calculating total cost of freight
    total_freight = total_calculator(voyage_info['freight_rate'],
                                     voyage_info['cargo_quantity'],
                                     voyage_info['commition_on_freight'])

    # calculating total cost of additional costs
    voyage_info = additional_costs_collector(voyage_info)
    total_additional_costs = sum(
        [cost['price'] for cost in voyage_info['additional_costs']])

    # calculating total cost of hire
    total_hire = total_calculator(
        voyage_info['bunker_consumption']['hire_rate'],
        voyage_info['bunker_consumption']['total_duration'],
        voyage_info['commition_on_hire'])

    # calculating total cost of voyage
    total_expanses = total_hire + total_additional_costs + total_bunkers_price

    # calculating profit
    profit = round(total_freight - total_expanses, 2)
    daily_profit = round(
        profit /
        voyage_info['bunker_consumption']['total_duration'],
        2)

    print('Voyage profit is expected to be USD {}.\n'.format(profit))
    print('Daily profit is expected to be USD {}.\n'.format(daily_profit))

    # appending JSON file FREIGHT_CALCULATIONS_FILE with voyage_info
    append_JSON_file(FREIGHT_CALCULATIONS_FILE, voyage_info)


# create a function to read freight calculation result
def read_calculation(voyage_info):

    print('Voyage details are:')
    print('Ship: {}'.format(voyage_info['ship']))
    print('Hire rate: {} USD'.format(voyage_info['hire_rate']))
    print('Cargo quantity: {}'.format(voyage_info['cargo_quantity']))
    print('Commition on freight: {}%'.format(
        voyage_info['commition_on_freight']))
    print('Commition on hire: {}%'.format(
        voyage_info['commition_on_hire']))
    print('Freight rate: {} USD'.format(voyage_info['freight_rate']))
    # print('Total duration: {} days'.format(
    #     voyage_info['bunker_consumption']['total_duration']))
    # print('Total cost of bunker consumption: {} USD'.format(
    #     total_bunkers_price))
    # print('Total cost of freight: {} USD'.format(total_freight))
    # print('Total cost of additional costs: {} USD'.format(
    #     total_additional_costs))
    # print('Total cost of hire: {} USD'.format(total_hire))
    # print('Total cost of voyage: {} USD'.format(total_expanses))
    # print('Profit: {} USD'.format(profit))
    # print('Daily profit: {} USD'.format(daily_profit))
    print('\n')

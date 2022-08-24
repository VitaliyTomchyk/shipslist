from ships_list.additional_functions.bunker.bunker_consumption \
    import calculate_bunkers_consumption
from ships_list.additional_functions.freight_calculator.additional_functions \
    import add_voyage_details, sum_bunkers_price, total_calculator, \
    additional_costs_collector
from ships_list.lists.Standard.constants import \
    FREIGHT_CALCULATIONS_FILE
from ships_list.additional_functions.supporting_functions.json_functions \
    import append_JSON_file


def freight_calculator(input_information=None):
    # TODO hire rate should be collected in one place
    # adding voyage details to input information
    if input_information is None:
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
    daily_profit = round(
        profit /
        input_information['bunker_consumption']['total_duration'],
        2)

    print('Voyage profit is expected to be USD {}.\n'.format(profit))
    print('Daily profit is expected to be USD {}.\n'.format(daily_profit))

    # appending JSON file FREIGHT_CALCULATIONS_FILE with input_information
    append_JSON_file(FREIGHT_CALCULATIONS_FILE, input_information)


# create a function to read freight calculation result
def read_calculation(input_information):

    print('Voyage details are:')
    print('Ship: {}'.format(input_information['ship']))
    print('Hire rate: {} USD'.format(input_information['hire_rate']))
    print('Cargo quantity: {}'.format(input_information['cargo_quantity']))
    print('Commition on freight: {}%'.format(
        input_information['commition_on_freight']))
    print('Commition on hire: {}%'.format(
        input_information['commition_on_hire']))
    print('Freight rate: {} USD'.format(input_information['freight_rate']))
    # print('Total duration: {} days'.format(
    #     input_information['bunker_consumption']['total_duration']))
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

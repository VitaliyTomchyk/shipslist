from ships_list.additional_functions.bunker.bunker_consumption \
    import calculate_bunkers_consumption


def add_voyage_details():
    # adding voyage details to input information
    input_information = {
        "freight_rate": int(input('Input freight rate, USD per mt\n')),
        "commition_on_freight": int(input('Commition on freight, %\n')) / 100,
        "cargo_quantity": int(input('Quantity of cargo, mt\n')),

        "hire_rate": int(input('Hire rate, USD per day\n')),
        "commition_on_hire": int(input('Commition on hire, %\n')) / 100,
        "duration": int(input('Duration of voyage, days\n'))
    }
    return input_information


def freight_calculator():

    # adding voyage details to input information
    input_information = add_voyage_details()

    # calculating total cost of freight
    total_freight = total_calculator(input_information['freight_rate'],
                                     input_information['cargo_quantity'],
                                     input_information['commition_on_freight'])

    # calculating total cost of hire
    total_hire = total_calculator(input_information['hire_rate'],
                                  input_information['duration'],
                                  input_information['commition_on_hire'])

    # calculating total cost of additional costs
    additional_costs_info = additional_costs_collector()
    total_additional_costs = sum([cost['price']
                                  for cost in additional_costs_info])

    # calculating total cost of bunker consumption
    bunker_consumption_info = calculate_bunkers_consumption()
    total_bunkers_price = bunker_consumption_info['total_price_of_bunkers']

    # calculating total cost of voyage
    total_expanses = total_hire + total_additional_costs + total_bunkers_price

    # calculating profit
    profit = round(total_freight - total_expanses, 2)
    daily_profit = round(profit / input_information['duration'], 2)

    print('Voyage profit is expected to be USD {}.\n'.format(profit))
    print('Daily profit is expected to be USD {}.\n'.format(daily_profit))


def total_calculator(rate, base, persentage):
    return round(rate * base * (1 - persentage), 2)


def additional_costs_collector():
    additional_costs = []
    while True:
        cost = {
            "name": input('\nPlease input name of additional cost\n'),
            "price": int(
                input('\nPlease input price of additional cost\n'))}
        additional_costs.append(cost)
        if input('Do you want to add another cost? (y/n)\n') == 'n':
            break
    return additional_costs

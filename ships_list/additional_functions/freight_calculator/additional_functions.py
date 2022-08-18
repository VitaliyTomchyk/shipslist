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

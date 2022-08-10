def add_voyage_details(result):
    return result


def freight_calculator():

    input_information = {
        "freight_rate": int(input('Input freight rate, USD per mt\n')),
        "commition_on_freight": int(input('Commition on freight, %\n')) / 100,
        "cargo_quantity": int(input('Quantity of cargo, mt\n')),

        "hire_rate": int(input('Hire rate, USD per day\n')),
        "commition_on_hire": int(input('Commition on hire, %\n')) / 100,
        "duration": int(input('Duration of voyage, days\n'))
    }
    input_information = add_voyage_details(input_information)

    total_freight = total_calculator(input_information['freight_rate'],
                                     input_information['cargo_quantity'],
                                     input_information['commition_on_freight'])

    total_hire = total_calculator(input_information['hire_rate'],
                                  input_information['duration'],
                                  input_information['commition_on_hire'])

    profit = round(total_freight - total_hire, 2)
    daily_profit = round(profit / input_information['duration'], 2)

    print('Voyage profit is expected to be USD {}.\n'.format(profit))
    print('Daily profit is expected to be USD {}.\n'.format(daily_profit))

    return profit


def total_calculator(rate, base, persentage):
    return round(rate * base * (1 - persentage), 2)

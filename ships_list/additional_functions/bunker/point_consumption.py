def point_consumption_in_SECA(point, ship):

    # MGO consumption during working days
    MGO_consumption_working = point['working_days'] * \
        ship['stay_consumption']['working']

    # MGO consumption during idle days
    MGO_consumption_idle = point['idle_days'] * \
        ship['stay_consumption']['idle']

    # additional MGO consumption
    MGO_consumption_additional = \
        point['working_days'] * ship['additional_consumption']['working'] + \
        point['idle_days'] * ship['additional_consumption']['idle']

    # total MGO consumption
    MGO_consumption_total = MGO_consumption_working + \
        MGO_consumption_idle + MGO_consumption_additional

    consumption_at_point = {
        'IFO': 0,
        'MGO': MGO_consumption_total
    }
    return consumption_at_point


def point_consumption_not_in_SECA(point, ship):
    # IFO consumption during working days
    IFO_consumption_working = point['working_days'] * \
        ship['stay_consumption']['working']

    # IFO consumption during idle days
    IFO_consumption_idle = point['idle_days'] *\
        ship['stay_consumption']['idle']

    # total IFO consumption
    IFO_consumption_total = IFO_consumption_working + IFO_consumption_idle

    # MGO consumption during working days
    MGO_additional_consumption_working = point['working_days'] * \
        ship['additional_consumption']['working']

    # MGO consumption during idle days
    MGO_additional_consumption_idle = point['idle_days'] * \
        ship['additional_consumption']['idle']

    # total MGO consumption
    MGO_consumption_total = MGO_additional_consumption_working + \
        MGO_additional_consumption_idle

    # calculating IFO and MGO consumption in point
    consumption_at_point = {
        'IFO': IFO_consumption_total,
        'MGO': MGO_consumption_total
    }

    return consumption_at_point

def point_consumption_in_SECA(point, ship):
    # calculating IFO consumption in point
    IFO_consumption_total = 0

    # MGO consumption during working days
    MGO_consumption_working = point['working_days'] * \
        ship['working_main_bunker']
    # MGO consumption during idle days
    MGO_consumption_idle = point['idle_days'] * ship['idle_main_bunker']

    # additional MGO consumption
    MGO_consumption_additional = \
        point['working_days'] * ship['working_auxiliary_bunker'] + \
        point['idle_days'] * ship['idle_auxiliary_bunker']

    # total MGO consumption
    # calculating IFO consumption in point
    IFO_consumption_total = 0

    # MGO consumption during working days
    MGO_consumption_working = point['working_days'] * \
        ship['working_main_bunker']
    # MGO consumption during idle days
    MGO_consumption_idle = point['idle_days'] * ship['idle_main_bunker']

    # additional MGO consumption
    MGO_consumption_additional = \
        point['working_days'] * ship['working_auxiliary_bunker'] + \
        point['idle_days'] * ship['idle_auxiliary_bunker']

    # total MGO consumption
    MGO_consumption_total = MGO_consumption_working + \
        MGO_consumption_idle + MGO_consumption_additional

    consumption_at_point = {
        'IFO': IFO_consumption_total,
        'MGO': MGO_consumption_total
    }
    return consumption_at_point


def point_consumption_not_in_SECA(point, ship):
    # IFO consumption during working days
    IFO_consumption_working = point['working_days'] * \
        ship['working_main_bunker']
    # IFO consumption during idle days
    IFO_consumption_idle = point['idle_days'] * ship['idle_main_bunker']
    # total IFO consumption
    IFO_consumption_total = IFO_consumption_working + IFO_consumption_idle

    # MGO consumption during working days
    MGO_additional_consumption_working = point['working_days'] * \
        ship['working_auxiliary_bunker']
    # MGO consumption during idle days
    MGO_additional_consumption_idle = point['idle_days'] * \
        ship['idle_auxiliary_bunker']
    # total MGO consumption
    MGO_consumption_total = MGO_additional_consumption_working + \
        MGO_additional_consumption_idle

    # calculating IFO and MGO consumption in point
    consumption_at_point = {
        'IFO': IFO_consumption_total,
        'MGO': MGO_consumption_total
    }

    return consumption_at_point


# calculator of IFO and MGO consupmtion in point returns dict
def point_consumption_calculator(point, ship):

    options = {
        'True': point_consumption_in_SECA,
        'False': point_consumption_not_in_SECA}

    return options[str(point['SECA'])](point, ship)

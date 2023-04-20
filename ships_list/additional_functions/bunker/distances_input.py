from ships_list.additional_functions.supporting_functions.input_functions \
    import input_option_from_dict
from ships_list.lists.Standard.constants import SUPPORTING_FILE
from ships_list.additional_functions.bunker.weather.weather_functions \
    import add_weather_factor


# add distance to points for in_SECA = False or True
def add_distances(points):

    print('\nPlease put distance between points in nautical miles.')

    legs = []

    # adding distances between points
    for i in range(len(points) - 1):
        the_leg = {}
        for marker_SECA, dist_type in [('total', 'total'),
                                       ('only SECA', 'only_SECA')]:
            the_points = [points[i], points[i + 1]]
            the_leg[dist_type] = sub_leg_generator(the_points, marker_SECA,
                                                   dist_type)
            # generating leg type
            the_leg['leg_type'] = add_leg_condition(points[i], points[i + 1])
        legs.append(the_leg)

    return legs


def sub_leg_generator(points, marker_SECA, dist_type):

    from_point, to_point = points[0], points[1]
    text = 'Please put {} distance \n- from {} {} to {} {}\n'
    request = text.format(
        marker_SECA,
        points[0]['point_type'],
        from_point['point_name'],
        points[1]['point_type'],
        to_point['point_name'])

    distance = int(input(request))

    speed = add_speed_type(distance)
    wf = add_weather_factor(distance, dist_type)

    return {'distance': distance,
            'speed': speed,
            'wf': wf}


def add_leg_condition(point_from, point_to):
    # Define dictionaries to store conditions and condition checkers.
    laden_conditions = {
        'Load port': True,
        'Discharge port': False,
        'Delivery point': False,
        'Redelivery point': False
    }
    ballast_conditions = {
        'Load port': False,
        'Discharge port': False,
        'Delivery point': True,
        'Redelivery point': True
    }

    # Check if leg is laden or ballast.
    if laden_conditions.get(point_from['point_type'], False) or \
            laden_conditions.get(point_to['point_type'], False):
        return 'laden'
    elif ballast_conditions.get(point_from['point_type'], False) or \
            ballast_conditions.get(point_to['point_type'], False):
        return 'ballast'

    # Ask user to specify vessel condition for the leg.
    text = "Please specify the condition of the vessel for the leg\n- " + \
        f"from {point_from['point_name']} to {point_to['point_name']}\n"
    print(text)
    condition = input_option_from_dict(
        SUPPORTING_FILE,
        'vessel_condition',
        'condition of vessel')
    return condition


def add_speed_type(distance):
    if distance == 0:
        return 'full'

    return input_option_from_dict(
        SUPPORTING_FILE, 'speed_types', 'speed type')

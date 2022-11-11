def wf_setter(distance):
    output_text = 'Please put weather factor for leg' + \
        ' from {} to {}'.format(distance['description']['from'],
                                distance['description']['to'])

    result = {'distance_only_SECA': {},
              'distance_total': {}}

    if distance['distance_only_SECA']['distance'] != 0:
        result['distance_only_SECA']['WF'] = \
            int(input(output_text + ' in SECA, %\n'))
    else:
        result['distance_only_SECA']['WF'] = 0

    if distance['distance_total']['distance'] > \
            distance['distance_in_SECA']['distance']:
        result['distance_total']['WF'] = int(input(output_text +
                                                   'excluding SECA, %\n'))
    else:
        result['distance_total']['WF'] = 0

    return result


def add_weather_factor(distances):
    result = list(map(wf_setter, distances))
    return result

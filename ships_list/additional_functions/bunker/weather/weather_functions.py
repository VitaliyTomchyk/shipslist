def wf_setter(distance, text):

    if distance['distance_in_SECA'] != 0:
        distance['wf_in_SECA'] = int(input(text + ' in SECA, %\n'))
    else:
        distance['wf_in_SECA'] = 0

    if distance['distance_total'] > distance['distance_in_SECA']:
        distance['wf_excluding_SECA'] = int(input(text +
                                                  'excluding SECA, %\n'))
    else:
        distance['wf_excluding_SECA'] = 0

    return distance


def add_weather_factor(distances):
    for distance in distances:
        text = 'Please put weather factor for leg' + \
            ' from {} to {}'.format(distance['from'], distance['to'])
        distance = wf_setter(distance, text)
    return distances

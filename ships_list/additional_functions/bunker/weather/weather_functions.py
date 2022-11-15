def add_weather_factor(distance, dist_type):

    output_text = 'Please put weather factor for leg' + \
        ' from {} to {} in {}, %\n'.format(distance['from'],
                                           distance['to'],
                                           dist_type)

    return float(input(output_text)) if distance['distance'] != 0 else 0

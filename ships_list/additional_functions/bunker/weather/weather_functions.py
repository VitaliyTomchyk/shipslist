def add_weather_factor(distance, dist_type):

    output_text = 'Please put weather factor for leg' + \
        ' in {}, %\n'.format(dist_type)

    return float(input(output_text)) if distance != 0 else 0

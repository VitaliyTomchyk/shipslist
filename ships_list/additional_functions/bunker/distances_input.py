# add distance to points for in_SECA = False or True
def add_distance(points):
    print('\nPlease put distance between points in nautical miles.')
    distances = []
    for i in range(len(points) - 1):
        for marker_SECA, port_of_key in [('only SECA', 'only_SECA'),
                                         ('total', 'including_SECA')]:
            text = 'Please put {} distance from {} {} to {} {}\n'
            request = text.format(
                marker_SECA,
                points[i]['point_type'],
                points[i]['point_name'],
                points[i + 1]['point_type'],
                points[i + 1]['point_name'])

            the_distance = {}
            the_distance['distance_' + port_of_key] = int(input(request))
            the_distance['description'] = {'from': points[i]['point_name'],
                                           'to': points[i + 1]['point_name']}
    return distances

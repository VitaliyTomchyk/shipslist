from datetime import datetime

fixture_input = ['POpy'] + list(range(1, 12))

fixture_output = ["Please enter ship's name\n",      
                      'Please enter IMO of the ship\n',      
                      '\nPlease add full laden speed of the ship, kn\n',      
                      '\nPlease add eco laden speed of the ship, kn\n',      
                      '\nPlease add full ballast speed of the ship, kn\n',      
                      '\nPlease add eco ballast speed of the ship, kn\n',      
                      '\nPlease add full laden consumption of the ship,' +  
                      ' mt/day\n',      
                      '\nPlease add eco laden consumption of the ship,' + 
                      ' mt/day\n',      
                      '\nPlease add full ballast consumption of the ship,' +  
                      ' mt/day\n',      
                      '\nPlease add eco ballast consumption of the ship,' +  
                      ' mt/day\n',      
                      '\nPlease add additional consumption during' +  
                      ' port_stay, mt of MGO\n',      
                      '\nPlease add additional consumption during steaming,' +  
                      ' mt of MGO\n',      
                      'Ship POPY has been added.\n']
fixture_diff = [{
        'ships_name': "POPY",
        'IMO': 1,
        'additional_consumption': {'port_stay': 10,
                                   'steaming': 11},
        'speed': {'laden_full_speed': 2,
                  'laden_eco_speed': 3,
                  'ballast_full_speed': 4,
                  'ballast_eco_speed': 5,
                  'date_of_update': '{:%Y-%m-%d}'.format(datetime.now())},
        'consumption': {
                  'laden_full_consumption': 6,
                  'laden_eco_consumption': 7,
                  'ballast_full_consumption': 8,
                  'ballast_eco_consumption': 9,
                  'date_of_update': '{:%Y-%m-%d}'.format(datetime.now())}}]
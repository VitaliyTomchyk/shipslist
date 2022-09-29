from datetime import datetime

fixture_input = ['POpy'] + list(range(1, 14))

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
                      ' idle, mt of MGO\n',      
                      '\nPlease add additional consumption during working,' +  
                      ' mt of MGO\n',      
                      '\nPlease add main consumption in idle condition' +  
                      ', mt of MGO\n',      
                      '\nPlease add main consumption in working condition,' +  
                      ' mt of MGO\n',
                      'Ship POPY has been added.\n']
fixture_diff = [{
        'ships_name': "POPY",
        'IMO': 1,
        'additional_consumption': {'idle': 10.0,
                                   'working': 11.0},
        'speed': {'laden_full_speed': 2.0,
                  'laden_eco_speed': 3.0,
                  'ballast_full_speed': 4.0,
                  'ballast_eco_speed': 5.0,
                  'date_of_update': '{:%Y-%m-%d}'.format(datetime.now())},
        'consumption': {
                  'stay_consumption': 
                        {'idle': 12.0,
                        'working': 13.0},
                  'laden_full_consumption': 6.0,
                  'laden_eco_consumption': 7.0,
                  'ballast_full_consumption': 8.0,
                  'ballast_eco_consumption': 9.0,
                  'date_of_update': '{:%Y-%m-%d}'.format(datetime.now())}}]
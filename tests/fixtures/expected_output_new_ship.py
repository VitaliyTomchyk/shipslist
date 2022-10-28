from datetime import datetime

fixture_input = ['POpy'] + list(range(1, 14))

fixture_output = ["Please enter ship's name\n",      
                      'Please enter IMO of the ship\n',      
                      '\n\nParameter speed will be added now.',
                      '\nPlease add full laden speed of the ship, kn\n',      
                      '\nPlease add eco laden speed of the ship, kn\n',      
                      '\nPlease add full ballast speed of the ship, kn\n',      
                      '\nPlease add eco ballast speed of the ship, kn\n',
                      '\n\nParameter consumption will be added now.',      
                      '\nPlease add full laden consumption of the ship,' +  
                      ' mt/day\n',      
                      '\nPlease add eco laden consumption of the ship,' + 
                      ' mt/day\n',      
                      '\nPlease add full ballast consumption of the ship,' +  
                      ' mt/day\n',      
                      '\nPlease add eco ballast consumption of the ship,' +  
                      ' mt/day\n',    
                      'Port stay consumption will be added now.',
                      '\nPlease add main consumption in idle condition, mt\n',
                      '\nPlease add main consumption in working condition, mt\n',

                      'Additional consumption will be added now.',
                      '\nPlease add additional consumption during' +  
                      ' steaming, mt of MGO\n',      
                      '\nPlease add additional consumption during at_port,' +  
                      ' mt of MGO\n',  

                      '\nShip POPY has been added.\n']
fixture_diff = [{
        'ships_name': "POPY",
        'IMO': 1,
        'additional_consumption': {'at_port': 13.0,
                                   'steaming': 12.0},
        'speed': {'laden_full_speed': 2.0,
                  'laden_eco_speed': 3.0,
                  'ballast_full_speed': 4.0,
                  'ballast_eco_speed': 5.0,
                  'date_of_update': '{:%Y-%m-%d}'.format(datetime.now())},
        'consumption': {
                  'stay_consumption': 
                        {'idle': 10.0,
                        'working': 11.0},
                  'laden_full_consumption': 6.0,
                  'laden_eco_consumption': 7.0,
                  'ballast_full_consumption': 8.0,
                  'ballast_eco_consumption': 9.0,
                  'date_of_update': '{:%Y-%m-%d}'.format(datetime.now())}}]
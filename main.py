'''

'''

import googlemaps
import json
from datetime import datetime

gmaps = googlemaps.Client(key='')

home = ''
work = ''

now = datetime.now()
commute_time = gmaps.distance_matrix(home,
                                     work,
                                     mode='driving',
                                     avoid='tolls',
                                     departure_time=now)

with open('commute_time.json', 'w') as file:
    json.dump(commute_time, file, indent=4)

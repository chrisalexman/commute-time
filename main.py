'''

'''

import credentials
import locations

import googlemaps
import os
import json
from datetime import datetime


gmaps = googlemaps.Client(key=credentials.api_key)

# get commute time with traffic, store in json file
def get_commute_time():
    home = locations.origin
    work = locations.destination

    now = datetime.now()
    commute_time = gmaps.distance_matrix(home,
                                        work,
                                        mode='driving',
                                        avoid='tolls',
                                        departure_time=now)

    with open('commute_time.json', 'w') as file:
        json.dump(commute_time, file, indent=4)


if __name__ == '__main__':
    get_commute_time()

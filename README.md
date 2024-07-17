# commute-time

A basic script to estimate the commute time between my home and work using the [Google Maps Python API](https://github.com/googlemaps/google-maps-services-python), stores the output in a json file.

## Example Output

The result of using the [Distance Matrix API](https://developers.google.com/maps/documentation/distance-matrix/) calculation, shows duration with and without traffic.

```
{
    "destination_addresses": ["<WORK ADDRESS>"],
    "origin_addresses": ["<HOME ADDRESS>"],
    "rows": [
        {
            "elements": [
                {
                    "distance": { "text": "121 km", "value": 121116 },
                    "duration": { "text": "1 hour 19 mins", "value": 4768 },
                    "duration_in_traffic": { "text": "1 hour 11 mins", "value": 4285 },
                    "status": "OK"
                }
            ]
        }
    ],
    "status": "OK"
}
```

# Divvy Bikes

import json
from urllib.request import urlopen
import math

webservice_url = "http://www.divvybikes.com/stations/json"
data = urlopen(webservice_url).read().decode("utf8")
result = json.loads(data)
stations = result['stationBeanList']

young_latitude = 41.793414
young_longitude = -87.600915

nearest_distance = 100000  # Assume something very far out

for station in stations:
  station_latitude = float(station['latitude'])
  station_longitude = float(station['longitude'])

  latitude_delta = math.fabs(station_latitude - young_latitude)
  longitude_delta = math.fabs(station_longitude - young_longitude)
  distance_from_young = math.sqrt(latitude_delta*latitude_delta + longitude_delta*longitude_delta)

  if distance_from_young < nearest_distance:
    nearest_station = station
    nearest_distance = distance_from_young


print("The nearest station is:", nearest_station['stationName'])
print("There are", nearest_station['availableBikes'], "bikes there right now, if you run for it!")

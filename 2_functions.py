import json
from urllib.request import urlopen

chicago = None

def get_airport_info(airport_code):
  # print(sport)
  if chicago == None:
    url = "http://services.faa.gov/airport/status/" + airport_code + "?format=application/json"
    data = urlopen(url).read().decode()
    chicago = json.loads(data)

  return chicago

def get_city_for(airport_code):
  result = get_airport_info(airport_code)
  return result['city']

def get_temperature_at(airport_code):
  get_airport_info(airport_code)
  return result['weather']['temp']

def get_wind_at(airport_code):
  get_airport_info(airport_code)
  return result['weather']['wind']

  pass


city_name = get_city_for('ORD')
print("ORD serves the city of", city_name)

temperature = get_temperature_at('ORD')
print("The temperature is:", temperature)

wind_report = get_wind_at('ORD')
print("The wind is:", wind_report)



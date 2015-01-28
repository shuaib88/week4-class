# Classes vs. instances; instance methods and attributes.
import json
from urllib.request import urlopen

class Airport:

  def __init__(self):
    self.code = "ORD"
    self.latitude = None

  def get_info(self):
    airport_code = self.code
    url = "http://services.faa.gov/airport/status/" + airport_code + "?format=application/json"
    data = urlopen(url).read().decode()
    result = json.loads(data)
    return result

  def get_temperature(self, units):
    result = self.get_info()
    return result['weather']['weather']

  def city(self):
    result = self.get_info()
    return result['city']



def main()
  my_airport = Airport()
  my_airport.temp = 55
  print(my_airport.latitude)
  print("My airport's FAA code is", my_airport.code)

  city_name = my_airport.city()
  print("My airport serves the city of", city_name)

  your_airport = Airport()
  your_airport.code = "MKE"
  print(your_airport.city())

  temperature = my_airport.get_temperature('F')
  print("At my airport, the temperature is:", temperature)

  # wind_report = my_airport.get_wind_at()
  # print("The weather is:", wind_report)

main()


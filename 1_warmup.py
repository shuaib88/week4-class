# 1. Checkout these websites first:
#
# http://www.fly.faa.gov/flyfaa/usmap.jsp
# http://services.faa.gov/docs/services/
# http://services.faa.gov/docs/basics/

import json
from urllib.request import urlopen


# 2. Display the city and weather information at each airport:
#
# ORD (Chicago): The temperature is 30.0 F (-1.1 C), and the wind is Northeast at 8.1mph.
# LAX (Los Angelese): The temperature is 65.0 F (18.3 C), and the wind is Variable at 4.6mph.
# etc.

# Here's a function to help you get started:

def get_airport_info(airport_code):
  # print(sport)
  url = "http://services.faa.gov/airport/status/" + airport_code + "?format=application/json"
  data = urlopen(url).read().decode()
  result = json.loads(data)
  return result

def get_weather(airport_code):
  sport = "hockey"
  get_airport_info(airport_code)


get_weather("ORD")


# TO DO: Write your code here.  Feel free to modify the code above, too.
#
# ORD (Chicago): The temperature is 30.0 F (-1.1 C), and the wind is Northeast at 8.1mph.
airport_codes = ['ORD', 'SFO', 'JFK', 'LGA', 'PHL', 'LAX', 'EWR', 'TEB', 'BOS']

for airport_code in airport_codes:
  info = get_airport_info(airport_code)
  print(airport_code, "(" + info['city'] + ")", "The temperature is", info['weather']['temp'], "and the wind is",
    info['weather']['wind'])












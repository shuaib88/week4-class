# 1. Checkout these websites first:
#
# http://www.fly.faa.gov/flyfaa/usmap.jsp
# http://services.faa.gov/docs/services/
# http://services.faa.gov/docs/basics/

import json
from urllib.request import urlopen

airport_codes = ['ORD', 'SFO', 'JFK', 'LGA', 'PHL', 'LAX', 'EWR', 'TEB', 'BOS']

# 2. Display the city and weather information at each airport:
#
# ORD (Chicago): The temperature is 30.0 F (-1.1 C), and the wind is Northeast at 8.1mph.
# LAX (Los Angelese): The temperature is 65.0 F (18.3 C), and the wind is Variable at 4.6mph.
# etc.

# Here's a function to help you get started:

def get_airport_info(airport_code):
  url = "http://services.faa.gov/airport/status/" + airport_code + "?format=application/json"
  data = urlopen(url).read().decode()
  result = json.loads(data)
  return result

# TO DO: Write your code here.  Feel free to modify the code above, too.
#



# 1. Checkout these websites first:
#
# http://www.fly.faa.gov/flyfaa/usmap.jsp
# http://services.faa.gov/docs/services/
# http://services.faa.gov/docs/basics/

import json
from urllib.request import urlopen

airport_codes = ['ORD', 'SFO', 'JFK', 'LGA', 'PHL', 'LAX', 'EWR', 'TEB', 'BOS']

# 2. Display the current delay at each airport:
#
# ORD: 15-30 minutes
# SFO: No delay
# JFK: 1 hour
# etc.

# Here's a function to help you get started:

def get_airport_info(airport_code):
  url = "http://services.faa.gov/airport/status/" + airport_code + "?format=application/json"
  data = urlopen(url).read().decode()
  result = json.loads(data)
  return result

# TO DO: Write your code here.  Feel free to modify the code above, too.
#



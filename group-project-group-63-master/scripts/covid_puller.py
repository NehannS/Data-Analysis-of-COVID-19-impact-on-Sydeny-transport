import requests
from io import StringIO

url = "https://data.nsw.gov.au/data/dataset/97ea2424-abaf-4f3e-a9f2-b5c883f42b6a/resource/2776dbb8-f807-4fb2-b1ed-184a6fc2c8aa/download/confirmed_cases_table4_location_likely_source.csv"

req = requests.get(url)

with open("../data/covid_nsw_data.csv", "w") as covid_data:
	covid_data.write(req.text);

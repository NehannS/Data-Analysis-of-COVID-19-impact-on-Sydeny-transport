import pandas as pd
import urllib.request

url = "https://www.ausstats.abs.gov.au/ausstats/subscriber.nsf/0/DC124D1DAC3D9FDDCA25825D000F9267/$File/2033055001%20-%20poa%20indexes.xls"
urllib.request.urlretrieve(url, "../data/seifa.xls")

seifa_overview_data = pd.read_excel("../data/seifa.xls", sheet_name=1, header=[4,5], skipfooter=2)
seifa_overview_data.to_csv("../data/seifa_overview_data.csv", index=False)

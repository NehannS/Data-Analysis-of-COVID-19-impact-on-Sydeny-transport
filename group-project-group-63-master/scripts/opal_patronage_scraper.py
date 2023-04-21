import requests
import datetime
import pandas as pd
from io import StringIO

# To pull the data automatically, the requests must provide a referer from the OpenData website
headers = {"referer": "https://opendata.transport.nsw.gov.au/"}

# The url will contain the appropriate variables substituted into {} when used
url = "https://tfnsw-prod-opendata-tpa.s3-ap-southeast-2.amazonaws.com/Opal_Patronage/2020-{date:%m}/Opal_Patronage_2020{date:%m}{date:%d}.txt"

# daterange will contain all dates from the patronage data that we want
date_range = pd.date_range(start='2020-01-01', end='2020-10-22', freq='D', closed='left')

main_df = pd.DataFrame()
for single_date in date_range:
	req = requests.get(url.format(date=single_date), headers=headers)
	df = pd.read_csv(StringIO(req.text), sep='|')

	# remove data that is not from buses or trains
	df = df[df['mode_name'].isin(["Bus", "Train"])]

	# add the data to the main dataframe for later use
	main_df = main_df.append(df)

main_df = main_df.reset_index()
main_df = main_df.drop(columns="index")
main_df.info()

main_df.to_csv("../data/opal_patronage_data.csv", index=False)

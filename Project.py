# Importing Data in this case API

import requests
data = requests.get("https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD,EUR"
                  ).json()
print(data)

# Import a CSV file into a Pandas DataFrame

import pandas as pd
df = pd.read_csv("GDP.csv")
df_2018 = df.sort_values('2018', ascending=False)
modifieddf=df_2018.fillna(" ")
print(modifieddf)













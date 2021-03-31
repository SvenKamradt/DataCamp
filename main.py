import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# Reading Data
covid_vaccination = pd.read_csv("country_vaccinations.csv")
print(covid_vaccination.head())

# Exploring Data
covid_vaccination.info()
info_covid = covid_vaccination.isnull().sum()
print(info_covid)

# How many distinct countries are available
countries_list = covid_vaccination.country.unique()
print(countries_list)

vaccine_df = covid_vaccination[covid_vaccination['country'].isin(countries_list)].fillna(0)
vaccine_df.head(100)
print(vaccine_df)

# sorting data

percent_vacc = vaccine_df.groupby(['country'], sort=False, as_index=False)['people_vaccinated_per_hundred'] \
.max() \
.sort_values(by='people_vaccinated_per_hundred', ascending=False)
print(percent_vacc)

percent_fvacc = vaccine_df.groupby(['country'], sort=False, as_index=False)['people_fully_vaccinated_per_hundred'] \
.max() \
.sort_values(by='people_fully_vaccinated_per_hundred', ascending=False)
print(percent_fvacc)

# Joining Dataframes

precent_vacc_f_vacc = percent_vacc.merge(percent_fvacc, how='outer', on='country').fillna(0)
print(precent_vacc_f_vacc)

percent_vacc = precent_vacc_f_vacc.groupby(['country'], sort=False)['people_vaccinated_per_hundred'].max()
print(percent_vacc)

percent_fvacc = precent_vacc_f_vacc.groupby(['country'], sort=False)['people_fully_vaccinated_per_hundred'].max()
print(percent_fvacc)

# Graphs Matplotlib


ax = percent_vacc.iloc[:15].plot(kind='bar', figsize=(10,6), color="green", fontsize=10,)
ax = percent_fvacc.iloc[:15].plot(kind='bar', figsize=(10,6), color="yellow", fontsize=10,)

ax.grid(which='major',zorder=1, alpha=0.5)
ax.grid(which='minor', alpha=1)

ax.legend()
ax.set_alpha(0.2)
ax.set_title("15 Most progressed countries for Covid vaccinations", fontsize=18)
ax.set_ylabel("Percent", fontsize=12)
ax.set_xlabel("Country", fontsize=12);
plt.show()

# Graphs Seaborn

df_confirmed = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
df_deaths = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
df_recoveries = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
df_latest = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/01-23-2021.csv')

print(df_confirmed.head())
print(df_recoveries.head())
print(df_latest.head())

dates = df_confirmed.columns[4:]
print(dates)

top_10_con = df_confirmed.iloc[:,[1,-1]].sort_values(by=dates[-1],ascending =False)[:10]
top_10_con.columns = ['Country/Region','Total Confirmed']
top_10_con=top_10_con.reset_index().drop('index',axis=1)
print(top_10_con)

sns.barplot(x='Country/Region',y='Total Confirmed',data=top_10_con)
plt.title('Top 10 Countries-Total Confirmed')
plt.show()




# Example Relational Database or API or Web Scraping in this case Cryptocurrencies Exchange rates.
# Ethereum vs USD/EUR and Bitcoin

import requests

data = requests.get("https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD,EUR"
                    ).json()
print(data)

# Numpy example

import numpy as np
print(np.__version__)
print(np.array([1, 4, 2, 5, 3]))


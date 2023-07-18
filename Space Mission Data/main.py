import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate

# These might be helpful:
from iso3166 import countries
from datetime import datetime, timedelta


df_data = pd.read_csv('mission_launches.csv')

df_data.duplicated()
cdf = df_data.dropna()

cdf.columns
cdf = cdf.drop(columns=['Unnamed: 0.1', 'Unnamed: 0'])

#--------------------- Who has launched the most missions ------------------------------------

num_launches = cdf.groupby('Location').count().sort_values(by=['Detail'], ascending=False)
num_launches

fig = px.histogram(num_launches, x=num_launches.index, y="Detail")
fig.show()

# ------------------------- How has cost of space missions changed over time? ---------------------------------------
cdf_date = cdf
new_dates = []
for date in cdf_date['Date']:
  date_split = date.split()
  new_date = int(date_split[3])
  new_dates.append(new_date)

cdf_date["New Date"] = new_dates

#cdf_date["Price"] = cdf_date["Price"].str.replace(',', '')
print(cdf_date["Price"].dtype)

cdf_date["Price"] = pd.to_numeric(cdf_date["Price"])

print(type(cdf_date["Price"]))
cdf_date["avg_price"] = cdf_date.groupby('New Date')['Price'].transform(sum)


fig = plt.plot(cdf_date['New Date'], cdf_date.avg_price)
plt.xlabel("Year")
plt.ylabel("Cost ($Billion)")
plt.show(fig)

# ------------------ Most Popular months for launches -------------------------------------

cdf_date2 = cdf

new_dates_month = []
for date in cdf_date['Date']:
  date_split = date.split()
  new_date = date_split[1].split(',')
  new_date2 = new_date[0]
  new_dates_month.append(new_date2)

cdf_date2["Month"] = new_dates_month
cdf_date2.Month.value_counts()

ax = cdf_date2.Month.value_counts().sort_values().plot(kind='bar', ylabel="Number of Launches", xlabel="Month")
ax.bar_label(ax.containers[0]) # shows frequency above bar

# -------------- How the failure rate of launches has changed over time --------------------------------

cdf_d = cdf
cdf_d.Mission_Status.value_counts()
#cdf_d['failure_rate'] = cdf_d.groupby('Mission Status').value_counts()
#cdf_date['failure_rate'] = cdf_date.groupby('New Date')['Mission_Status'['Mission_Status' != 'Success']].transform('count')

failures = cdf_date[cdf_date.Mission_Status != 'Success']
failures.groupby('New Date')['Mission_Status'].value_counts()
ax = failures['New Date'].value_counts().sort_index().plot(kind='bar', ylabel="Number of Failures", xlabel="Year")   # sort_index sorts the x axis
ax.bar_label(ax.containers[0])
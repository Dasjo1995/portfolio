import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate

# These might be helpful:
from iso3166 import countries
from datetime import datetime, timedelta


df_hh_income = pd.read_csv('Median_Household_Income_2015.csv', encoding="windows-1252")
df_pct_poverty = pd.read_csv('Pct_People_Below_Poverty_Level.csv', encoding="windows-1252")
df_pct_completed_hs = pd.read_csv('Pct_Over_25_Completed_High_School.csv', encoding="windows-1252")
df_share_race_city = pd.read_csv('Share_of_Race_By_City.csv', encoding="windows-1252")
df_fatalities = pd.read_csv('Deaths_by_Police_US.csv', encoding="windows-1252")


df_fatalities.fillna(0)


# Graph
df_pct_poverty.groupby['Geographic Area'].sort_values(by=['poverty_rate'])

df_pct_poverty.groupby['Geographic Area'].value_countspoverty_rate

plt.bar(df_pct_poverty['Geographic Area'], df_pct_poverty.poverty_rate)
plt.xticks(rotation = 90)
plt.yticks(rotation = 45)
plt.show()


# Chart the Poverty Rate in each US State
poverty_sorted = df_pct_poverty.sort_values('poverty_rate')
top_poverty_states = poverty_sorted[-5:]

plt.bar(top_poverty_states['Geographic Area'], top_poverty_states.poverty_rate)
plt.xticks(rotation = 90)
plt.yticks(rotation = 45)
plt.show()
# Chart the High School Graduation Rate by US State
df_pct_completed_hs.percent_completed_hs.value_counts()

# df_pct_completed_hs.percent_completed_hs = df_pct_completed_hs.percent_completed_hs.str.replace('-', 'none')
df_pct_completed_hs.percent_completed_hs.value_counts()

df_pct_completed_hs = df_pct_completed_hs[df_pct_completed_hs.percent_completed_hs != 'none']
df_pct_completed_hs.percent_completed_hs.value_counts()

df_pct_completed_hs.percent_completed_hs = pd.to_numeric(df_pct_completed_hs.percent_completed_hs)
sorted = df_pct_completed_hs.sort_values('percent_completed_hs')

average_grad_state = sorted.groupby('Geographic Area').agg(
    {'percent_completed_hs': pd.Series.mean})  # Creates mean for percentage of graduates per State
avg_g_s_sorted = average_grad_state.sort_values('percent_completed_hs')

plt.figure(figsize=(14, 8), dpi=120)
plt.bar(avg_g_s_sorted.index, avg_g_s_sorted.percent_completed_hs)
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.show()
# Visualise the Relationship between Poverty Rates and High School Graduation Rates

# Now use a Seaborn .jointplot() with a Kernel Density Estimate (KDE) and/or scatter plot to visualise the same relationship
plt.figure(figsize=(14, 8), dpi=200)

with sns.axes_style('whitegrid'):  # With .jointplot you can show both a scatterplot and histogram is one graph
    sns.jointplot(avg_g_s_sorted,
                  x='Geographic Area',
                  y='percent_completed_hs')

plt.xticks(rotation=90)
plt.show()
# Seaborn's .lmplot() or .regplot() to show a linear regression between the poverty ratio and the high school graduation ratio.
average_grad_state = sorted.groupby('Geographic Area').agg({'percent_completed_hs': pd.Series.mean})

#df_pct_poverty.poverty_rate = df_pct_poverty.poverty_rate.str.replace('-', 'none')  # Replaces each '-' with 'none
df_pct_poverty = df_pct_poverty[df_pct_poverty.poverty_rate != 'none']    # Updates column with all none values dropped

df_pct_poverty.poverty_rate = pd.to_numeric(df_pct_poverty.poverty_rate)  # Converts strings to numeric
sorted_p = df_pct_poverty.sort_values('poverty_rate')                     # Sorts the values

average_pov_state = sorted_p.groupby('Geographic Area').agg({'poverty_rate': pd.Series.mean})   # Creates mean values of poverty for each state

merged_pov_grad = pd.merge(average_grad_state, average_pov_state, on=['Geographic Area'])
merged_pov_grad



plt.figure(figsize=(8,4), dpi=200)                              # Creates a regression plot
with sns.axes_style('whitegrid'):
  sns.regplot(merged_pov_grad, x='percent_completed_hs', y='poverty_rate')

plt.show()
# Create a Bar Chart with Subsections Showing the Racial Makeup of Each US State
# ---------------- Create average of white share for state ---------------------

#df_share_race_city.share_white = df_share_race_city.share_white.str.replace('-', 'none')  # Replaces each '-' with 'none
#df_share_race_city.share_white = df_share_race_city.share_white.str.replace('(X)', 'none')
#df_share_race_city.share_white = df_share_race_city.share_white.str.replace('(none)', 'none')

#df_share_race_city = df_share_race_city[df_share_race_city.share_white != 'none']    # Updates column with all none values dropped
#df_share_race_city = df_share_race_city[df_share_race_city.share_white != '(none)']
#df_share_race_city = df_share_race_city[df_share_race_city.share_white != '(X)']

df_share_race_city.share_white = pd.to_numeric(df_share_race_city.share_white)  # Converts strings to numeric
sorted_white = df_share_race_city.sort_values('share_white')


avg_share_white = df_share_race_city.groupby('Geographic area').agg({'share_white': pd.Series.mean})

# ---------------- Create average of black share for state ---------------------

#df_share_race_city.share_black = df_share_race_city.share_black.str.replace('-', 'none')  # Replaces each '-' with 'none
#df_share_race_city.share_black = df_share_race_city.share_black.str.replace('(X)', 'none')
#df_share_race_city.share_black = df_share_race_city.share_black.str.replace('(none)', 'none')

#df_share_race_city = df_share_race_city[df_share_race_city.share_black != 'none']    # Updates column with all none values dropped
#df_share_race_city = df_share_race_city[df_share_race_city.share_black != '(none)']
#df_share_race_city = df_share_race_city[df_share_race_city.share_black != '(X)']

df_share_race_city.share_black = pd.to_numeric(df_share_race_city.share_black)  # Converts strings to numeric
sorted_black = df_share_race_city.sort_values('share_black')

avg_share_black = df_share_race_city.groupby('Geographic area').agg({'share_black': pd.Series.mean})

# ---------------- Create average of native_american share for state ---------------------

'''
df_share_race_city.share_native_american = df_share_race_city.share_native_american.str.replace('-', 'none')  # Replaces each '-' with 'none
df_share_race_city.share_native_american = df_share_race_city.share_native_american.str.replace('(X)', 'none')
df_share_race_city.share_native_american = df_share_race_city.share_native_american.str.replace('(none)', 'none')

df_share_race_city = df_share_race_city[df_share_race_city.share_native_american != 'none']    # Updates column with all none values dropped
df_share_race_city = df_share_race_city[df_share_race_city.share_native_american != '(none)']  
df_share_race_city = df_share_race_city[df_share_race_city.share_native_american != '(X)'] 
'''
df_share_race_city.share_native_american = pd.to_numeric(df_share_race_city.share_native_american)  # Converts strings to numeric
sorted_native_american = df_share_race_city.sort_values('share_native_american')

avg_share_native_american = df_share_race_city.groupby('Geographic area').agg({'share_native_american': pd.Series.mean})

# ---------------- Create average of asian share for state ---------------------

'''
df_share_race_city.share_asian = df_share_race_city.share_asian.str.replace('-', 'none')  # Replaces each '-' with 'none
df_share_race_city.share_asian = df_share_race_city.share_asian.str.replace('(X)', 'none')
df_share_race_city.share_asian = df_share_race_city.share_asian.str.replace('(none)', 'none')

df_share_race_city = df_share_race_city[df_share_race_city.share_asian != 'none']    # Updates column with all none values dropped
df_share_race_city = df_share_race_city[df_share_race_city.share_asian != '(none)']  
df_share_race_city = df_share_race_city[df_share_race_city.share_asian != '(X)'] 
'''
df_share_race_city.share_asian = pd.to_numeric(df_share_race_city.share_asian)  # Converts strings to numeric
sorted_asian = df_share_race_city.sort_values('share_asian')

avg_share_asian = df_share_race_city.groupby('Geographic area').agg({'share_asian': pd.Series.mean})

# ---------------- Create average of hispanic share for state ---------------------

'''
df_share_race_city.share_hispanic = df_share_race_city.share_hispanic.str.replace('-', 'none')  # Replaces each '-' with 'none
df_share_race_city.share_hispanic = df_share_race_city.share_hispanic.str.replace('(X)', 'none')
df_share_race_city.share_hispanic = df_share_race_city.share_hispanic.str.replace('(none)', 'none')

df_share_race_city = df_share_race_city[df_share_race_city.share_hispanic != 'none']    # Updates column with all none values dropped
df_share_race_city = df_share_race_city[df_share_race_city.share_hispanic != '(none)']  
df_share_race_city = df_share_race_city[df_share_race_city.share_hispanic != '(X)'] 
'''
df_share_race_city.share_hispanic = pd.to_numeric(df_share_race_city.share_hispanic)  # Converts strings to numeric
sorted_hispanic = df_share_race_city.sort_values('share_hispanic')

avg_share_hispanic = df_share_race_city.groupby('Geographic area').agg({'share_hispanic': pd.Series.mean})

merged_shares1 = avg_share_white.join(avg_share_black)
merged_shares2 = merged_shares1.join(avg_share_asian)
merged_shares3 = merged_shares2.join(avg_share_native_american)
merged_shares4 = merged_shares3.join(avg_share_hispanic)
merged_shares4

plt.figure(figsize=(8,4), dpi=200)

fig = px.bar(merged_shares4, x=merged_shares4.index, y=['share_white', 'share_black', 'share_asian', 'share_native_american', 'share_hispanic'], title="Long-Form Input")

fig.show()

# Create Donut Chart by of People Killed by Race
df_fatalities
df_fatalities.dropna()

fig = px.pie(labels=df_fatalities.race, values=df_fatalities.index, names=df_fatalities.race, hole=0.6)
fig.show()
# Create a Chart Comparing the Total Number of Deaths of Men and Women
fig = px.pie(labels=df_fatalities.gender, values=df_fatalities.index, names=df_fatalities.gender, hole=0.6)
fig.show()
# Create a Box Plot Showing the Age and Manner of Death
box = px.box(df_fatalities,
             y=df_fatalities.age,
             x=df_fatalities.manner_of_death,
             color='manner_of_death')
box.show()
# Were People Armed?
fig = px.pie(labels=df_fatalities.armed, values=df_fatalities.index, names=df_fatalities.armed, hole=0.6)
fig.show()
# How Old Were the People Killed?
plt.figure(figsize=(8,4), dpi=200)

fig = px.bar(df_fatalities, x=df_fatalities.age, y=df_fatalities.index, title="Long-Form Input")

fig.show()
# Race of People Killed
plt.figure(figsize=(8,4), dpi=200)

fig = px.bar(df_fatalities, x=df_fatalities.race, y=df_fatalities.index, title="Long-Form Input")

fig.show()
# Mental Illness and Police Killings
plt.figure(figsize=(8,4), dpi=200)

fig = px.bar(df_fatalities, x=df_fatalities.signs_of_mental_illness, y=df_fatalities.index, title="Long-Form Input")

fig.show()
# In Which Cities Do the Most Police Killings Take Place?
top_10 = df_fatalities.value_counts('city')[:10]   # value counts shows in descending order, can grab top ones
print(top_10)


fig = px.pie(labels=top_10.index, values=top_10, names=top_10.index, hole=0.6)
fig.show()
# Rate of Death by Race
for city in top_10.index:
  print(df_share_race_city.loc[df_share_race_city.City == f'{city} city'])

df_share_race_city.loc[:, ['City', 'share_white', 'share_black', 'share_asian', 'share_native_american', 'share_hispanic']]  # picks out all rows but only the columns specified


df_share_race_city.loc[df_share_race_city.City == 'Los Angeles city']           # only shows the row with the specified city
# Create a Choropleth Map of Police Killings by US State
fig = px.choropleth(df_fatalities,
                    locations='state',
                    locationmode="USA-states",
                    scope="usa",
                    color='id',
                    color_continuous_scale=px.colors.sequential.matter,

                    )
fig.show()
# Number of Police Killings Over Time
df_fatalities.date = pd.to_datetime(df_fatalities.date)

plt.figure(figsize=(8,4), dpi=200)                              # Creates a regression plot
with sns.axes_style('whitegrid'):
  sns.regplot(df_fatalities, x='date', y='id')

plt.show()

# ---------------------------------------------------------- #
# -------------- Main Understanding ------------------------ #
# It is incredibly important to save the changes you make, or they will simply vanish when you run the next line of code.
# You need to save the column as the new column if you change anything, and use that new column. Same goes for variables.
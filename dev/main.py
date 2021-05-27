# %%

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from datetime import date
import datetime
import scipy.stats as st
import plotly.graph_objects as go
import statsmodels.api as sm
import statistics
from scipy import integrate
from pytrends.request import TrendReq

# %%

fname = 'https://raw.githubusercontent.com/IronicNinja/covid19api/master/5_year_period.xlsx'
df = pd.read_excel(fname)

df # show the github data
# %%

# Initialize keywords (without 'covid')
kw_list = ["depression", "anxiety", "panic attack", "insomnia", "loneliness"]
# Initialize colors
word_color_list = ['red', 'blue', 'orange', 'yellow', 'gray']

plt.figure(figsize=(20, 10))
for pos in range(len(kw_list)):
    plt.plot(df['date'], df[kw_list[pos]],
             color=word_color_list[pos],
             linewidth=2)

plt.plot(df['date'], df['covid'], color='black')

plt.xlim(date(2015, 5, 31).toordinal(), date(2020, 5, 31).toordinal())
plt.legend(["depression", "anxiety", "panic attack",
           "insomnia", "loneliness", "covid"])
plt.xlabel('Time')
plt.ylabel('Search Interest')
plt.title('Search Interest of Mental Health in the US - 5 year period')

plt.show() # Plot the figure

# %%
df_5 = df.copy()  # Make a copy of the dataframe

start_5 = date(2020, 5, 31)

# Converts the indices of the dataframe into dates - helps with the graphing. 
# We will use this alot later
def change_axis_time(df, start):
    temp_list = []
    for time in range(len(df)):
        d0 = start-datetime.timedelta(days=7*time)
        d1 = d0.strftime("%Y-%m-%d")
        temp_list.append(d1)

    temp_list.sort()
    df.index = temp_list


change_axis_time(df_5, start_5)
df_5
# %%
plt.figure(figsize=(20, 10))
for pos in range(len(kw_list)):
    fig = sm.tsa.seasonal_decompose(df_5[kw_list[pos]], period=26)
    # Period is every half year
    plt.plot(fig.trend, color=word_color_list[pos], linewidth=3)
    # blur the original
    plt.plot(df[kw_list[pos]], color=word_color_list[pos], linewidth=0.5)

legend_list = []
for keyword in kw_list:
    legend_list.append(keyword + ' trend')
    legend_list.append(keyword + ' org')  # Org for original

plt.xticks([26*n for n in range(math.ceil(len(df_5)/26))])
plt.xlim(0, 261)
plt.ylim(-5, 105)

plt.legend(legend_list)
plt.xlabel('Time')
plt.ylabel('Search Interest')
plt.title('Search Interest of Mental Health in the US - 5 year period, Trend')

plt.show()

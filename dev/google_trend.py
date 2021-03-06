# %% importing
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
from pytrends import dailydata

import os
import sys
import datetime as dt
import matplotlib.dates as mdates
import random
from collections import deque

import utility as util

################################################################################
# %% initialization
dir_name = os.path.dirname(__file__)
date_path = os.path.join(dir_name, 'date.csv')
data_path = os.path.join(dir_name, 'google_trend/0-basic.csv')
fig1_path = os.path.join(dir_name, 'google_trend/1-basic.png')
fig2_path = os.path.join(dir_name, 'google_trend/2-seasonal.png')
fig3_path = os.path.join(dir_name, 'google_trend/3-average.png')
fig4_path = os.path.join(dir_name, 'google_trend/4-linear_regress.png')

# generate random color for plotting (testing purpose)
def rand_color():
    return [random.randint(0, 1) for i in range(3)]

###############################################################################
# %% get the Search Interest && save as .csv
pytrend = TrendReq()
df = pd.read_csv(date_path)
waiting_list = deque(util.kw_list)
while waiting_list:
    key = waiting_list[0]
    print("==========", key, "==========")
    try:
        temp = dailydata.get_daily_data(key, util.start_year,
                                        util.start_month,
                                        util.end_year,
                                        util.end_month,
                                        geo='')
        print("==========", "successed", "==========")
    except:
        print("==========", "failed", "==========")
        continue
    waiting_list.popleft()
    temp.to_csv(data_path)
    temp = pd.read_csv(data_path)
    df[key] = temp[key]
# df = df.drop(labels='isPartial', axis='columns')
df.to_csv(data_path)
df

###############################################################################
# %%
# plot the search interest figure from 2020-02-01 to 2020-10-31
df = pd.read_csv(data_path)
dates = [dt.datetime.strptime(day, '%Y-%m-%d').date() for day in df['date']]

plt.figure(figsize=(20, 10))

for (i, key) in enumerate(util.kw_list):
    plt.plot(dates,
             df[key],
             color=util.keyword_color[i],
             linewidth=2)

plt.legend(util.kw_list)
plt.xlabel('Time')
plt.ylabel('Search Interest')
plt.title('Search Interest of Mental Health in World-wide')
fig1 = plt.gcf()
plt.show()
fig1.savefig(fig1_path)
###############################################################################
# %%
# seasonal trend

df_season = df.copy()
df_season
plt.figure(figsize=(20, 10))
for (i, key) in enumerate(util.kw_list):
    # Period is every half season (6 weeks)
    fig2 = sm.tsa.seasonal_decompose(df_season[key], period=util.season_period)
    plt.plot(fig2.trend,
             color=util.keyword_color[i],
             linewidth=3)
    # blur the original
    plt.plot(df_season[key],
             color=util.keyword_color[i],
             linewidth=0.5)
legend_list = []
for kw in util.kw_list:
    legend_list.append([kw + ' new'])
    legend_list.append([kw + ' old'])

# TODO: fix the x-axis
plt.legend(legend_list)
plt.xlabel('Time')
plt.ylabel('Search Interest')
plt.title('Search Interest of Mental Health and Seasonal Domcomposition in World-wide')

fig2 = plt.gcf()
plt.show()
fig2.savefig(fig2_path)

###############################################################################
# %%
# average trend

pd.set_option('mode.chained_assignment', None) # turn the warning off

df['total'] = float(0)
df
for row in range(len(df)):
    acc = 0
    for keyword in util.kw_list:
        acc += df[keyword][row]
    df['total'][row] = (acc/len(util.kw_list))

df_ave = df.copy()
plt.figure(figsize=(20,10))

fig = sm.tsa.seasonal_decompose(df_ave['total'], period=util.season_period)
plt.plot(fig.trend, color='red', linewidth=3)
plt.plot(df_ave['total'], color='red', linewidth=0.5)

# TODO: fix the x-axis
plt.legend(['average trend new', 'average trend old'])
plt.xlabel('Time')
plt.ylabel('Search Interest')
plt.title('None - average seasonal decomposed trend')

fig3 = plt.gcf()
plt.show()
fig3.savefig(fig3_path)


###############################################################################
# %%
# Linear Regression
x = [n for n in range(util.week_num)] #262 weeks over the 5 year period
y = [df_ave['total'][row] for row in range(util.week_num)]
coe = np.polyfit(x, y, 1)
fn = np.poly1d(coe)

### Figuring out statistics of linear regression
stat = st.linregress(x, y)

### printing stat
print('r value: %.4f' % stat[2])
print('p value: %.4f' % stat[3])
# TODO: understands the below code
# print('+%.4f relevance per year' % (stat[0]*52)) ?????????????????????..?????????????????????

### plotting
plt.figure(figsize=(20,10))
fig = sm.tsa.seasonal_decompose(df_ave['total'], period=util.season_period)
plt.plot(fig.trend, color='red', linewidth=3)
plt.plot(df_ave['total'], color='red', linewidth=0.5)
plt.plot(x, fn(x), linestyle='solid', color='blue', linewidth=2)

# TODO: fix the x-axis
plt.annotate('+%.4f relevance per week' % stat[0], (100, 85), fontsize=15)
plt.legend(['average trend', 'average old', 'line of best fit'])
plt.xlabel('Time')
plt.ylabel('Search Interest')
plt.title('None - Average Trend with Line of Best Fit')

fig4 = plt.gcf()
plt.show()
fig4.savefig(fig4_path)


# %%

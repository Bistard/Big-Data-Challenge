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

import os
import datetime as dt
import matplotlib.dates as mdates

# %% initialization
search_period = '2020-03-01 2020-10-31'
mental_health_keywords = ['anxiety disorder',
                          'insomnia',
                          'depression',
                          'eating disorder',
                          'loneliness']
keyword_color = ['red', 'blue', 'orange', 'yellow', 'gray']
dir_name = os.path.dirname(__file__)
data_path = os.path.join(dir_name, 'google_trend/search_interest_2020-03_2020-10.csv')
fig1_path = os.path.join(dir_name, 'google_trend/search_interest-all.png')

# %%
# get the Search Interest && save as .csv
pytrend = TrendReq()
pytrend.build_payload(kw_list=mental_health_keywords,
                      geo='',
                      timeframe=search_period)
data_frame = pytrend.interest_over_time()
data_frame = data_frame.drop(labels='isPartial', axis='columns')
data_frame.to_csv(data_path)
data_frame

# %%
# plot the search interest figure from 2020-03-01 to 2020-10-31

data_frame = pd.read_csv(data_path)

x_axis = [dt.datetime.strptime(day,'%Y-%m-%d').date() for day in data_frame['date']]

plt.figure(figsize=(20, 10))
for (i, key) in enumerate(mental_health_keywords):
    plt.plot(x_axis,
             data_frame[key],
             color=keyword_color[i],
             linewidth=2)

plt.legend(mental_health_keywords)
plt.xlabel('Time')
plt.ylabel('Search Interest')
plt.title('Search Interest of Mental Health in World-wide (8 months)')
fig1 = plt.gcf()
plt.show()
fig1.savefig(fig1_path)
# %%


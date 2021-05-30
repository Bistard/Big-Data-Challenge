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

import os
import datetime as dt
import matplotlib.dates as mdates

import random
import utility as util
################################################################################
# %% initialization and reading data
dir_name = os.path.dirname(__file__)
fake_news_path = os.path.join(dir_name, 'fake_news/0-basic.csv')
google_trend_path = os.path.join(dir_name, 'google_trend/0-basic.csv')

fig0_path = os.path.join(dir_name, 'fake_vs_google-trend/0-basic.png')

df_fake = pd.read_csv(fake_news_path)
df_google = pd.read_csv(google_trend_path)

df_fake
df_google

################################################################################
# %% plot both data
dates = []
fake_freqs = []
for i, day in enumerate(df_fake['date']):
    d = dt.datetime.strptime(day, '%Y-%m-%d').date()
    if d.year == 2020 and d.month == 11:
        break
    dates.append(d)
    fake_freqs.append(df_fake['frequency'][i])

plt.figure(figsize=(20, 10))
plt.plot(dates, fake_freqs, color='red', linewidth=2)

for (i, key) in enumerate(util.kw_list):
    plt.plot(dates,
             df_google[key],
             color=util.keyword_color[i],
             linewidth=2)

# TODO: more specific titles and legend
plt.legend(['fake news per day'])
plt.xlabel('Time')
plt.ylabel('Search Interest')
plt.title('fake news')
fig0 = plt.gcf()
plt.show()
fig0.savefig(fig0_path)
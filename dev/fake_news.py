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
import datetime as dt
import matplotlib.dates as mdates

import random

from htmldate import find_date
from concurrent.futures import ThreadPoolExecutor 
from operator import itemgetter
import csv

import utility as util

################################################################################
# %% organize data
""" 
files = ["fake_news/NewsFakeCOVID1.csv",
         "fake_news/NewsFakeCOVID2.csv",
         "fake_news/NewsFakeCOVID3.csv",
         "fake_news/NewsFakeCOVID4.csv"]
main_container = []
for path in files:
    with open(path, encoding="utf8") as file:
        lines = file.readlines()
        lines = [x.split(',') for x in lines] 
        urls = [[[int(x[0]), y] for y in x if str(y).startswith('http')] for x in lines ]
   
        [[main_container.append(y) for y in (x)] for x in urls]
 
    
data = []

def dateprinter(url): 
    try:
        required_data = find_date(url[-1])
        data.append([url[0],str(required_data)])
        print(url[0],required_data)
    except:pass    

def main():
    print(len(main_container))
    with ThreadPoolExecutor(max_workers=100) as executor:
        try:
            executor.map(dateprinter , main_container)
            executor.shutdown(wait=True)
        except:
            pass

main()
header = ['key','password']

data = sorted(data, key=itemgetter(0))
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)
 """

 ################################################################################
# %% initialization and reading data
dir_name = os.path.dirname(__file__)
fake_news_path = os.path.join(dir_name, 'fake_news/0-basic.csv')
fig0_path = os.path.join(dir_name, 'fake_news/1-basic.png')
fig1_path = os.path.join(dir_name, 'fake_news/2-seasonal.png')
df_fake = pd.read_csv(fake_news_path)
df_fake

################################################################################
# %% plot the graph
dates = []
freqs = []
for i, day in enumerate(df_fake['date']):
    d = dt.datetime.strptime(day, '%Y-%m-%d').date()
    if d.year == 2020 and d.month == 11:
        break
    dates.append(d)
    freqs.append(df_fake['frequency'][i])

plt.figure(figsize=(20, 10))
plt.plot(dates, freqs, color='red', linewidth=2)

# TODO: more specific titles and legend
plt.legend(['fake news per day'])
plt.xlabel('Time')
plt.ylabel('Search Interest')
plt.title('fake news')
fig0 = plt.gcf()
plt.show()
fig0.savefig(fig0_path)


# %% seasonal trend

df_season = df_fake.copy()
plt.figure(figsize=(20, 10))
# Period is every half season (6 weeks)
fig1 = sm.tsa.seasonal_decompose(freqs, period=util.season_period)
plt.plot(fig1.trend, color='red', linewidth=3)
# blur the original
plt.plot(freqs, color='red', linewidth=0.5)
# TODO: more specific titles and legend
plt.legend(['fake news per day'])
plt.xlabel('Time')
plt.ylabel('Fake News Count')
plt.title('Fake News Per Day and Seasonal Domcomposition in World-wide')

fig1 = plt.gcf()
plt.show()
fig1.savefig(fig1_path)
# %%

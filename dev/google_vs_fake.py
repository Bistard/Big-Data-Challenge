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

################################################################################
# %% initialization and reading data
dir_name = os.path.dirname(__file__)
fake_news_path = os.path.join(dir_name, 'fake_news/0-basic.csv')
google_trend_path = os.path.join(dir_name, 'google_trend/0-basic.csv')

df_fake = pd.read_csv(fake_news_path)
df_google = pd.read_csv(google_trend_path)

df_fake

# df_google

# %%

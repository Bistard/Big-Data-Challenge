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
# %% initialization
dir_name = os.path.dirname(__file__)
fake_news_path = os.path.join(dir_name, 'fake_news/.csv')

df_fake = pd.read_csv(fake_news_path)

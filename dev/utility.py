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
import sys
import datetime as dt
import matplotlib.dates as mdates
import random

kw_list = ['depression',
           'loneliness',
           'panic attack',
           'anxiety',
           'insomnia']
keyword_color = ['red', 'blue', 'orange', 'yellow',
                 'gray', 'green', 'violet', 'black',
                 'magenta', 'cyan']

search_period = '2020-02-01 2020-11-01'
start_year = 2020
end_year = 2020
start_month = 2
end_month = 10
season_period = 6 # number of weeks
week_num = round(abs(date(2020, 11, 1) - date(2020, 2, 1)).days / 7)

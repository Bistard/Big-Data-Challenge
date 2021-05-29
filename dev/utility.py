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

search_period = '2020-02-01 2020-11-01'
season_period = 6 # number of weeks
week_num = round(abs(date(2020, 11, 1) - date(2020, 2, 1)).days / 7)

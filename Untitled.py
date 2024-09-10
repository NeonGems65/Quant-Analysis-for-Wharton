#!/usr/bin/env python
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import certifi
import json

def get_jsonparsed_data(url):
    response = urlopen(url, cafile=certifi.where())
    data = response.read().decode("utf-8")
    return json.loads(data)

urlAAPL = ("https://financialmodelingprep.com/api/v3/key-metrics/AAPL?period=annual&apikey=V6J4FVBPQvPyJAWmcPry9kb8pVlTgibE")
urlNVDA = ("https://financialmodelingprep.com/api/v3/key-metrics/NVDA?period=annual&apikey=V6J4FVBPQvPyJAWmcPry9kb8pVlTgibE")
urlArray = [get_jsonparsed_data(urlAAPL), get_jsonparsed_data(urlNVDA)]


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from pandas_datareader import data as pdr
import yfinance as yf

 # import data 
def get_data(stocks, start, end):
    stockData = yf.download(stocks, start=start, end=end)
    stockData = stockData["Close"]
    returns = stockData.pct_change()
    meanReturns = returns.mean()
    covMatrix = returns.cov()
    return meanReturns, covMatrix

stockList = ["NVDA", "AAPL"]
stocks = ' '.join(stockList)
endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days=300)

meanReturns, covMatrix = get_data(stocks, startDate, endDate)

weights = np.random.random(len(meanReturns))
weights /= np.sum(weights)

# Monte Carlo Method
# number of simulations 
mc_sims = 100
T = 100

meanM = np.full(shape=(T, len(weights) ), fill_value=meanReturns)
meanM = meanM.T

portfolio_sims = np.full(shape=(T,mc_sims), fill_value=0.0)

initialPortfolio = 10000

for m in range(0, mc_sims):
    # MC loops
    Z = np.random.normal(size=(T, len(weights)))
    L = np.linalg.cholesky(covMatrix)
    dailyReturns = meanM + np.inner(L, Z)
    portfolio_sims[:,m] = np.cumprod(np.inner(weights,dailyReturns.T)+1)*initialPortfolio

plt.plot(portfolio_sims)
plt.ylabel("Portfolio Value ($)")
plt.xlabel("Days")
plt.title("MC simulation of a stock portfolio")
plt.show()


print(weights)


print(meanReturns)
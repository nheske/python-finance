# created with jupyter nbconvert --to script *.ipynb

# !/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/nheske/python-finance/blob/main/python-for-finance/Python_For_Finance.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# In[1]:


# Description: This is a python program for finance
# This program will show you how to compute portfolio simple returns, get daily returns and volatility, etc. 


# In[6]:
# import pip
# pip.main(['install', 'pandas_datareader'])

from datetime import datetime
import time
import numpy as np
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

# In[7]:


# Get stock symbols for FAANG
stockSymbols = ["FB", "AMZN", "AAPL", "NFLX", "GOOG"]

# In[8]:


# Get stock starting date
stockStartDate = '2013-01-01'

# In[9]:


# Get today's date and format it in the form YYY-mm-dd
today = time.strftime('%Y-%m-%d')
print(today)

# In[10]:


# Get the number of assests in the portfolio 
numAssets = len(stockSymbols)
# Print the number of assests in your portfolio 
print('You have ' + str(numAssets) + ' assets in your portfolio')


# In[11]:


# Create a function to get the stock price(s) of the portfolio 
def getMyPortfolio(stocks=stockSymbols, start=stockStartDate, end=today, col='Adj Close'):
    data = web.DataReader(stocks, data_source='yahoo', start=start, end=end)[col]
    return data


# In[12]:


# Get the stock portfolio Adj. Close price 
my_stocks = getMyPortfolio(stockSymbols)
# Show my stocks
my_stocks


# In[13]:


# Create a function to visualize the stock/portfolio
def showGraph(stocks=stockSymbols, start=stockStartDate, end=today, col='Adj Close'):
    # Create the title
    title = 'Portfolio ' + col + ' Price History'

    # Get the stocks
    my_stocks = getMyPortfolio(stocks=stocks, start=start, end=end, col=col)

    # Visualize the price history
    plt.figure(figsize=(12.2, 4.5))
    # Loop through each stock and plot the Adj Close for each day
    for c in my_stocks.columns.values:
        plt.plot(my_stocks[c], label=c)

    plt.title(title)
    plt.xlabel('Date', fontsize=18)
    plt.ylabel(col + ' Price USD ($)', fontsize=18)
    plt.legend(my_stocks.columns.values, loc='upper left')
    plt.show()


# In[14]:


# Show the adjusted close price of FAANG                              
showGraph(stockSymbols)

# In[ ]:


# try another style https://www.dunderdata.com/blog/view-all-available-matplotlib-styles
# available = ['default'] + plt.style.available
# for i, style in enumerate(available):
#     plt.style.use(style)
#     showGraph(stockSymbols)


# In[15]:


# Calculate Simple Returns
daily_simple_returns = my_stocks.pct_change(1)
daily_simple_returns

# In[16]:


# Show the stock correlation
daily_simple_returns.corr()

# In[17]:


# Show the co-variance matrix for simple returns (diagonal is the daily variance)
daily_simple_returns.cov()

# In[18]:


# Show the variance
daily_simple_returns.var()

# In[19]:


import math

math.sqrt(0.000471)

# In[20]:


# Print the standard deviation
print("The Stock Volatility:")
daily_simple_returns.std()

# In[21]:


plt.style.use('seaborn-poster')
plt.style.use('fivethirtyeight')

# In[22]:


# Visualize the stocks daily simple returns / volatility 
plt.figure(figsize=(12, 4.5))  # Set the figure size (width, height)
# Loop through each stock and plot the simple returns for each day
for c in daily_simple_returns.columns.values:
    plt.plot(daily_simple_returns.index, daily_simple_returns[c], lw=2, label=c)
# Place the legend in the upper left corner with font size of 10
plt.legend(loc='upper right', fontsize=10)
plt.title('Volatility')
plt.ylabel('Daily Simple Returns')  # Label the Y-axis simple returns
plt.xlabel('Date')
plt.show()

# In[23]:


# Show the mean / average of the daily simple return
dailyMeanSimpleReturns = daily_simple_returns.mean()
# Print the daily mean simple return
print("The daily mean simple return: ")
print(dailyMeanSimpleReturns)

# In[24]:


# Calculate the expected portfolio daily performance with weights
# 40% FB, 10% AMZN, 30% AAPL, 10% NFLX, 10% GOOG
randomWeights = np.array([0.4, 0.1, 0.3, 0.1, 0.1])
portfolioSimpleReturn = np.sum(dailyMeanSimpleReturns * randomWeights)
# Print the daily expected portfolio return
print("The daily expected portfolio return: " + str(portfolioSimpleReturn))

# In[25]:


# Print the expected annual portfolio simple return
# The number 253 was calculated from 365.25 (days on average per year) * 5/7 (proportion work days per week) — 6 (weekday holidays) — 3*5/7 (fixed date holidays) = 252.75 ≈ 253.
print("Expected annualised portfolio simple return : " + str(portfolioSimpleReturn * 253))

# In[26]:


# Calculate the growth of our investment
dailyCumulSimplReturn = (daily_simple_returns + 1).cumprod()
# Show the cumulative simple return
dailyCumulSimplReturn

# In[27]:

# Visualize the daily cumulative simple returns
# switch from plt way to fig, ax way: Axes methods vs. pyplot
# fig = plt.figure(figsize=(12.2,4.5))
# for c in dailyCumulSimplReturn.columns.values:
#   plt.plot(dailyCumulSimplReturn.index, dailyCumulSimplReturn[c], lw=2, label=c)
# # Place the legend in the upper left corner with font size of 10
# plt.legend(loc='upper left', fontsize=10)
# plt.xlabel("Date")
# plt.ylabel("Growth of $1 investment")
# plt.title("Daily Cumulative Simple Returns")
# plt.show()
fig, ax = plt.subplots(figsize=(10, 6))
for c in dailyCumulSimplReturn.columns.values:
    ax.plot(dailyCumulSimplReturn.index, dailyCumulSimplReturn[c], lw=2, label=c)
leg = ax.legend(loc='upper left', fontsize=10)
ax.set_xlabel('Date', fontsize=10)
ax.set_ylabel('Growth of $1 investment', fontsize=10)
ax.set_title('Daily Cumulative Simple Returns', fontsize=10)
ax.tick_params(axis='both', which='major', labelsize=8)
ax.tick_params(axis='both', which='minor', labelsize=6)
fig.tight_layout()
plt.show()

# In[ ]:


# In[ ]:

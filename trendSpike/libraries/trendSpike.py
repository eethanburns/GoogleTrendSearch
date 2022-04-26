from pathlib import Path

import sys
sysPath = str(Path.cwd())+"\libraries"
sys.path.append(sysPath)

import google
import scipy
import pandas
from scipy import signal
from googlesearch import search
from pytrends.request import TrendReq
from GoogleNews import GoogleNews
import warnings
from scipy.signal import argrelextrema
import numpy as np
from tkinter import *

#data = scipy.signal.argrelextrema(data.values,np.greater)


if not sys.warnoptions:
     warnings.simplefilter("ignore")

def printDict(dictionary):
     for key, value in dictionary.items():
          print(key, ' : ', value)

def timetoStr(timestamp):
     return str(timestamp)[0:10]

def fixSlash(timestamp):
     reorder = timestamp[5:7]+"/"+timestamp[8:10]+"/"+timestamp[0:4]
     return reorder

def addMonth(timestamp):
     return pandas.to_datetime(timestamp) + pandas.DateOffset(months=1)

def addDay(timestamp):
     return pandas.to_datetime(timestamp) + pandas.DateOffset(days=1)

def subtractDay(timestamp):
     return pandas.to_datetime(timestamp) + pandas.DateOffset(days=-1)

def maxTrend(topquery):
     pytrends = TrendReq(hl='en-US',tz=360)
     kw_list = [topquery]
     pytrends.build_payload(kw_list, cat=0, timeframe='all')
     data = pytrends.interest_over_time()
     mydict = data.to_dict()
     finaldict = mydict[topquery]
     return max(finaldict, key=finaldict.get)

def peakTrends(topquery,peakCount,sort):
     pytrends = TrendReq(hl='en-US',tz=360)
     kw_list = [topquery]
     pytrends.build_payload(kw_list, cat=0, timeframe='all')
     data = pytrends.interest_over_time()
     data = data.drop(columns=['isPartial'])
     dateChart = data.reset_index(drop=False)
     datapeaks = data.values.flatten()
     datapeaks = scipy.signal.find_peaks(datapeaks,prominence=5)
     peaks = datapeaks[0]
     amounts = datapeaks[1]['prominences']
     yx = sorted(zip(amounts,peaks),reverse=True)
     x_sorted = [x for y, x in yx]

     peakList = []
     if sort == "Popularity":
          for x in x_sorted[0:peakCount]:
               peakList.append(dateChart.iloc[x,0])
     else:
          for x in x_sorted[0:peakCount]:
               peakList.append(dateChart.iloc[x,0])
          peakList.sort()
     return peakList

def maxTrendTime(topquery,month):
     pytrends = TrendReq(hl='en-US',tz=360)
     kw_list = [topquery]
     pytrends.build_payload(kw_list, cat=0, timeframe=timetoStr(month)+" "+timetoStr(addMonth(month)))
     data = pytrends.interest_over_time()
     mydict = data.to_dict()
     finaldict = mydict[topquery]
     return max(finaldict, key=finaldict.get)

def maxDay(topquery):
     return maxTrendTime((topquery),maxTrend(topquery))


def searchBig(query):
     finalQuery = query+" after:"+timetoStr(subtractDay(maxDay(query)))+" before:"+timetoStr(addDay(maxDay(query)))
     print(finalQuery)

     for j in search(finalQuery, tld="co.in", num=10, stop=10, pause=2):
          print(j)

def searchNews(query,day,results):
     try:
          googlenews = GoogleNews()
          googlenews.set_time_range(fixSlash(timetoStr(subtractDay(day))),fixSlash(timetoStr(addDay(day))))
          googlenews.search(query)
     except TypeError:
          pass
     newsCount = googlenews.total_count()
     if newsCount > results:
          print("-------------------------------------")

          print(fixSlash(timetoStr(day)))
          for x in range(0,results):
               print(googlenews.get_texts()[x])
     else:
          print("-------------------------------------")
          print(fixSlash(timetoStr(day)))
          for x in range(0,newsCount):
               print(googlenews.get_texts()[x])
          print("(Not enough results)")
          

def searchList(query,peaks,articles,sort):
     print("-------------------------------------")
     print("Keyword: "+query)
     dateList = peakTrends(query,peaks,sort)
     for x in dateList:
          searchNews(query,maxTrendTime(query,x),articles)


def askforSearch():
     x = input("Search? ")
     results = int(input("Results? "))
     searchNews(x,maxDay(x),results)
     askforSearch()





import json
import numpy as np
import os
import pandas as pd
import urllib2

def collectData():
  # connect to poloniex's API
  url = 'https://poloniex.com/public?command=returnChartData&currencyPair=USDT_BTC&start=1518393227&end=9999999999&resolution=auto'

  # parse json returned from the API to Pandas DF
  openUrl = urllib2.urlopen(url)
  r = openUrl.read()
  openUrl.close()
  d = json.loads(r.decode())
  df = pd.DataFrame(d)

  original_columns=[u'close', u'date', u'high', u'low', u'open']
  new_columns = ['Close','Timestamp','High','Low','Open']
  df = df.loc[:,original_columns]
  df.columns = new_columns
  df.to_csv('data/bitcoin.csv',index=None)
  print('Data Collected')
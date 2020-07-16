# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 22:58:16 2020

@author: Bjergsen
"""

import requests

import pandas as pd

import numpy as np


url = 'https://api.doctorxiong.club/v1/fund/position'

code = input('please enter your code: ')

params = {'code':code}
   
r = requests.get(url,params=params).json()

stockList = r['data']['stockList']

m = len(stockList)

#fundTitle = r['data']['title']
#
#fundTitle = fundTitle[:(fundTitle.find('0')-3)]

stockDF = pd.DataFrame(stockList,index = np.tile(code,m),columns = ['stockid','stockName','rate','1','2'])

#stockDF['fundName'] = np.tile(fundTitle,m)

stock_data = stockDF.loc[:,['stockName','rate']]

#stock_data.index.name = 'fundId'

print(stock_data)






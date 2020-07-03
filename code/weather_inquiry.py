# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 22:24:19 2020

@author: Bjergsen
"""

import requests

import pandas as pd

url = 'http://www.tianqiapi.com/api?version=v9&appid=23035354&appsecret=8YvlPNrz'

r = requests.get(url)

t = r.json()

hourly_weather = t['data'][1]['hours']  #这里应该改成0

df = pd.DataFrame(hourly_weather)

working_time = df.iloc[[0,1,2]]

closing_time = df.iloc[[11,12,13,14]]

working_time_weather = working_time.loc[:,'wea_img'].tolist()

closing_time_weather = closing_time.loc[:,'wea_img'].tolist()

def get_work_message():
      
    if 'yu' in working_time_weather:
        
        work_message = '1'
        
    else:
        
        work_message = '0'
        
    return work_message


def get_close_message():
      
    if 'yu' in closing_time_weather:
        
        close_message = '1'
        
    else:
        
        close_message = '0'
        
    return close_message


def get_message():
    
    if get_work_message() == '1' and get_close_message() == '0':
        
        msg = working_time.iloc[0,0] + '-' + working_time.iloc[-1,0] + '会下雨熬，早上记得带伞'
        
    if get_close_message() == '1' and get_work_message() == '0':
        
        msg = closing_time.iloc[0,0] + '-' + closing_time.iloc[-1,0] + '会下雨熬，早上记得带伞'
        
    if get_close_message() == '0' and get_work_message() == '0':
        
        msg = '上下班时间都不会下雨熬，男生可以不带伞，女生可以带着遮阳辣'
    print(msg)

get_message()
    
    

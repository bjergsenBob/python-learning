# -*- coding: utf-8 -*-
"""
Created on Fri May 15 16:32:02 2020

@author: baobingsen
"""



import requests

import datetime

import schedule

import time

import pandas as pd
 


url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=51e02d90-139c-4515-b839-4c8ff3013b03'

headers = {'Content-Type':'text/plain'}

send_message = ['中午点外卖啦！！！','晚上点外卖啦！！！','周四写周报啦！！！']

#获取当前周几
def get_current_time():
    
    dayOfWeek = datetime.datetime.now().isoweekday()
       
    return dayOfWeek

#发送函数
def send_msg(content):
    
    data = {
        'msgtype':'text',
        'text':{
            'content':content,
            }
        }
    
    r = requests.post(url,headers = headers,json = data)

    print(r.text)


#获取是否下雨
def get_rain_message():
    
    weather_url = 'https://tianqiapi.com/api?version=v1&appid=86739165&appsecret=FqnR56Jl&cityid=101020100'
    
    r = requests.get(weather_url).json()
    
    # today_wea_img = r['data'][0]['wea_img']
    
    tomorrow_wea_img = r['data'][1]['wea_img']
    
    # if today_wea_img = 'yu':
        
    #     today_message = '今天会下雨嗷，记得带伞'
        
    if tomorrow_wea_img == 'yu':
        
        message = '明天会下雨嗷，记得带伞'
        
    # else：
    #     message = '明天不会下雨嗷'
        
    return message

        
#下雨提醒    
def weather_time():
    
    content = get_rain_message()
    
    send_msg(content)
    

#获取股票信息
def get_fund_message():
    
    fund_url = 'https://api.doctorxiong.club/v1/stock/board' 
    
    r = requests.get(fund_url).json()
    
    fund_data = r['data']
    
    data_pd = pd.DataFrame(fund_data)
    
    print(data_pd)

#吃饭提醒   
def lunch_time(content='中午点外卖辣！！！'):
    
    dayOfWeek = get_current_time()
    
    if dayOfWeek in [1,2,3,4,5]:
        
            send_msg(content)


def dinner_time(content='晚上点外卖辣！！！'):
    
    dayOfWeek = get_current_time()
    
    if dayOfWeek in [1,2,3,4,5]:
        
        send_msg(content)


#周报提醒
def weekly_time(content='周四写周报辣！！！'):
    
    send_msg(content)
    

#定时发送            
def register():

    schedule.every(1).day.at('11:30').do(lunch_time)
    
    schedule.every(1).day.at('11:40').do(lunch_time,content='再不点12.30就没得吃辣')

    schedule.every(1).day.at('17:30').do(dinner_time)
    
    schedule.every(1).day.at('17:40').do(dinner_time,content='再不点晚上又要吃罗森辣')
    
    schedule.every().thursday.at('16:50').do(weekly_time)

    schedule.every().thursday.at('17:00').do(weekly_time,content='算了，不写好像也没啥问题')
    
    schedule.every(1).day.at('19:00').do(weather_time)

def start_scheduler():
    
    while True:
        
        schedule.run_pending()
        
        time.sleep(60)
        
        
def main():

    register()
    
    start_scheduler()
    
    
if __name__ == '__main__':
    
    main()


    
    







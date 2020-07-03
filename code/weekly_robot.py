# -*- coding: utf-8 -*-
"""
Created on Fri May 15 16:32:02 2020

@author: baobingsen
"""



import requests

import datetime

import schedule

import time


url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=51e02d90-139c-4515-b839-4c8ff3013b03'

headers = {'Content-Type':'text/plain'}

send_message = ['中午点外卖啦！！！','晚上点外卖啦！！！','周四写周报啦！！！']


def get_current_time():
    
    dayOfWeek = datetime.datetime.now().isoweekday()
       
    return dayOfWeek


def send_msg(content):
    
    data = {
        'msgtype':'text',
        'text':{
            'content':content,
            }
        }
    
    r = requests.post(url,headers = headers,json = data)

    print(r.text)


def lunch_time(content='中午点外卖辣！！！'):
    
    dayOfWeek = get_current_time()
    
    if dayOfWeek in [1,2,3,4,5]:
        
            send_msg(content)


def dinner_time(content='晚上点外卖辣！！！'):
    
    dayOfWeek = get_current_time()
    
    if dayOfWeek in [1,2,3,4,5]:
        
        send_msg(content)


def weekly_time(content='周四写周报辣！！！'):
    
    send_msg(content)
    
            
def register():

    schedule.every(1).day.at('11:30').do(lunch_time)
    
    schedule.every(1).day.at('11:40').do(lunch_time,content='再不点12.30就没得吃辣')

    schedule.every(1).day.at('17:30').do(dinner_time)
    
    schedule.every(1).day.at('17:40').do(dinner_time,content='再不点晚上又要吃罗森辣')
    
    schedule.every().thursday.at('16:50').do(weekly_time)

    schedule.every().thursday.at('17:00').do(weekly_time,content='算了，不写好像也没啥问题')
    

def start_scheduler():
    
    while True:
        
        schedule.run_pending()
        
        time.sleep(60)
        
        
def main():

    register()
    
    start_scheduler()
    
    
if __name__ == '__main__':
    
    main()


    
    







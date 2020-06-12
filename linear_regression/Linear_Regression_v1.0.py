# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 16:50:08 2020

@author: baobingsen
"""


import pandas as pd

from matplotlib import pyplot as plt



#读取数据
def get_data_set():
    
    data_set = pd.read_csv('D:\py\习题\机器学习\linear regression\Salary_Data.csv')
    
    return data_set
    
data_set = get_data_set()


#画图
def get_plot():
        
    plt.scatter(data_set.x,data_set.y)



def get_items():
    
    a = 0

    b = 0
    
    #确定学习速率
    c = 0.001
    
    m = len(data_set.x)
    x2 = data_set.x
    
    precision = 0.0001
    cnt = 0
    
    monitor_df = pd.DataFrame(columns=['cnt','t'])
    
    while True:
        cnt += 1
        h0 = a * x2 + b
        t = sum(h0 - data_set.y)
        new = pd.DataFrame({'cnt':cnt,'t':t},index=['0'])
        monitor_df = monitor_df.append(new,ignore_index=True)
        # print(monitor_df)
        if cnt % 1000 == 0:
            #c *= 1.01
            print(t)
            # print(monitor_df)
            plt.scatter(monitor_df.cnt,monitor_df.t)
            #print(h0)
            #print(data_set.y)
            #break
        if abs(t) > precision:
            b = b - c / m * t
            a = a - c / m * sum((h0 - data_set.y) * x2)
        else:
            break
    print(round(a,2),round(b,2))
    
        
import time
s = time.time()
get_items()
e = time.time()
print(e-s)

    

# =============================================================================
# def get_items2():
#     
#     a = 0
# 
#     b = 0
#     
#     #确定学习速率
#     c = 0.001
#     
#     m = len(data_set.x)
#     #print(data_set.x)
#     #print(data_set.y)
#     
# #    precision = 0.001
#     
#     while True:
#     #for i in range(10000): 
#         #if i % 1000 == 0:
#         #    c *= 0.99
#         h0 = a * data_set.x + b
#         #print(a,b)
#         #cost = sum((h0 - data_set.y)**2)
#         
#         if abs(sum(h0 - data_set.y)) > 0.0001:
#             
#             #gradient = c / m * sum(h0 - data_set.y)
#             #print(gradient)
#             #temp_a = a - gradient 
#             #temp_b = b - gradient
#             
#             #gradient = c / m * sum((h0 - data_set.y)*data_set.x)
#             #print(gradient)
#             #a -= gradient * sum(data_set.x)
#             #b -= gradient
#             
#             #a -= c/m * sum((h0 - data_set.y)*data_set.x)
#             #b -= c/m * sum(h0 - data_set.y)
#             t =  c/m * (h0 - data_set.y)
#             #print(h0 - data_set.y)
#             #print(sum(t))
#             a -= sum(t*data_set.x)
#             b -= sum(t)
#         else:
#             break
# 
#     print(a,b)
# =============================================================================    

    
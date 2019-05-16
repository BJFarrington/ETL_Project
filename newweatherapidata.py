#!/usr/bin/env python
# coding: utf-8

# In[25]:


import csv

import requests
from datetime import datetime
import pandas as pd
from api_keys import api_key
import requests
import json


# In[ ]:





# In[ ]:





# In[10]:


longitude = -114.7420
latitude = 44.0682
all_data= []
p = +1


for b in range (1,11):
        
        for a in range (1, 10):
            month_day = f'2017-0{b}-0{a}T12:00:00'
            idaho = f'https://api.darksky.net/forecast/{api_key}/{latitude},{longitude},{month_day}'
            response = requests.get(idaho).json()
            timeA = response["currently"]['time']
            temp = response["currently"]['temperature']
            t_t = {"Date": timeA, "Temp" : temp}
            all_data.append(t_t )
            print(timeA,temp)
        for a in range (10, 28):
            month_day = f'2017-0{b}-{a}T12:00:00'
            idaho = f'https://api.darksky.net/forecast/{api_key}/{latitude},{longitude},{month_day}'
            response = requests.get(idaho).json()
            timeA = response["currently"]['time']
            temp = response["currently"]['temperature']
            t_t = {"Date": timeA, "Temp" : temp}
            all_data.append(t_t )
            print(timeA,temp)
            
        
            
        


# In[23]:


df = pd.DataFrame(all_data)


# In[24]:



df
    


# In[28]:


df['Date'] = pd.to_datetime(df['Date'],unit='s')
df


# In[33]:


export_csv = df.to_csv(r"C:\Users\BWayn\Desktop\Rice-BootCamp\ETL_Project\ETL_Project\2017_Idaho_weather_data.csv ", index = None, header=True)


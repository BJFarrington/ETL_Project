#!/usr/bin/env python
# coding: utf-8

# In[19]:


import csv

import requests

import pandas as pd
from config import api_key
import requests
import json


# In[ ]:





# In[ ]:





# In[20]:


longitude = -114.7420
latitude = 44.0682
all_data={} 
p = +1


for b in range (3,7):
        
        for a in range (1, 10):
            month_day = f'2017-0{b}-0{a}T12:00:00'
            idaho = f'https://api.darksky.net/forecast/{api_key}/{latitude},{longitude},{month_day}'
            response = requests.get(idaho).json()
            timeA = response["currently"]['time']
            temp = response["currently"]['temperature']
            all_data.append("Date":timeA, "Temp":temp )
            print(timeA,temp)
        for a in range (10, 26):
            month_day = f'2017-0{b}-{a}T12:00:00'
            idaho = f'https://api.darksky.net/forecast/{api_key}/{latitude},{longitude},{month_day}'
            response = requests.get(idaho).json()
            timeA = response["currently"]['time']
            temp = response["currently"]['temperature']
            all_data.append("Date":timeA, "Temp":temp )
            print(timeA,temp)
            
        
            
        


# In[33]:





# In[ ]:




    

